from django.forms import ModelForm
from labels.models import Labels


class CreateLabelForm(ModelForm):

    class Meta:
        model = Labels
        fields = ['name']
