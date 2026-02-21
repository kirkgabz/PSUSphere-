from django.views.generic import ListView
from .models import Organization

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"