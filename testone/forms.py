from django import forms
from .models import Todo


class TodoCreatForm(forms.Form):
    title = forms.CharField()
    # description = forms.CharField(widget=forms.Textarea)
    description = forms.CharField()
    create = forms.DateTimeField()
    completed = forms.BooleanField()


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'create', 'completed']  # or __all__
