from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    age1 = models.IntegerField(default=18)
    last_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + "  " + self.description