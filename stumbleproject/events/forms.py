from django.forms import ModelForm
from events.models import Link
# Create your views here.

class AddForm(ModelForm):
	class Meta:
		model=Link
		fields=['category','title','description','link']
		
