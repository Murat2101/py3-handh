from django import forms
from .models import Resume


class ResumeEditForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['text',
                  'summary',
                  'skills',
                  'worker',
                  'profile_photo'
                  ]


class ResumeAddForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['text',
                  'summary',
                  'skills',
                  'worker'
                  ]


