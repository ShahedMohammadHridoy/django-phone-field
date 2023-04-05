from django import forms
from .models import Person
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class PersonForm(forms.ModelForm):
    phone = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial='BD')
    )

    class Meta:
        model = Person
        fields = "__all__"
