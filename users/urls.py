from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views


app_name = 'users'

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name= 'users/login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'users/logout.html'), name= 'logout'),
    path('list-of-members/', user_views.list_of_members, name= 'list_of_members'),
    path('list-of-members-exco/', user_views.list_of_members_exco, name= 'list_of_members_exco'),
    path('list-of-members-nonexco/', user_views.list_of_members_nonexco, name= 'list_of_members_nonexco'),
    path('list-of-members-passedout/', user_views.list_of_members_passedout, name= 'list_of_members_passedout'),
    path('register/', user_views.register, name= 'register'),
    path('view-profile/', user_views.view_profile, name= 'view_profile'),
    path('user-profile/<int:pk>/', user_views.users_profile, name= 'users_profile'),
    path('edit-profile/', user_views.edit_profile, name= 'edit_profile'),
    path('change-password/', user_views.change_password, name='change_password')

]