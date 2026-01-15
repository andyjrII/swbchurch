from django import forms


class PlaceholderTextInput(forms.TextInput):
    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        # Check if the label is present in the widget context
        if "label" in context["widget"]:
            context["widget"]["attrs"]["placeholder"] = context["widget"]["label"]

        return context


class SearchForm(forms.Form):
    title = forms.CharField(
        required=False,
        widget=PlaceholderTextInput(
            attrs={
                "class": "form-control form-control-lg custom-form-control",
                "placeholder": "BOOK TITLE",
            }
        ),
    )
    
    def __init__(self, *args, **kwargs):
        authors = kwargs.pop('authors', [])
        super().__init__(*args, **kwargs)
        
        author_choices = [('', 'AUTHOR')] + [(author, author) for author in authors]
        self.fields['author'] = forms.ChoiceField(
            required=False,
            choices=author_choices,
            widget=forms.Select(
                attrs={
                    "class": "form-control form-control-lg custom-form-control",
                }
            ),
        )