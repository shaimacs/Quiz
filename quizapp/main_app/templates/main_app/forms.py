from django import forms

class ScoreForm(forms.Form):
    score=forms.IntegerField(label='score')



# class LoginForm(forms.Form):
#     username = forms.CharField(label="User Name", max_length=64)
#     password = forms.CharField(widget=forms.PasswordInput())
