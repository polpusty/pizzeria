from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^accounts/login/', views.login_user,
        name='login'),
    url(r'^accounts/register/', views.register_user,
        name='register'),
    url(r'^accounts/logout/', views.logout_user,
        name='logout'),
]
