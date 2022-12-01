"""
Module docstring
"""
from django.contrib.auth.forms import AuthenticationForm as AuthenticationFormGeneric
from django.forms import Widget


class AuthenticationForm(AuthenticationFormGeneric):
    """
    Class docstring
    """

    def __init__(self, *args, **kwargs):
        """
        Some docstring
        """
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"
