from django.shortcuts import render_to_response
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth import authenticate,login

# Create your views here.
def signinForm(request):
	if request.method=='POST':
		form=AuthenticationForm(request.POST)
		if form.is_valid:
			formValues=request.POST.values()
			#form=AuthenticationForm(data=request.POST)
			user=authenticate(username=formValues[0],password=formValues[2])
			if user is not None:
				if user.is_active:
					login(request,user)
				return HttpResponseRedirect('/test/')
	else:
		form=AuthenticationForm()
		c={}
		c.update(csrf(request))
		c['signinForm']=form
		return render_to_response('loginform.html',c)


		
def test(request):
	s=''
	if request.user.is_authenticated():
		s=request.user.username
	return HttpResponse(s)			
