from django import forms

from .models import education, UserSkill, UserExperience , UserInterest, UserProject

class EducationForm(forms.ModelForm):
    class Meta:
        model = education
        fields = [
            'school',
            'degree',
            'field_of_study',
            'from_Year',
        ]

    def save(self, **kwargs):
        user = kwargs.pop('user')
        instance = super(EducationForm, self).save(**kwargs)
        instance.user = user
        instance.save()
        return instance


class SkillForm(forms.ModelForm):
    class Meta:
        model = UserSkill
        fields = [
            'skill',
        ]

    def save(self, **kwargs):
        user = kwargs.pop('user')
        instance = super(SkillForm, self).save(**kwargs)
        instance.user = user
        instance.save()
        return instance

class UserExperienceForm(forms.ModelForm):
    class Meta:
        model = UserExperience
        fields = [
            'Experience',
        ]

    def save(self, **kwargs):
        user = kwargs.pop('user')
        instance = super(UserExperienceForm, self).save(**kwargs)
        instance.user = user
        instance.save()
        return instance

class UserInterestForm(forms.ModelForm):
    class Meta:
        model = UserInterest
        fields = [
            'Interest',
        ]

    def save(self, **kwargs):
        user = kwargs.pop('user')
        instance = super(UserInterestForm, self).save(**kwargs)
        instance.user = user
        instance.save()
        return instance

class UserProjectForm(forms.ModelForm):
    class Meta:
        model = UserProject
        fields = [
            'Title',
            'Course',
            'Description',
        ]

    def save(self, **kwargs):
        user = kwargs.pop('user')
        instance = super(UserProjectForm, self).save(**kwargs)
        instance.user = user
        instance.save()
        return instance
