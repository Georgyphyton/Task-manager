from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = '''
        <ul><li>Ваш пароль должен содержать как минимум 8
        символов</li><li>Пароль должен состоять из цифр и букв</li></ul>'''

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'password1',
                  'password2']
