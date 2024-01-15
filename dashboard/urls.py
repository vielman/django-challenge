from django.urls import path
from dashboard import views

urlpatterns = [
    path('view/', views.DashboardView.as_view()),
    
]