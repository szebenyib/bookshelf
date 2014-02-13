from django.shortcuts import render, render_to_response, get_object_or_404
from mercator.models import Entry

def entries_index(request):
    return render(request, 'mercator/entry_index.html',
        { 'entry_list': Entry.objects.filter(status=Entry.LIVE_STATUS) })

def entry_detail(request, year, month, day, slug):
#    import datetime, time
#    date_stamp = time.strptime(year+month+day, "%Y%b%d")
#    pub_date = datetime.date(*date_stamp[:3])
    #entry = Entry.objects.filter(slug=slug)
    entry = get_object_or_404(Entry, slug=slug)
    print entry
    """
    entry = get_object_or_404(Entry,
                pub_date__year=pub_date.year,
                pub_date__month=pub_date.month,
                pub_date__day=pub_date.day,
                slug=slug)
    """
    return render_to_response('mercator/entry_detail.html', { 'entry': entry })
    #return render(request, 'mercator/entry_detail.html', { 'entry': entry })
"""
    return render_to_response('mercator/entry_detail.html',
            { 'entry': Entry.objects.get(pub_date__year=pub_date.year,
                pub_date__month=pub_date.month,
                pub_date__day=pub_date.day,
                slug=slug) })
    return render_to_response('mercator/entry_detail.html',
            { 'entry': entry })
            """
