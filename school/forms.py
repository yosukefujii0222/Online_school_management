from django import forms
from .models import Customer
from .models import Lesson_history

class CustomerForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ('name', 'gender', 'age')

class LessonHistoryForm(forms.ModelForm):
  class Meta:
    model = Lesson_history
    fields = ('customer', 'lesson', 'date' , 'hour')
