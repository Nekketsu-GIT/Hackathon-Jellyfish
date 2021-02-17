from django.conf.urls import url
from django.urls import path, include
from .views import (
    AlertListApiView, AlertDetailApiView
)

urlpatterns = [
    path('', AlertListApiView.as_view()),
    path('<int:alert_id>/', AlertDetailApiView.as_view()),
]