from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import JobSerializer
from jobs.models import Job
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

#### APIs #####

class JobViewSet(viewsets.ViewSet):
    querySet = Job.objects.all()
    serializer_class = JobSerializer

    def retrieve(self, request, pk=None):
        job = get_object_or_404(self.querySet, pk=pk)
        serializer = self.serializer_class(job)
        return Response(serializer.data)

    def list(self, request):
        serializer = self.serializer_class(self.querySet, many=True)
        return Response(serializer.data)


    def create(self, request):
        job = request.data
        serializer = self.serializer_class(data=job)
        if serializer.is_valid():
           job_saved = serializer.save()
           return Response({"success": "Job '{}' created successfully".format(job_saved.title)})
        else:
            return Response(serializer.errors)


    def update(self, request, pk=None):
        saved_article = get_object_or_404(Job.objects.all(), pk=pk)
        data = request.data
        serializer = JobSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid():
            job_saved = serializer.save()
            return Response({"success": "Job '{}' updated successfully".format(job_saved.title)})
        else:
            return Response(serializer.errors)


    def destroy(self, request, pk=None):
        job = get_object_or_404(Job.objects.all(), pk=pk)
        job.delete()
        return Response({"success": "Job '{}' deleted successfully".format(job.title)})

