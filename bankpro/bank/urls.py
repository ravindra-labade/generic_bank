from django.urls import path
from .views import Add_bank, List_bank, Detail_bank, Update_bank, Delete_bank

urlpatterns = [
    path('add/', Add_bank.as_view()),
    path('list/', List_bank.as_view()),
    path('detail/<int:pk>/', Detail_bank.as_view()),
    path('update/<int:pk>/', Update_bank.as_view()),
    path('delete/<int:pk>/', Delete_bank.as_view()),
]
