from django.shortcuts import render_to_response
from django.template import RequestContext
from cal.models import Event
#from forms import EventForm

def index(request):
    """
    Events of the coming months sorted in to a list for each month
    """

    return render_to_response('cal/index.html', {
        'event_list': Event.future.all(),
        #'form': EventForm()
    }, context_instance=RequestContext(request))
