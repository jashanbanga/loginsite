from django import forms
class APIform(forms.Form):
	g_username=forms.CharField(max_length='25')
class signinn(forms.Form):
	text=forms.CharField(max_length='20')