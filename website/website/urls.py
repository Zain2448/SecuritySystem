"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from userApp import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.Home.as_view(), name='home'),
    path('',include("django.contrib.auth.urls")),
    path("motion/", user_views.motion_status),
    path('live', user_views.live_page, name='live'),
    path('notifications/', user_views.notifications_page, name='notifications'),

    path('logs/', user_views.smoke_log, name='log_view'),
    path('motion-logs/', user_views.motion_log_view, name='motion_logs'),

]
