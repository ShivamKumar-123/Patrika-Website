from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    #path("", admin.site.urls),
    path("",views.home,name='home'),
    path("allCards/",views.allCards,name='allcard'),
    path('aboutus/', views.about, name='aboutUs'),
    path('newArrival/', views.newArrival, name='newArrival'),
    path('<int:card_id>/edit/',views.updateCard, name="card_edit"),
    path('<int:card_id>/delete/',views.deleteCard,name="card_delete"),
    path('updateNewArrival/<int:card_id>/', views.updateCardNewArrival, name='update_new_arrival'),

    path('deleteNewArrival/<int:card_id>/', views.deleteCardNewArrival, name='delete_new_arrival'),
    path('member/update/<int:member_id>/', views.updateMember, name='update_member'),
    path('member/delete/<int:member_id>/', views.deleteMember, name='delete_member'),




    path('signup/', views.signup_view, name='signup'),
    
    path('feedback/', views.FeedBackView.as_view(), name='feedback'),
    path('showFeedback/', views.feedBackShow, name='feedbackShow'),
    path('feedback/thankyou/', views.feedback_thankyou, name='feedback_thankyou'),
    path('feedback/update/<int:feedback_id>/', views.updateFeedback, name='update_feedback'),
    path('feedback/delete/<int:feedback_id>/', views.deleteFeedback, name='delete_feedback'),

    
    path("accounts/", include("django.contrib.auth.urls")),
    
] 
