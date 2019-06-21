from django.contrib import admin
from .models import education , UserSkill , UserProject, UserExperience, UserInterest

# Register your models here.
admin.site.register(education)
admin.site.register( UserSkill)
admin.site.register( UserInterest)
admin.site.register( UserExperience)
admin.site.register( UserProject)


