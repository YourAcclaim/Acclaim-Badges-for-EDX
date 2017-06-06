from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import JsonResponse

from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from acclaim_badges.models import BadgeCourse
from acclaim_badges.models import AcclaimToken
from django.contrib.auth.decorators import user_passes_test
from django.forms import ModelForm
from .forms import AcclaimTokenForm
from .forms import BadgeCourseForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

# badge course list controllers
class BadgeCourseDelete(DeleteView):
    model = BadgeCourse
    success_url = reverse_lazy('badge-courses')

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/admin/login'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteView, self).dispatch(*args, **kwargs)

class BadgeCourseList(ListView):
    model = BadgeCourse

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/admin/login'))
    def dispatch(self, *args, **kwargs):
        return super(ListView, self).dispatch(*args, **kwargs)

class BadgeCourseCreate(CreateView):
    model = BadgeCourse
    form_class = BadgeCourseForm

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/admin/login'))
    def dispatch(self, *args, **kwargs):
        return super(CreateView, self).dispatch(*args, **kwargs)

class BadgeCourseUpdate(UpdateView):
    model = BadgeCourse
    form_class = BadgeCourseForm
    success_url = reverse_lazy('badge-courses')

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/admin/login'))
    def dispatch(self, *args, **kwargs):
        return super(UpdateView, self).dispatch(*args, **kwargs)

# acclaim token controllers
class AcclaimTokenList(ListView):
    model = AcclaimToken

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/admin/login'))
    def dispatch(self, *args, **kwargs):
        return super(ListView, self).dispatch(*args, **kwargs)

class AcclaimTokenCreate(CreateView):
    model = AcclaimToken
    fields = ['auth_token', 'organization_id', 'url']

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/admin/login'))
    def dispatch(self, *args, **kwargs):
        return super(CreateView, self).dispatch(*args, **kwargs)

class AcclaimTokenDelete(DeleteView):
    model = AcclaimToken
    success_url = reverse_lazy('acclaim-tokens')

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/admin/login'))
    def dispatch(self, *args, **kwargs):
        return super(DeleteView, self).dispatch(*args, **kwargs)

class AcclaimTokenUpdate(UpdateView):
    model = AcclaimToken
    form_class = AcclaimTokenForm
    initial = {'auth_token': ''}
    success_url = reverse_lazy('acclaim-tokens')

    @method_decorator(user_passes_test(lambda u: u.is_superuser, login_url='/admin/login'))
    def dispatch(self, *args, **kwargs):
        return super(UpdateView, self).dispatch(*args, **kwargs)
