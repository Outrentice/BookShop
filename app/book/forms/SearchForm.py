from django import forms

class SearchForm(forms.Form):
    search_input = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Поиск...', 'class': 'email'}))

