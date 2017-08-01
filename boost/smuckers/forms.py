from django import forms

from smuckers.models import Bol, BolItem, ForkliftDriver, TruckDriver

class BolForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
	    super(BolForm, self).__init__(*args, **kwargs)

	    for key in self.fields:
	        self.fields[key].required = False 

	class Meta:
		model = Bol
		fields = '__all__'
		widgets = {
			'truck_approved': forms.HiddenInput(),
            'approved': forms.HiddenInput(),
            'dock_number': forms.HiddenInput(),
            'seal_number': forms.HiddenInput(),
            'forklift_driver': forms.HiddenInput()
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

class ForkliftDriverForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
	    super(ForkliftDriverForm, self).__init__(*args, **kwargs)

	    for key in self.fields:
	        self.fields[key].required = False

	class Meta:
		model = ForkliftDriver
		fields = '__all__'
		widgets = {
        }

class TruckDriverForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
	    super(TruckDriverForm, self).__init__(*args, **kwargs)

	    for key in self.fields:
	        self.fields[key].required = False

	class Meta:
		model = TruckDriver
		fields = '__all__'
		widgets = {
        }