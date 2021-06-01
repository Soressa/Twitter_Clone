from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tweets
from .forms import TweetForm
from datetime import datetime
from cloudinary.forms import cl_init_js_callbacks


# Create your views here


def index(request):
    # If the method is POST 
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        # If the form is valid
        if form.is_valid():
            # Yes, Save
            form.save()

            # Redirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show Error
            return HttpResponseRedirect(form.errors.as_json())

    # Get all the tweets
    tweets = Tweets.objects.all()

    # Show
    return render(request, 'tweets.html', {'tweets': tweets})

# /// DELETE

def delete(request, tweets_id):
    # find post
    tweets = Tweets.objects.get(id=tweets_id)
    tweets.delete()
    return HttpResponse('/')

# /// UPDATE

def update(request, tweets_id):
    tweets = Tweets.objects.get(id=tweets_id)
    form = TweetForm(instance=tweets)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance = tweets)
        if form.is_valid():
            form.save()
            # Redirect to home
            return HttpResponseRedirect('/')
            # Show 
    return render(request, 'update.html',{'form':form})