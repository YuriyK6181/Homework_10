"""
Module docstring
"""
from django.contrib.auth.forms import AuthenticationForm as AuthenticationFormGeneric
from django.forms import Widget

"""
Class docstring
"""
class AuthenticationForm(AuthenticationFormGeneric):

    def __init__(self, *args, **kwargs):
        """
        Some docstring
        """
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name, field, field.widget)
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"
