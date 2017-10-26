from django import forms

from .models import Users
from django.db import models


class DetailForm(forms.Form):
	class Meta:
		model = Users
        fields = ('name', 'model', 'imei', 'imei1' , 'mob_no')

		
    