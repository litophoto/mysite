from django.shortcuts import render
from django.views import generic

from .models import WallPaper

class List(generic.ListView):
    template_name = 'piplup/list.html'
    #model = WallPaper

    def get_queryset(self):
        search_text = self.request.GET.get('query')
        if search_text:
            return WallPaper.objects.filter(text__icontains=search_text)
        else:
            return WallPaper.objects.all()


class Detail(generic.DeleteView):
    template_name = 'piplup/detail.html'
    model = WallPaper