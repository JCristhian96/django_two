from django.views.generic import ListView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
# Models
from .models import Person
# Forms
from .forms import PersonForm


class PersonListView(ListView):
    model = Person
    template_name = "core/list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Listado de Personas"
        return context


class PersonCreateView(CreateView):
    form_class = PersonForm
    model = Person
    template_name = "core/form.html"
    success_url = reverse_lazy('core:list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Añadir Persona"
        return context


class PersonUpdateView(UpdateView):
    form_class = PersonForm
    model = Person
    template_name = "core/form.html"
    success_url = reverse_lazy('core:list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar Persona"
        return context
    
    
class PersonDeleteView(View):
    success_url = reverse_lazy('core:list')
    
    def get(self, request, *args, **kwargs):
        person = get_object_or_404(Person, pk=kwargs.get('pk'))
        person.delete()
        return redirect(self.success_url)
    