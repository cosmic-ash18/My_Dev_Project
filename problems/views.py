from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from .models import Problem
from .forms import UserRegisterForm

# Create your views here.

# Registration View
def register(request):
    if request.user.is_authenticated:
        return redirect('problems:list')
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


# Problems list view
class ProblemListView(ListView):
    model = Problem
    template_name = 'problems_list.html'
    context_object_name = 'problems'


# Problem detail view
class ProblemDetailView(DetailView):
    model = Problem
    template_name = 'problem_detail.html'


from django.shortcuts import render

def register_view(request):
    return render(request, "problems/register.html")

def login_view(request):
    return render(request, "problems/login.html")

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        # if already logged in, skip the form and go straight to list
        if request.user.is_authenticated:
            return redirect('problems:list')
        return super().dispatch(request, *args, **kwargs)