from django.forms import ModelForm
from .models import Task
from django.contrib.auth.models import User

class TaskAddForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'






