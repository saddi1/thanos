import datetime

from django import forms
from .models import Student


class CreatestudentForm(forms.ModelForm):
    dob = forms.DateField(
        label="Your Birth Date",
        widget=forms.SelectDateWidget(years=range(2000, datetime.date.today().year - 10))
    )

    class Meta:
        model = Student
        fields = "__all__"
        exclude = ['id']
