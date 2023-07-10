from django.shortcuts import render, redirect
from  . import models
from django.urls import reverse, reverse_lazy
from tweet_app.forms import AddTweetForm, AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

def list_tweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dictionary = {"tweets":all_tweets}
    return render(request, 'tweet_app/list_tweet.html', context=tweet_dictionary)

@login_required(login_url="/login")
def add_tweet(request):
    #print(request.POST)
    if request.POST:
        message = request.POST["message"]
        
        # tweet = models.Tweet(nickname,message)
        # tweet.save()

        models.Tweet.objects.create(username=request.user, message=message)
        return redirect(reverse('tweet_app:list_tweet'))
    else:
        return render(request, 'tweet_app/add_tweet.html')
    
def addtweetbyform(request):
    if request.method == "POST":
        form = AddTweetForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data["message_input"]
            models.Tweet.objects.create(username=request.user, message=message)
            return redirect(reverse('tweet_app:list_tweet'))
        else:
            print("Error in form!")
            return render(request,'tweet_app/addtweetbyform.html',context={"form":form}) 
    else:
        form = AddTweetForm
        return render(request,'tweet_app/addtweetbyform.html',context={"form":form})


def addtweetbymodelform(request):
    if request.method == "POST":
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname"]
            message = form.cleaned_data["message"]
            models.Tweet.objects.create(nickname=nickname, message=message)
            return redirect(reverse('tweet_app:list_tweet'))
        else:
            print("Error in form!")
            return render(request,'tweet_app/addtweetbymodelform.html',context={"form":form}) 
    else:
        form = AddTweetModelForm()
        return render(request,'tweet_app/addtweetbymodelform.html',context={"form":form})

@login_required
def delete_tweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect('tweet_app:list_tweet')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"