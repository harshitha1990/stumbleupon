from django.shortcuts import render_to_response
from django.http import HttpResponse
from events.models import Link
from events.forms import AddForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def addView(request):
	if request.method=='POST':
		f=AddForm(request.POST)
		if f.is_valid():
			f.save()
			return HttpResponse("Succesfully inserted")
		else:
			return HttpResponse("Not inserted")
	else:
		f=AddForm()
		c={}
		c.update(csrf(request))
		c['addView']=f
		return render_to_response("addEvents.html",c)
		
def myLinks(request):
	links=Link.objects.all()
	return render_to_response("myLinksTemplate.html",{"links_list":links})
		

