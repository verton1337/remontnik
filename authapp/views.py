
from django.shortcuts import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import ModelFormMixin
from authapp.forms import LoginForm
from django.urls import reverse_lazy
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.


class LoginView(LoginView):
    template_name = "authapp/index.html"
    success_url = reverse_lazy('order:orders_list')

    def get_context_data(self, **kwargs):
        data =  super(LoginView, self).get_context_data(**kwargs)
        form = LoginForm(data=self.request.POST)
        if self.request.POST and form.is_valid():
            
            username = self.request.POST['username']
            password = self.request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(self.request, user)
                return HttpResponseRedirect(reverse('main'))
            else:
                return HttpResponseRedirect(reverse('auth'))
            
        else:
            data["form"] = LoginForm()

        
        return data

    def get_success_url(self):
        return reverse('order:orders_list')


class LogoutView(LogoutView):
    template_name = "authapp/index.html"

    def get_context_data(self, **kwargs):
        data = super(LogoutView, self).get_context_data(**kwargs)
        data["form"] = LoginForm(data=self.request.POST)

        return data



