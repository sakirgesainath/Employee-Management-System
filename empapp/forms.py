from django import forms
from empapp.models import Users

class UsersForm(forms.ModelForm):
    class Meta:
        model=Users
        fields=['id','name','Salary','designation','company_name','address','role','age','dob']

        widgets={
        'dob':forms.DateInput(
          attrs={'type':'date'}
        ),
    }
       
