from django.urls import path
from feedbacks import views

urlpatterns = [
    path('send-forms', views.send_forms, name="receive-feeds"),
    path('recive-feedbacks', views.receive_feedbacks, name="receive-feeds")
]