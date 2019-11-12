from rest_framework.viewsets import ReadOnlyModelViewSet

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

    def filter_queryset(self, queryset):
        filters = self.request.query_params

        if 'search' in filters:
            queryset = queryset.filter(title__icontains=filters.get('search'))

        if 'location' in filters:
            queryset = queryset.filter(location__icontains=filters.get('location'))

        if 'category' in filters:
            category_arr = filters.get('category').split(',')
            queryset = queryset.filter(categories__contains=category_arr)

        if 'levels' in filters:
            levels_arr = filters.get('levels').split(',')
            queryset = queryset.filter(levels__overlap=levels_arr)

        return queryset
