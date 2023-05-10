from django.urls import path
from favit.views import *


urlpatterns = [
    path('add-or-remove/', add_or_remove, name='favit.views.add_or_remove'),
    path('remove/', remove, name='favit.views.remove'),
]
