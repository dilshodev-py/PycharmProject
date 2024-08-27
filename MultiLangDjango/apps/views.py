from urllib.parse import urlparse

from django.http import HttpResponseRedirect
from django.urls import resolve, reverse
from django.utils import translation
from django.views.generic import ListView

from apps.models import Post


# Create your views here.


class HomePage(ListView):
    queryset = Post.objects.all()
    template_name = 'apps/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.language(self.request.COOKIES.get('language')).all()


def set_language_view(request):
    next = request.POST.get('next', request.GET.get('next'))
    lang_code = request.POST.get('language', None)
    next = urlparse(next).path
    current_language = translation.get_language_from_path(next)
    translation.activate(current_language)
    next_data = resolve(next)
    translation.activate(lang_code)
    next = reverse(next_data.view_name, args=next_data.args, kwargs=next_data.kwargs)
    response = HttpResponseRedirect(next)
    response.set_cookie('language', lang_code )
    return response


