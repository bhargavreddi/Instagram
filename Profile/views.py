import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http.response import  Http404
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView
from django import forms
from django.views.generic.list import ListView

from Profile.models import Image, Likes

@method_decorator(login_required, name='dispatch')
class Profile(CreateView):
    model = Image
    fields = ['image']

    def form_valid(self, form):
        form.instance.date = datetime.date.today()
        form.instance.time = datetime.datetime.now()
        form.instance.user = self.request.user
        return super(Profile, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        obj = Image.objects.all().filter(user = self.request.user).order_by("-id")
        context['images'] = obj
        context['user'] = self.request.user
        return context;

    def get_success_url(self):
        return reverse('profile')

@method_decorator(login_required, name='dispatch')
class ImageDeleteView(DeleteView):
    model = Image
    def get_success_url(self):
        return reverse("profile")

    def get_object(self, queryset=None):
        obj = Image.objects.get(id=self.kwargs.get('pk'))
        if obj.user != self.request.user:
            raise Http404
        # if obj.list.user != self.request.user:
        #     raise Http404
        return obj


@method_decorator(login_required, name='dispatch')
class ImageDetailView(DetailView):
    model = Image

    def get_context_data(self, **kwargs):
        context = super(ImageDetailView, self).get_context_data(**kwargs)
        like = Likes.objects.filter(user = self.request.user,image = context['image'])
        if(like.count()==0):
            context['liked'] = False
        else:
            context['liked'] = True

        context['likes'] = Likes.objects.all().filter(image = context['image']).count()
        return context

@method_decorator(login_required, name='dispatch')
class ProfileView(ListView):
    model = Image
    fields = ['image','date','user']
    template_name = 'profile.html'

    def get_queryset(self):
        try:
            user_id = self.kwargs.get('pk')
            user = User.objects.get(id =user_id)
        except Exception:
            raise Http404
        image = Image.objects.all().filter(user = user).order_by("-id")
        return image

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        user_id = self.kwargs.get('pk')
        user = User.objects.get(id=user_id)
        context['user'] = user
        return context


@method_decorator(login_required, name='dispatch')
class HomeView(ListView):
    model = Image
    fields = ['image','date','user']
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context=super(HomeView, self).get_context_data(**kwargs)
        context['object_list'] =  Image.objects.all().order_by("-id")
        return context


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)


class SignupView(FormView):
    template_name = 'register.html'
    form_class = UserCreateForm
    success_url = '/login/'

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.save()
        return super(SignupView, self).form_valid(form)

@method_decorator(login_required, name='dispatch')
class UserDetailView(ListView):
    model = User
    fields = ['id','username']
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context=super(UserDetailView, self).get_context_data(**kwargs)
        username = self.kwargs.get('pk')
        context['object_list'] =  User.objects.all().filter(username__contains=username)
        return context