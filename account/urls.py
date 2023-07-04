from django.urls import path
from .views import Register, Login, AddLink, login_t, home, update_view_count

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('addlink/', AddLink.as_view(), name='AddLink-list'),
    path('logint/', login_t, name='logint'),
    path('home/', home, name='home'),
    path('url_open/<int:pk>/', update_view_count, name='updateview')
]
