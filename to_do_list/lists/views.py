# from django.shortcuts import render
# from django.views.generic.edit import FormView
from rest_framework import viewsets

# from lists.forms import ListForm
from lists.models import List
from lists.serializers import ListSerializer


# def home_page(request):
#     return render(request, 'home.html')

# class ListView(FormView):
#     form_class = ListForm
#     template_name = 'home.html'
#     success_url = '/'


class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
