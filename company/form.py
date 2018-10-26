from django import forms

class CompanyForm(forms.Form):
    company_name = forms.CharField(max_length=10)

class CompanyPVForm(forms.Form):
    company_id = forms.CharField(max_length=200)
    # parking_id = forms.CharField(max_length=100)