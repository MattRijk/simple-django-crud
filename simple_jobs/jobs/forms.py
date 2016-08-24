from jobs.models import Job
from django.forms.models import ModelForm


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields=['title', 'location', 'company']
        