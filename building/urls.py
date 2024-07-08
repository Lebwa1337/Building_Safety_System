from django.urls import path

from building.views import index, user_login, user_signup, user_logout, entrance

urlpatterns = [
    path("", index, name="index"),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('entrance/<int:pk>/',entrance, name='entrance'),
]

app_name = 'building'
