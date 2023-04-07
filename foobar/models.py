from django.db import models

class Note(models.Model):
    content = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return str(self.content) + " --- " + str(self.date)
