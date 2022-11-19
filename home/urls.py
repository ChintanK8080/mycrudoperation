from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = "Admin Control Panel"
admin.site.site_title = "Admin Control Panel"
admin.site.index_title = "Welcome"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('login', views.login, name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('users', views.users, name = 'users'),


]
