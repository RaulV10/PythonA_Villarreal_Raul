# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Titulo",
                "class": "form-control"
            }
        ))
    
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Descripción",
                "class": "form-control"
            }
        ))
    
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Lugar",
                "class": "form-control"
            }
        ))



class Meta:
    model = Request
    fields = ('title', 'description', 'location')
