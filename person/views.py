from django.shortcuts import render
from django.views.generic import CreateView
from .models import Person
from .forms import PersonCreateForm
from django.urls import reverse

# Create your views here.

class PersonCreateView(CreateView):
    model = Person
    template_name = 'form.html'
    form_class = PersonCreateForm
    
    def get_success_url(self):
        return reverse('person:person_create_view')

def index(request):
    print(request.POST)
    form = PersonCreateForm()
    return render(request, 'form.html', {"form":form})