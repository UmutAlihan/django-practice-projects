
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# more complex lookups such as using "OR" which is when it's time to turn to Q objects
from django.db.models import Q
from .models import City

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"

class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'
    # updating the queryset method of ListView and adding a hardcoded filter
    # so that only a city with the name of "Ankara" is returned
    #queryset = City.objects.filter(name__icontains='Ankara')

    # customize the queryset by overriding the get_queryset() method to change the list of cities returned
    def get_queryset(self):
        query = self.request.GET.get('q')
        #  built-in QuerySet methods of filter(), all(), get(), or exclude()
        #  docs: https://docs.djangoproject.com/en/3.1/ref/models/querysets/#queryset-api
        object_list = City.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list
