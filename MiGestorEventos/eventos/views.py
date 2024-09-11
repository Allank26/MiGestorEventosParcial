from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Organizador, Evento
from .forms import EventoForm

class OrganizadorListView(ListView):
    model = Organizador
    template_name = 'organizador_list.html'
    context_object_name = 'organizadores'

class OrganizadorCreateView(CreateView):
    model = Organizador
    template_name = 'organizador_form.html'
    fields = ['nombre', 'email']
    success_url = reverse_lazy('organizador_list')

class EventoCreateView(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = 'evento_form.html'
    success_url = reverse_lazy('evento_list')

@login_required(login_url='/accounts/login/')
def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'evento_form.html', {'form': form})

class EventoUpdateView(LoginRequiredMixin, UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'evento_form.html'
    success_url = reverse_lazy('evento_list')
    login_url = '/accounts/login/'

class EventoListView(ListView):
    model = Evento
    template_name = 'evento_list.html'
    context_object_name = 'eventos'

def home(request):
    return render(request, 'home.html')
