from jobs.api.viewsets import JobViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('jobs' , JobViewSet, base_name='job')

