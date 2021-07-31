from django.db import models
import uuid
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Patient(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('nonbinary', 'Non Binary'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fname = models.CharField(max_length=200,verbose_name="First Name")
    lname = models.CharField(max_length=200,verbose_name="Last Name")
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES,verbose_name="Gender")
    age = models.IntegerField(default=0,verbose_name="Age")
    disease = models.CharField(max_length=200,verbose_name="Disease")
    doctor = models.CharField(max_length=200,verbose_name="Doctor Name")
    doctor_fees = models.FloatField(default=500.00,verbose_name="Doctor Fees(Rs.)")
    start_med = models.DateTimeField(verbose_name="Date of start of medications")
    slug = models.SlugField(max_length=100, unique=True)
    updated = models.DateField(auto_now=True)

    def save(self, **kwargs):
        if not self.slug:
            self.slug=slugify(self.fname+self.lname)
        super(Patient, self).save()

    def get_absolute_url(self):
        return reverse("crud_patients:single", args=[self.slug])
    
    def get_full_name(self):
        return self.fname+" "+self.lname

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return (self.fname+" "+self.lname)
