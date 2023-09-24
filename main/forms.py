from django.forms import ModelForm
from .models import *

class AnswerForm(ModelForm):
    class Meta:
        model=Answer
        fields=('details',)

class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields=('title','details','tags')

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name' , 'email', 'bio']