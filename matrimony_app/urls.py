from django.contrib import admin
from django.urls import path,include
from matrimony_app import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),


    path('registration/',views.registration,name='registration'),
    path('login_view/',views.login_view,name='login_view'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('user_home/',views.user_home,name='user_home'),
    path('user_profiles/',views.user_profiles,name='user_profiles'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('approve_profile/<int:user_id>/', views.approve_profile, name='approve_profile'),
    path('reject_profile/<int:user_id>/', views.reject_profile, name='reject_profile'),
path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
path('search/',views.search,name='search'),
    path('create_payment/',views.create_payment,name='create_payment'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('search_results/',views.search_results,name='search_results'),
    path('all_users/',views.all_users,name='all_users'),
    path('search_id/',views.search_id,name='search_id'),
    path('search_id_admin/',views.search_id_admin,name='search_id_admin'),

    path('report_user/<int:user_id>/', views.report_user, name='report_user'),

   path('add_interest/<int:profile_id>/', views.add_interest, name='add_interest'),
    path('remove_interest/<int:profile_id>/', views.remove_interest, name='remove_interest'),
    
    path('subscription_list/',views.subscription_list,name='subscription_list'),
    path('subscription_list_admin/',views.subscription_list_admin,name='subscription_list_admin'),

  path('interested_profiles/', views.interested_profiles, name='interested_profiles'),
    path('edit_photos/', views.edit_photos, name='edit_photos'),
    path('view_report_profile/',views.view_report_profile,name='view_report_profile'),
    path('all_reports/', views.all_reports, name='all_reports'),
 path('change_password/', views.change_password, name='change_password'),
    path('send_message/<str:receiver_username>/', views.send_message, name='send_message'),
    path('show_messages/<str:receiver_username>/', views.show_messages, name='show_messages'),
]

    




