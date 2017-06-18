from django import forms

from smuckers.models import Bol, BolItem

class BolForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
	    super(BolForm, self).__init__(*args, **kwargs)

	    for key in self.fields:
	        self.fields[key].required = False 

	class Meta:
		model = Bol
		fields = '__all__'
		widgets = {
            'approved': forms.HiddenInput(),
            'dock_number': forms.HiddenInput(),
            'seal_number': forms.HiddenInput(),
        }

class BolItemForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
	    super(BolItemForm, self).__init__(*args, **kwargs)

	    for key in self.fields:
	        self.fields[key].required = False

	class Meta:
		model = BolItem
		fields = '__all__'
		widgets = {
            'bol': forms.HiddenInput(),
        }