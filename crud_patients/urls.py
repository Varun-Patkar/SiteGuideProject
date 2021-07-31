from django.urls import path
from . import views

app_name="crud_patients"
urlpatterns = [
    path("",views.IndexView.as_view(),name="index"),
    path("add/",views.AddView.as_view(),name="add"),
    path("patients/",views.PatientsView.as_view(),name="patients"),
    path("edit/<str:id>/",views.EditView.as_view(),name="edit"),
    path("delete/<str:id>/",views.Delete.as_view(),name="delete"),
    path("<slug:slug>/",views.SingleView.as_view(),name="single"),
]