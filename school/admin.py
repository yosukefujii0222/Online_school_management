from django.contrib import admin
from .models import Lesson, Customer, Lesson_history

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Customer)
admin.site.register(Lesson_history)

