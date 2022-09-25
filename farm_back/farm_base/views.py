from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from farm_base.api.v1.views import owner
from .models import Farm, Owner
from django.db.models import Q

class searchView(TemplateView):
    template_name = 'farm_base/search.html'

class resultsView(ListView):
    model = Farm
    template_name = 'farm_base/results.html'

    def get_queryset(self):
        q = self.request.GET.get("q")
        object_list = Farm.objects.filter(
            Q(owner__name__icontains=q) | Q(owner__document__icontains=q) | Q(name__icontains=q) | 
            Q(municipality__icontains=q) | Q(state__icontains=q) | Q(id__icontains=q)  
        )
        return object_list

class detailsView(TemplateView):
    template_name = 'farm_base/details.html'
    
    def get(self, request, farm_id):
        farm = Farm.objects.get(pk=farm_id)
        return render(request, self.template_name, {'farm': farm})
    
