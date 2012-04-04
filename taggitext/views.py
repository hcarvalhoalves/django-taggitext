from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.utils.simplejson import dumps

from taggit.models import Tag


RESULTS = getattr(settings, 'TAGGITEXT_RESULTS_LIMIT', 20)


# TODO: Cache the results
def search_tags(request):
    try:
        query = request.GET['q']
        tags = Tag.objects.filter(name__icontains=query).values_list('name', flat=True)[:RESULTS]
        response = sorted(tags, key=lambda t: len(t))
        return HttpResponse(dumps(response), mimetype='application/json')
    except KeyError:
        return HttpResponseBadRequest()
