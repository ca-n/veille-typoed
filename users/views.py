from django.views import generic

from users.models import User

# Create your views here.

"""
| users | `/users/login` | POST |
| users | `/users/logout` | POST |
| users | `/users` | POST |
| users | `/users/{id}` | GET, PATCH, DELETE |
| users | `/users/{id}/tests` | GET |
"""

class UserCreate(generic.CreateView):
    model = User

class UserDetail(generic.DetailView):
    model = User

class UserUpdate(generic.UpdateView):
    model = User

class UserDelete(generic.DeleteView):
    model = User