import datetime

from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
from markdown import markdown

class Category(models.Model):
    title = models.CharField(max_length=250,
            help_text='Maximum 250 characters.')
    slug = models.SlugField(unique=True,
            help_text='Created from title, feel free to adjust. Must be unique.')
    description = models.TextField()

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s/" % self.slug

class Entry(models.Model):
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )

    #Core fields
    title = models.CharField(max_length=250,
            help_text='Maximum 250 characters.')
    excerpt = models.TextField(blank=True,
            help_text='Optional.')
    body = models.TextField()
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique=True)

    #Metadata
    author = models.ForeignKey(User)
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS,
            help_text='Only entries with live status will be publicly displayed.')

    #Categorization
    categories = models.ForeignKey(Category)
    tags = TaggableManager()

    #Stores generated html
    excerpt_html = models.TextField(editable=False,
            blank=True)
    body_html = models.TextField(editable=False,
            blank=True)

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/weblog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)

    def save(self, force_insert=False, force_update=False):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save(force_insert, force_update)
