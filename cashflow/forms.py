from django import forms


class UserForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "comment-form", "placeholder": "Enter name"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class": "comment-form", "placeholder": "Enter email"}))
    comment = forms.CharField(widget=forms.Textarea(attrs={"class": "comment-form", "placeholder": "Enter message"}))


