from django.conf.urls import url
from django.urls import path, include
from .views import (
    AlertListApiView, AlertDetailApiView, get_alerts, add_alert, delete, update
)

urlpatterns = [
    path('', AlertListApiView.as_view()),
    path('<int:alert_id>/', AlertDetailApiView.as_view()),
    path('mesAlertes/', get_alerts, name='alertes'),
    path('add_alert/', add_alert, name='add_alert'),
    path('delete/<int:alert_id>', delete, name='delete'),
    path('update/<int:alert_id>', update, name='update_alert')

]