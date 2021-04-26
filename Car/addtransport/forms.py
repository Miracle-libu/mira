from .models import Transport
from django.forms import ModelForm

class TransportAddForm(ModelForm):
    class Meta:
        model = Transport
        fields = '__all__'