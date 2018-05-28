from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Article, Author,Category


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',  'password1', 'password2',)


class Profile(forms.ModelForm):
    class Meta:
        model = Author

        fields = (
             'profile_image', 'phone', 'details'
        )



class Article_Create(forms.ModelForm):
    class Meta:
        model = Article

        labels = ('Article Title', 'Choose Category', 'Choose Image', 'Write Details')

        fields = (
            'title', 'category', 'image', 'details'
        )


