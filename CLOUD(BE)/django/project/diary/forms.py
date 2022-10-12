from django import forms
from diary.models import diary


class DiaryForm(forms.ModelForm):
    class Meta:
        model = diary
        fields = ['title', 'content']