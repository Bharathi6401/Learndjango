from django.db import models


class Study(models.Model):
    study_name = models.CharField(max_length=200)
    study_phase = models.CharField(max_length=200)
    sponser_name = models.CharField(max_length=200)
    study_description = models.CharField(max_length=200)


