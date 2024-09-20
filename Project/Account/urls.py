from django.urls import path,include
from . import views
urlpatterns = [
    path('login/',views.Login,name="Login"),
    path('logout/',views.Logout,name="Logout"),
    path('signup/',views.SignUp,name="SignUp"),
    path('profile/',views.Profile,name="Profile"),
    path('profile/changepass',views.ChangePass,name="ChangePass"),
    path('profile/changepasswooldpass',views.ChangePassWOOldPass,name="ChangePassWOOldPass"),
]