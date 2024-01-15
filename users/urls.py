from django.urls import path
from users import views

urlpatterns = [
    path('list/', views.ListUserView.as_view()),
    path('create/', views.CreateUserView.as_view()),
    path('login/', views.CreateTokenView.as_view()),
    path('logout/', views.Logout.as_view()),
    path('user/', views.RetreiveUpdateUserView.as_view()),
]