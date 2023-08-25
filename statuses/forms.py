from django.forms import ModelForm
from statuses.models import Statuses


class CreateStatusForm(ModelForm):

    class Meta:
        model = Statuses
        fields = ['name']
