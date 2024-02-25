from django import forms

class IndexCardForm(forms.Form):
    username = forms.CharField(label='Username', max_length=32)
    email = forms.CharField(label='Email', max_length=100)
    password = forms.CharField(label='Password', max_length=32)
    reemail = forms.CharField(label='Re-enter Email', max_length=100)
    repassword = forms.CharField(label='Re-enter Password', max_length=32)