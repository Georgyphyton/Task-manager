from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.utils.translation import gettext_lazy as _


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = _('''
        <ul><li>Your password must contain at least 8
        characters</li><li>The password must consist of numbers and letters</li></ul>''')

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'password1',
                  'password2']
