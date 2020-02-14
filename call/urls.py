from django.urls import path
from call import views

urlpatterns = [
    path('answer/', views.answer_call),
]
