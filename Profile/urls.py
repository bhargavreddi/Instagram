from django.conf.urls import url, include

from Profile import views

urlpatterns = [
    url(r'^signup/$',views.SignupView.as_view(),name='register'),
    url(r'^$',views.HomeView.as_view(),name='home'),
    url(r'^profile/$',views.Profile.as_view(),name='profile'),
    url(r'^profile/(?P<pk>[0-9]+)/$',views.ProfileView.as_view(),name='profile_id'),
    url(r'^profile/delete/(?P<pk>[0-9]+)/$',views.ImageDeleteView.as_view(),name='delete_image'),
    url(r'^image/(?P<pk>[0-9]+)/$',views.ImageDetailView.as_view(),name='image_view'),
    url(r'^search/(?P<pk>[A-Za-z]+)/$',views.UserDetailView.as_view(),name='search_view'),
]