from django.views.generic.edit import CreateView
from .models import Patient
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class IndexView(ListView):
    model = Patient
    template_name = 'crud_patients/index.html'
    context_object_name = "patients_list"


class SingleView(DetailView):
    model = Patient
    template_name = 'crud_patients/single.html'
    context_object_name = "patient"


class PatientsView(ListView):
    model = Patient
    template_name = "crud_patients/patients.html"
    context_object_name = "patient_list"


class AddView(CreateView):
    model = Patient
    template_name = "crud_patients/add.html"
    fields = ("fname", "lname", "gender", "age","disease",
              "doctor", "doctor_fees", "start_med")
    success_url = reverse_lazy("crud_patients:patients")


class EditView(UpdateView):
    model = Patient
    template_name = "crud_patients/edit.html"
    fields = ("fname", "lname", "gender", "age","disease",
              "doctor", "doctor_fees", "start_med")
    pk_url_kwarg = "id"
    success_url = reverse_lazy("crud_patients:patients")

class Delete(DeleteView):
    model=Patient
    pk_url_kwarg="id"
    success_url=reverse_lazy("crud_patients:patients")
    template_name="crud_patients/confirm-delete.html"