from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.translation import get_language, activate
from django.views.generic import TemplateView, ListView
from parler.utils import get_active_language_choices

from apps.models import MyModel


# Create your views here.
class HomePageView(ListView):
    template_name = 'apps/index.html'
    queryset = MyModel.objects.all()
    context_object_name = 'objects'

    def get_queryset(self):
        return self.queryset.language(self.request.COOKIES.get('lang_code', 'en')).all()

def set_language(request):
    lang_code = request.POST.get('language')
    if lang_code:
        activate(lang_code)
        request.session['LANGUAGE_SESSION_KEY'] = request.POST.get('language')
    response = HttpResponseRedirect(request.POST.get('next'))
    response.set_cookie('lang_code' , lang_code)
    return response