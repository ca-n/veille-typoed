from django.shortcuts import get_object_or_404
from django.views import generic

from tests.models import Test
from users.models import User

# Create your views here.

class HighscoreList(generic.ListView):
    queryset = Test.objects.order_by("wpm")
    paginate_by = 10
    context_object_name = "test_list"
    template_name = "tests/highscores.html"
    