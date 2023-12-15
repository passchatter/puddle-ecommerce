from django.urls import path
from .views import index, contact, signup
from django.contrib.auth import views

from .forms import LoginForm

urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
    path('signup/', signup, name="signup"),
    path('login/', views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name="login")
]