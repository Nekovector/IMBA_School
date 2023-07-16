from .models import Queries1, Queries2, Queries3
from django.forms import ModelForm


class Queries1Form(ModelForm):
    class Meta:
        model = Queries1
        fields = ['surname', 'name', 'patronymic', 'phone_number', 'type_of_learning', 'math_learn', 'physics_learn']


class Queries2Form(ModelForm):
    class Meta:
        model = Queries2
        fields = ['surname', 'name', 'patronymic', 'phone_number', 'type_of_learning', 'math_learn']


class Queries3Form(ModelForm):
    class Meta:
        model = Queries3
        fields = ['surname', 'name', 'patronymic', 'phone_number', 'grade_number', 'type_of_learning', 'physics_learn',
                  'math_learn']
