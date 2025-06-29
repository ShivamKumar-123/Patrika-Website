from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #path("", admin.site.urls),
    path("",views.home,name='home'),
    path("allCards/",views.allCards,name='allcard'),
    path('aboutus/', views.about, name='aboutUs'),
    path('newArrival/', views.newArrival, name='newArrival'),
    path('signup/', views.signup_view, name='signup'),
    
    path('feedback/', views.FeedBackView.as_view(), name='feedback'),
    path('showFeedback/', views.feedBackShow, name='feedbackShow'),
    
    
    
    path("accounts/", include("django.contrib.auth.urls")),
] 
