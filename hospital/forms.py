from django import forms
from .models import *


class register_form(forms.Form, forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), min_length=6, label='Password', required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class register_form_detail_p(forms.ModelForm):

    class Meta:
        model = patient
        exclude = ('user', 'doc')


class register_form_detail_d(forms.ModelForm):

    class Meta:
        model = doctor
        exclude = ('user', )


class login_form(forms.Form):
    username = forms.CharField(label='Username', required=True)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=6, label='Password', required=True)


class appointment_form(forms.ModelForm):
    class Meta:
        model = appointment
        fields = '__all__'


class prescription_form(forms.ModelForm):
    class Meta:
        model = prescription
        exclude = ('doc', )


class payment_form(forms.ModelForm):
    class Meta:
        model = p_payment
        exclude = ('date', 'pat')


class contact_form(forms.Form):
    name = forms.CharField(label='Your Name', required=True, max_length=50)
    email = forms.EmailField(label='Your Email', required=True)
    subject = forms.CharField(label='Your Subject', required=True, max_length=100)
    message = forms.CharField(widget=forms.Textarea, label='Your Message', required=True)