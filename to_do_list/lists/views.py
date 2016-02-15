from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response

from lists.forms import UploadFileForm
from lists.models import UploadFile


def home_page(request):
    return render(request, 'home.html')


def drop(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            new_file = UploadFile(file=request.FILES['file'])
            new_file.save()
            return HttpResponseRedirect(reverse('lists:drop'))
    else:
        form = UploadFileForm()
        data = {'form': form}
        return render_to_response('drop.html', data, context_instance=RequestContext(request))