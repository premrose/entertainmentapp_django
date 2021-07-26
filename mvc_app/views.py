from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Media, Favourite


def sign_up(request):
    """ sign up view"""
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            response = redirect('/accounts/login/')
            return response
        if not form.is_valid():
            context['details'] = 'Details something wrong in the form. Please Enter again'
    context['form']=form
    return render(request,'registration/sign_up.html',context)


@login_required
def audio(request):
    """ audio view for audio details"""
    queryset = Media.objects.all().filter(Media_type='Audio')
    return render(request, 'audios.html' , {'audio': queryset})


@login_required
def video(request):
    """video view for video details"""
    queryset = Media.objects.all().filter(Media_type='Video')
    return render(request, 'videos.html' , {'video': queryset})


def favourite_get(request, Media_id):
    """endpoint for get liked or not"""
    user = request.user
    queryset = Favourite.objects.all().filter(user=user, Media_id=Media_id)
    if len(queryset) == 0:
        isfavourite=False
    elif len(queryset) == 1:
        isfavourite=True
    else:
        isfavourite="Something went wrong in isfavourite"
    popularity = Favourite.objects.all().filter(Media_id='%s' % Media_id).count()
    context = {
        'isfavourite': isfavourite,
        'popularity': popularity,
    }
    return render(request, 'favourite_get.html', context)


def favourite_post(request):
    """endpoint for post like"""
    user = request.user
    a = Media.objects.get(Media_id=request.GET.get("Media_id",""))
    f = Favourite(user=user, Media_id=a)
    if f.Media_id in Favourite.objects.all():
        return HttpResponse("That like is already exists")
    f.save()
    return HttpResponse('created Successfully')


def favourite_delete(request):
    """endpoint for delete favourite"""
    user = request.user
    Favourite.objects.filter(user=user, Media_id = request.GET.get("Media_id","")).delete()
    return HttpResponse("Deleted Successfully")
