from django.urls import path
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'web'

urlpatterns = [
    path('buyersignup/', views.buyer_signup_view, name='buyer_signup'), 
    path('sellersignup/', views.seller_signup_view, name='seller_signup'),
    path('login/', views.login_view , name='login'), 
    path('loggedin/', views.login_index , name='login_index'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name="home"),
    path('options/', views.signup_options,name="signup_options"),
    path('myprofile/',views.my_profile,name="my_profile"),
    path('myprofile/edit/',views.edit_profile,name="edit_profile"),
    path('myprofile/password/',views.change_password,name="change_password"),
    path('search/',include('haystack.urls')),
    path('create/',views.product_create_view,name='product_create_view'),
    path('product/(?P<pk>\d+)/',views.product,name="product"),
    path('product/edit/(?P<pk>\d+)/',views.edit_details,name="edit_details"),
    path('wishlist/',views.view_wishlist,name="wishlist"),
    path('add-wishlist/(?P<pk>\d+)/',views.add_to_wishlist,name="add-wishlist"),
    path('remove-wishlist/(?P<pk>\d+)/',views.remove_wishlist,name="remove-wishlist"),
    path('search_product/(?P<pk>\d+)/',views.search_product, name="search_product"),
    path('password-reset/',auth_views.PasswordResetView.as_view(
        template_name='web/password_reset.html',
        email_template_name='web/reset_password_email.html'),
        name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(
        template_name='web/password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
        template_name='web/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(
        template_name='web/password_reset_complete.html'),
        name='password_reset_complete'),
    #path('product_in_cat/(?P<pk>\d+)/',views.product_in_category, name="product_in_category"),
]