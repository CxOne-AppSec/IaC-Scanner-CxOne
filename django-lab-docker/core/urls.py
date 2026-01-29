from django.urls import path
from .views import form_page, submit_form

urlpatterns = [
    path("", form_page, name="form"),
    path("submit/", submit_form, name="submit"),
]
