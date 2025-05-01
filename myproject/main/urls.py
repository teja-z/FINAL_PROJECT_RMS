from django.urls import path
from . import views
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('dairy/', views.dairy, name='dairy'),
    path('cold_drink/', views.cold_drink, name='cold_drink'),
    path('snacks/', views.snacks, name='snacks'),
    path('instant_food/', views.instant_food, name='instant_food'),
    path('sweet/', views.sweet, name='sweet'),
    path('bakery/', views.bakery, name='bakery'),
    path('tea_coffee/', views.tea_coffee, name='tea_coffee'),
    path('atta_rice_dal/', views.atta_rice_dal, name='atta_rice_dal'),
    path('masala_oil/', views.masala_oil, name='masala_oil'),
    path('sauce_spread/', views.sauce_spread, name='sauce_spread'),
    path('baby_care/', views.baby_care, name='baby_care'),
    path('pharma_wellness/', views.pharma_wellness, name='pharma_wellness'),
    path('cleaning_essentials/', views.cleaning_essentials, name='cleaning_essentials'),
    path('personal_care/', views.personal_care, name='personal_care'),
    path('love_corner/', views.love_corner, name='love_corner'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
]
