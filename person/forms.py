from django import forms
from .models import Person


class PersonCreateForm(forms.ModelForm):
    def __init__(self, request=None, *args, **kwargs):
        super(PersonCreateForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control col-12'
            self.fields['name'].widget.attrs['placeholder'] = 'name'
            self.fields['cell'].widget.attrs['placeholder'] = 'cell'
            self.fields['road'].widget.attrs['placeholder'] = 'road'
            self.fields['house_number'].widget.attrs['placeholder'] = 'house number'

    class Meta:
        model = Person
        fields = ['name', 'cell', 'road', 'house_number'] 

        widgets = {
            'name': forms.TextInput(attrs={'id': 'check_field_name'}),        
            'cell': forms.TextInput(attrs={'id': 'check_field_cell'}),        
            'road': forms.TextInput(attrs={'id': 'check_field_road'}),
            'house_number': forms.TextInput(attrs={'id': 'check_field_house_number'}),
        }