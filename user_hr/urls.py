from django.urls import path, include
from .views import dashboard, register, logout_view
urlpatterns = [
    path('',dashboard,name="dashboard"),
    path('accounts/', include('django.contrib.auth.urls')), # new
    path('register/', register, name="register"),
    path('logout/', logout_view, name="logout"),
]