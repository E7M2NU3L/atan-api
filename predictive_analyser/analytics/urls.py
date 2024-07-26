from django.urls import path
from analytics import views

urlpatterns = [
    path('analyse_customers', views.analyse_customers, name="analyse-customers"),
    path('analyse_stocks', views.analyse_stock, name="analyse_stocks")
]