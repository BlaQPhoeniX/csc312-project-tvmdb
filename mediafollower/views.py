# Create your views here.
from mediafollower.models import Media, Genre
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist 
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import datetime
import cjson

def events(request):
    start = int(request.GET.get('start', ''))
    end = int(request.GET.get('end', ''))
    start = datetime.datetime.fromtimestamp(start)
    end = datetime.datetime.fromtimestamp(end)
    f = '%Y-%m-%d %H:%M'
    d = []
    u = request.user
    if u.is_authenticated():
        mm = u.userprofile.media.all()
    else:
        mm = Media.objects.all()
    for m in mm:
        url = '/media/%d' % m.id
        for e in m.episode_set.filter(airdate__gte=start, airdate__lte=end):
            title = '%s - %dx%d - %s' % (m.title, e.season, e.number, e.title)
            startd = e.airdate.strftime(f)
            endd = ( e.airdate + datetime.timedelta(minutes=60) ).strftime(f)
            d.append({'title' : title,
                      'start' : startd,
                      'end' : endd,
                      'url' : url,
                      'allDay' : False})
    t = cjson.encode(d)
    return HttpResponse(t, content_type='application/json')

def search(request):
    #d = [str(s) for s in Media.objects.values_list('title', flat=True)]
    d = [{'id':k, 'title':str(v)} for k,v in Media.objects.values_list('id', 'title')]
    e = {'results':d}
    t = cjson.encode(e)
    return HttpResponse(t, content_type='application/json')

@login_required
def subscribe(request, i):
    u = request.user
    up = u.userprofile
    try:
        m = Media.objects.get(id=i)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    up.media.add(m)
    t = cjson.encode('success')
    return HttpResponse(t, content_type='application/json')

@login_required
def unsubscribe(request, i):
    u = request.user
    up = u.userprofile
    try:
        m = Media.objects.get(id=i)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    up.media.remove(m)
    t = cjson.encode('success')
    return HttpResponse(t, content_type='application/json')

def media(request, i=None):
    h = []
    u = request.user
    if u.is_authenticated():
        h = u.userprofile.media.values_list('id', flat=True)
    if i:
        try:
            m = Media.objects.get(id=i)
            return render(request, 'media_1.html', {'media':m})
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/media')
    mm = Media.objects.all().order_by('title')
    return render(request, 'media_N.html', {'medias':mm, 'h':h})

def media_gen(request, genre):
    h = []
    u = request.user
    if u.is_authenticated():
        h = u.userprofile.media.values_list('id', flat=True)
    try:
        g = Genre.objects.get(id=genre)
        mm = g.media_set.all().order_by('title')
        gname = ' - %s' % g.name
    except ObjectDoesNotExist:
        mm = []
    return render(request, 'media_N.html', {'medias':mm, 'g':gname, 'h':h})
