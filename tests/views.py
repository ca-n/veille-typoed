from django.views import generic
from wordfreq import random_ascii_words

from tests.models import Test

# Create your views here.

class HighscoreList(generic.ListView):
    queryset = Test.objects.order_by("-wpm")
    template_name = "tests/highscores.html"
    
class TakeTest(generic.TemplateView):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    template_name = "tests/take_test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        word_list = list(filter(lambda word: not word.isnumeric(), random_ascii_words(nwords=150, bits_per_word=8).split(' ')))
        context['word_list'] =  word_list
        return context
    
class SubmitTest(generic.CreateView):
    model = Test