from django.urls import path
# . means import from the same directory this urls.py file is in
from . import views

app_name = 'submit'

urlpatterns = [
    path('<int:problem_id>', views.submit_code, name='submit_code'),
    path('<int:problem_id>/suggest/', views.suggest_improvements, name='suggest_improvements'),
]
