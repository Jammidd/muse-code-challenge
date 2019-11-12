from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ReadOnlyModelViewSet, generics
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

from apps.job_board.models import Company, Job
from apps.job_board.serializers import CompanySerializer, JobSerializer


# Create your views here.
class CompanyViewSet(ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    permission_classes = []
    serializer_class = CompanySerializer


class JobViewSet(ReadOnlyModelViewSet):
    queryset = Job.objects.all()
    permission_classes = []
    serializer_class = JobSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']
