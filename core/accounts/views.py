from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm  
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect
# Create your views here.

class UserLogin(LoginView):
    
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('task_list') 
    
    # def form_invalid(self, form):
    #     messages.error(self.request,'Invalid username or password')
    #     return self.render_to_response(self.get_context_data(form=form))
    
class UserRegister(FormView):
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('task_list')
    template_name = 'registration/register.html'
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(UserRegister, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("task_list")
        return super(UserRegister, self).get(*args, **kwargs)
    


    
