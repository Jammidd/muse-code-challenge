import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Company(models.Model):
    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=256)
    industries = ArrayField(models.CharField(max_length=128, blank=True))
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)

    def __str__(self):
        return '%s' % self.name


class Job(models.Model):
    LEVEL_CHOICES = (
        ('I', 'Internship'),
        ('E', 'Entry Level'),
        ('M', 'Mid Level'),
        ('S', 'Senior Level')
    )
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=256)
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)
    locations = ArrayField(models.CharField(max_length=128, blank=True), null=True, blank=True)
    levels = ArrayField(models.CharField(max_length=1, choices=LEVEL_CHOICES, blank=True))
    categories = ArrayField(models.CharField(max_length=128, blank=True))
    description = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.company.name, self.title)
