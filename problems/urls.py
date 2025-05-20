from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ProblemListView, ProblemDetailView

app_name = 'problems'

urlpatterns = [
    # Wrap the class-based views with login_required here
    path('', login_required(ProblemListView.as_view()), name='list'),
    path('problem/<int:pk>/', login_required(ProblemDetailView.as_view()), name='detail'),
]