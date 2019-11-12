from rest_framework.serializers import ModelSerializer

from apps.job_board.models import Company, Job


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        depth = 2

