from django.conf.urls import url
from django.urls import path, include
from .views import (
    AlertListApiView, AlertDetailApiView, get_alerts
)

urlpatterns = [
    path('', AlertListApiView.as_view()),
    path('<int:alert_id>/', AlertDetailApiView.as_view()),
    path('mesAlertes', get_alerts, name='alertes')
]