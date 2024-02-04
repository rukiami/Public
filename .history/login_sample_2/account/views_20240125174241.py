# from django.shortcuts import render

# # Create your views here.

# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic import TemplateView

# from . import forms


# class TopView(TemplateView):
#     template_name = "account/top.html"

# class HomeView(TemplateView):
#     template_name = "account/home.html"

# class LoginView(LoginView):
#     """ログインページ"""
#     form_class = forms.LoginForm
#     template_name = "account/login.html"

# class LogoutView(LogoutView):
#     """ログアウトページ"""
#     template_name = "account/login.html"


# class SignUpView(TemplateView):   
#     """サインアップ""" 
#     template_name = "account/signup.html"

# from django.urls import reverse_lazy
# from django.views import generic
# from .forms import SignUpForm

# class SignUpView(generic.CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy('account:login')
#     template_name = 'account/signup.html'

from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from .forms import LoginForm, SignUpForm
from .models import Shop

class TopView(TemplateView):
    template_name = "account/top.html"

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "account/home.html"

class LoginView(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = "account/login.html"

class LogoutView(LogoutView):
    """ログアウトページ"""
    template_name = "account/login.html"

class SignUpView(CreateView):
    """サインアップ"""
    form_class = SignUpForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/signup.html'

class CalendarView(TemplateView):
    template_name = 'account/calendar.html'  # calendar.html テンプレートを使用する

class ShopListView(ListView):
    model = Shop
    template_name = 'account/shop_list.html'   

def search_view(request):
    # 検索機能の実装をここに書きます
    # この例では単純に search.html テンプレートをレンダリングします
    return render(request, 'account/search.html')


# views.py

# ...他のimport文...

# class CalendarView(LoginRequiredMixin, TemplateView):
#     template_name = 'account/calendar.html'

# ...他のビュークラス...

from django.views.generic import TemplateView

# ...他のビュークラス...

class CalendarView(TemplateView):
    template_name = 'account/calendar.html'  # calendar.html テンプレートを使用する

# ...他のビュークラス...
    
class ShopListView(ListView):
    model = Shop
    template_name = 'account/shop_list.html'

