from django import forms
# Models
from .models import Person


class PersonForm(forms.ModelForm):
    
    class Meta:
        model = Person
        fields = ("__all__")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    