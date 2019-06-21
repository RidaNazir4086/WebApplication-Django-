from django import forms

from .models import Job, applicant

class Job_form(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title',
            'department',
            'location',
            'jobType',
            'company',
            'position',
            'reqSkills',
            'description'
        ]

    def save(self, **kwargs):
        user = kwargs.pop('user')
        instance = super(Job_form, self).save(**kwargs)
        instance.postedBy = user
        instance.save()
        return instance


