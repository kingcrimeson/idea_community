
from django.contrib import admin
from django.urls import path
from django.urls import include
import LOGIN.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',LOGIN.views.login),

]
