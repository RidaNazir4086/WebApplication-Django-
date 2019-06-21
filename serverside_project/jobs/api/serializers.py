from rest_framework import serializers
from jobs.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model= Job
        fields = '__all__'
        #fields = ('title' , 'department')

