from django.conf.urls import include, url
from . import views

urlpatterns = [
  url(r'^$', views.lesson_list, name='lesson_list'),
  url(r'^customer$', views.customer_list, name='customer_list'),
  url(r'^lesson_history$', views.lesson_history, name='lesson_history'),
  url(r'^monthly_report$', views.monthly_report, name='monthly_report'),
  url(r'^report$', views.report, name='report'),
  url(r'^new_customer$', views.new_customer, name='new_customer'),
  url(r'^customer/(?P<pk>[0-9]+)/edit/$', views.customer_edit, name='customer_edit'),
  url(r'^lesson_history$', views.lesson_history, name='lesson_history'),
  url(r'^new_lesson_history$', views.new_lesson_history, name='new_lesson_history'),
  url(r'^lesson_history/(?P<pk>[0-9]+)/edit/$', views.lesson_history_edit, name='lesson_history_edit'),

]
