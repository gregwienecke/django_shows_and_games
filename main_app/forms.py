from django import forms

class GameForm(forms.Form):
	name = forms.CharField(label="Name", max_length=100)
	release = forms.CharField(label="Release", max_length=100)

class ShowForm(forms.Form):
	name = forms.CharField(label="Name", max_length=100)
	seen = forms.BooleanField(label="Seen")