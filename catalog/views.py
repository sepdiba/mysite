from django.shortcuts import render

# Create your views here.
from catalog.models import Person, Gender, Education, Location

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_person = Person.objects.all().count()
    num_education = Education.objects.all().count()
    
   
    
    # The 'all()' is implied by default.    
    num_location = Location.objects.count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_person': num_person,
        'num_education': num_education,
        'num_location': num_location,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
from django.views import generic

class PersonListView(generic.ListView):
    model = Person
    paginate_by = 5

class PersonDetailView(generic.DetailView):
    model = Person

from django.contrib.auth.mixins import LoginRequiredMixin

class CreatedByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing persons created by user."""
    model = Person
    template_name ='catalog/person_list_user.html'
    paginate_by = 5
    
    def get_queryset(self):
        return Person.objects.filter(creater=self.request.user)

from django.views import generic

class LocationListView(generic.ListView):
    model = Location

class LocationDetailView(generic.DetailView):
    model = Location

class EducationListView(generic.ListView):
    model = Education

class EducationDetailView(generic.ListView):
    model = Education

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.models import Person

class PersonCreate(CreateView):
    model = Person
    fields = '__all__'
    initial = {'date_of_birth': '05/01/2018'}

class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_graduation', 'gender', 'location', 'education']

class PersonDelete(DeleteView):
    model = Person
    success_url = reverse_lazy('persons')

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.models import Location

class LocationCreate(CreateView):
    model = Location
    fields = '__all__'

class LocationUpdate(UpdateView):
    model = Location
    fields = '__all__'

class LocationDelete(DeleteView):
    model = Location
    success_url = reverse_lazy('locations')


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from catalog.models import Education

class EducationCreate(CreateView):
    model = Education
    fields = '__all__'

class EducationUpdate(UpdateView):
    model = Education
    fields = '__all__'

class EducationDelete(DeleteView):
    model = Education
    success_url = reverse_lazy('educations')