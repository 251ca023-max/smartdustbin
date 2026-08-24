from django.urls import path
from .views import dashboard, receive_sensor_data

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("api/sensor-data/", receive_sensor_data, name="receive_sensor_data"),
]