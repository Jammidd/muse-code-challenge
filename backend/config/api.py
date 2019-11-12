from rest_framework import routers

from apps.job_board.views import CompanyViewSet, JobViewSet

# Settings
api = routers.DefaultRouter()
api.trailing_slash = '/?'

# API
api.register(r'companies', CompanyViewSet)
api.register(r'jobs', JobViewSet)
