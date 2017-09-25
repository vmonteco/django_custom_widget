from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)
from .forms import PictureForm, ListForm
from .models import Picture, List

class PictureListView(ListView):
    model = Picture

class PictureCreateView(CreateView):
    model = Picture
    form_class = PictureForm

class PictureUpdateView(UpdateView):
    model = Picture
    form_class = PictureForm
    
class PictureDeleteView(DeleteView):
    model = Picture
    success_url = reverse_lazy('main:picture_list')
    
class PictureDetailView(DetailView):
    model = Picture

class ListListView(ListView):
    model = List

class ListCreateView(CreateView):
    model = List
    form_class = ListForm

class ListUpdateView(UpdateView):
    model = List
    form_class = ListForm

class ListDeleteView(DeleteView):
    model = List
    success_url = reverse_lazy('main:list_list')

class ListDetailView(DetailView):
    model = List
