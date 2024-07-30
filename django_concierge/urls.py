from django.urls import path

from django_concierge import views

urlpatterns = [
    path("ajax/", views.ajax_recive_client_intel, name="concierge_ajax_endpoint"),
]
