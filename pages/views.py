from  django.urls import reverse_lazy
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import PageForm
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
# Create your views here.


class PageListView(ListView):
    model = Page
    template_name = 'pages/pages.html'


class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/page.html'


@method_decorator(staff_member_required, name='dispatch')
class CreatePageView(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')


@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
