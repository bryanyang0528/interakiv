import logging
import json
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import (
    HttpResponse, HttpResponseRedirect,
    HttpResponseBadRequest, HttpResponseNotAllowed
)
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone

from streamit.models import Show
from streamit.utils import generate_key


logger = logging.getLogger('stream_auth')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
chformatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s', datefmt='[%d/%b/%Y %H:%M:%S]')
ch.setLevel(logging.INFO)
ch.setFormatter(chformatter)
logger.addHandler(ch)


class StreamView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        s=Show.objects.last()
        return render(request, self.template_name, {'show': s})


@require_POST
@csrf_exempt
def on_publish(request):

    stream_key = request.POST.get('name', '')
    show = None
    try:
        show = Show.objects.get(key=stream_key)
    except Show.DoesNotExist as err:
        logger.warning('Invalid key, publish abort.')
        return HttpResponseBadRequest('Invalid publish key.')

    # TODO: auth check
    if show.activated:
        if show.on_air:
            return HttpResponseNotAllowed('Show already start')
        else:
            now = timezone.now()
            m3u8 = generate_key('{}{}{}'.format(show.uid, show.key, now.timestamp()))
            show.last_on = now
            show.last_off = None
            show.m3u8 = m3u8
            show.on_air = True
            show.save()
            logger.info('Publish started.')
            return HttpResponseRedirect(m3u8)
    else:
        logger.warning('Show inactivated, publish cancelled.')
        return HttpResponseNotAllowed('Show inactivated.')




@require_POST
@csrf_exempt
def on_publish_done(request):
    stream_key = request.POST.get('name', '')

    try:
        Show.objects.filter(key=stream_key).update(last_off=timezone.now(), on_air=False)
    except Exception as err:
        logger.error(err)

    logger.info('Publish finished.')
    return HttpResponse('Show finished.')


