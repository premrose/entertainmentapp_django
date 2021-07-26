from django.urls import path, include

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/sign_up/',views.sign_up,name="sign-up"),
    path('audio/', views.audio, name='audio'),
    path('video/', views.video, name='video'),
    path('favourite_get/<str:Media_id>/', views.favourite_get, name='favourite_post'),
    path('favourite_post/', views.favourite_post, name='favourite_post'),
    path('favourite_delete/', views.favourite_delete, name='favourite_delete'),
]
