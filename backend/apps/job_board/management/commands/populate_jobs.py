import json

import requests

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from apps.job_board.models import Company, Job


class Command(BaseCommand):
    help = 'Populates the database with jobs'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--num-jobs', type=int,
                             help='Parameter to specify how many jobs to import', default=40)

    def handle(self, *args, **options):
        page = 1
        job_url = 'https://www.themuse.com/api/public/jobs?page=%s'

        num_jobs = options['num_jobs']

        not_complete = True

        while not_complete:
            # Get the count of existing jobs and exit if there are enough jobs
            job_count = len(Job.objects.all())
            if job_count >= num_jobs:
                break

            response = requests.get(job_url % page)

            if response.status_code == 200:
                response_json = response.json()
                num_pages = response_json['page_count']

                jobs_to_add = num_jobs - job_count
                count = 0
                for r in response_json['results']:
                    company_name = r['company']['name']

                    try:
                        company = Company.objects.get(name__iexact=company_name)
                    except Company.DoesNotExist:
                        company_response = requests.get('https://www.themuse.com/api/public/companies/%s' % r['company']['id'])

                        if company_response.status_code == 200:
                            data = company_response.json()
                            company_data = {
                                'name': data['name'],
                                'industries': [elem['name'] for elem in data['industries']],
                                'size': data['size']['short_name'].capitalize()[0]
                            }

                            company = Company.objects.create(**company_data)

                    job_data = {
                        'title': r['name'],
                        'company': company,
                        'description': r['contents'],
                        'location': r['locations'][0]['name'] if len(r['locations']) > 0 else None,
                        'categories': [elem['name'] for elem in r['categories']],
                        'levels': [elem['name'][0] for elem in r['levels']]
                    }

                    job, created = Job.objects.get_or_create(**job_data)

                    if jobs_to_add >= count:
                        break
                    else:
                        count += 1

                page += 1
