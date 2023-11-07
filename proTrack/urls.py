from django.urls import path

import proTrack
from . import views

app_name = 'proTrack'

urlpatterns = [
    # path('', views.home, name='home'),
    path('', proTrack.views.login_view, name='login'), # en ves de un home, directamente va al login
    path('dashboard/', proTrack.views.dashboard, name='dashboard'),
]
