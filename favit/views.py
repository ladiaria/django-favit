# -*- coding: utf-8 -*-
import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest

from .models import Favorite
from .utils import is_xhr


@login_required
def add_or_remove(request):

    if not is_xhr(request):
        return HttpResponseNotAllowed([])

    user = request.user

    try:
        app_model = request.POST["target_model"]
        obj_id = int(request.POST["target_object_id"])
    except (KeyError, ValueError):
        return HttpResponseBadRequest()

    fav = Favorite.objects.get_favorite(user, obj_id, model=app_model)

    if fav is None:
        Favorite.objects.create(user, obj_id, app_model)
        status = 'added'
    else:
        fav.delete()
        status = 'deleted'

    response = {
        'status': status,
        'fav_count': Favorite.objects.for_object(obj_id, app_model).count()
    }

    return HttpResponse(
        json.dumps(response, ensure_ascii=False),
        content_type='application/json'
    )


@login_required
def remove(request):

    if not is_xhr(request):
        return HttpResponseNotAllowed([])

    user = request.user

    try:
        app_model = request.POST["target_model"]
        obj_id = int(request.POST["target_object_id"])
    except (KeyError, ValueError):
        return HttpResponseBadRequest()

    Favorite.objects.get_favorite(user, obj_id, model=app_model).delete()
    status = 'deleted'

    response = {
        'status': status,
    }

    return HttpResponse(
        json.dumps(response, ensure_ascii=False),
        content_type='application/json'
    )
