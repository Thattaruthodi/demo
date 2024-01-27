from django import forms
from .models import student_details

class Dataform(forms.ModelForm):
     class Meta:
          model = student_details
          fields = "__all__"