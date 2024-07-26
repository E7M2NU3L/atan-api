from django.urls import path
from .views import ListPayments, CreatePayment, CancelPayment, SinglePayment

urlpatterns = [
    path('payments/', ListPayments.as_view(), name='list-payments'),
    path('payments/create/', CreatePayment.as_view(), name='create-payment'),
    path('payments/cancel/<int:pk>/', CancelPayment.as_view(), name='cancel-payment'),
    path('payments/<int:pk>/', SinglePayment.as_view(), name='single-payment'),
]
