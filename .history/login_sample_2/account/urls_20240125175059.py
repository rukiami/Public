from django.urls import path
from .views import (
    TopView,
    HomeView,
    LoginView,
    LogoutView,
    SignUpView,
    CalendarView,
    ShopListView,
    Search_view,
)


app_name="account"
urlpatterns = [
    path("", TopView.as_view(), name="top"),
    path("home/", HomeView.as_view(), name="home"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('shop_list/', ShopListView.as_view(), name='shop_list'),
    path('search/', Search_view, name='search'),  # search の URL パターンを追加
    # ...他にも必要なURLパターンがあれば追加...
]  

# account/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from . views import TopView, CalendarView, LoginView, SignUpView, HomeView, ShopListView
  # CalendarViewをimport

app_name = 'account'  # アプリケーションの名前空間を設定

urlpatterns = [
    # 他のURLパターン
    path('', TopView.as_view(), name='top'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('login/', LoginView.as_view(), name='login'),  # ログインページ
    path('signup/', SignUpView.as_view(), name='signup'),  # サインアップページ
    path('home/', HomeView.as_view(), name='home'),  # ホームページ
    path('logout/', LogoutView.as_view(), name='logout'), 
    path('shop_list/', ShopListView.as_view(), name='shop_list'),  # 店舗一覧ページ
     # ログアウトペー
    # ...他にも必要なURLパターンがあればここに追加...
]
