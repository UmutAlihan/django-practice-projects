from django.urls import path

from . import views

urlpatterns = [
    path("", views.AllTestsView.as_view(), name="tests-page"),
]