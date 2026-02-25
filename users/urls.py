from django.urls import path
from .views import RegisterView, LoginView, ProfileView, EditInterestsView

urlpatterns = [
    path("register/", RegisterView.as_view(), name = 'register'),
    path("login/", LoginView.as_view(), name = 'home'),
    path("profile/", ProfileView.as_view(), name = "profile"),  
    path("interest/", EditInterestsView.as_view(), name = "interest")
    #path("print/", PrintVIew.as_view(), name = "print")
]

#