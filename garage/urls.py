from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("booking/", views.booking, name="booking"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("thank-you/", views.thank_you, name="thank_you"),
]