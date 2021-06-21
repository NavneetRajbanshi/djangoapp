from django.db.models import fields
from django.db.models.fields import Field
from  django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'