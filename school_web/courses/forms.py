from .models import Queries
from django.forms import ModelForm

class QueriesForm(ModelForm):
    class Meta:
        model = Queries
        fields = ['fio', 'phone_number', 'type_of_learning', 'math_learn', 'physics_learn']
