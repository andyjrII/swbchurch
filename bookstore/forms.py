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
