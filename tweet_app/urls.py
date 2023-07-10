from django.urls import path
from . import views

app_name = "tweet_app"


urlpatterns = [
    path('', views.list_tweet, name="list_tweet"),          # www.atilsamancıoğlu.com/tweet_app
    path('add_tweet', views.add_tweet, name="add_tweet"),   # www.atilsamancıoğlu.com/tweet_app/add_tweet
    path('addtweetbyform', views.addtweetbyform, name='addtweetbyform'),
    path('addtweetbymodelform', views.addtweetbymodelform, name='addtweetbymodelform'),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('delete_tweet/<int:id>', views.delete_tweet, name="delete_tweet"),
]