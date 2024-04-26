from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


def init(self, *args, **kwargs):
    super(ContactForm, self).__init__(*args, **kwargs)
    for field_name, field in self.field.items():
        field.widget.atters['class'] = 'form-control'
        field.widget.atters['placeholder'] = field.label
