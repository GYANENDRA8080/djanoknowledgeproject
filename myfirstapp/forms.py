from django import forms

class FeedbackForm(forms.Form):
    title = forms.CharField(min_length=1, label='Title',widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(max_length=200, label='Subject Description',widget=forms.Textarea(attrs={'class':'form-control'}))
    email = forms.CharField(min_length=1, label='Email',widget=forms.TextInput(attrs={'class':'form-control'}))
