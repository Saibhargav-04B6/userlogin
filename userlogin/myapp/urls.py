from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.createproduct,name='createproduct'),
    path('home',views.home,name='home'),
    # path('accounts/',include('django.contrib.auth.urls')),
    # path('signup/',views.authview,name='auth_view'),
    # path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
]