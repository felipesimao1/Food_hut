from django.db import models

# Create your models here.

class bookTables(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    

    def __str__(self):
        return self.name + ' - ' + self.email + str(self.guests) + ' - ' + str(self.date) + ' - ' + str(self.time)