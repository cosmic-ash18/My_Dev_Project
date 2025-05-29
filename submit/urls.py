from django.urls import path
from . import views

app_name = 'submit'

urlpatterns = [
    path('<int:problem_id>', views.submit_code, name='submit_code'),
]
