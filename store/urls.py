from django.urls import path
from store import views
from .views import index,signup
urlpatterns=[
    path('',index),
    path('signup',views.signup,name='signup')
]