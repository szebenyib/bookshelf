from django.conf.urls import *

from mercator.models import Entry

entry_info_dict = {
    'queryset': Entry.objects.all(),
    'date_filed': 'pub_date',
}

urlpatterns = patterns('',
    (r'^$', 'mercator.views.entries_index'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'mercator.views.entry_detail'),
)
