from django.db import models

# Create your models here.
class status_storage(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class problems(models.Model):
    id_request = models.BigIntegerField()
    id_employee = models.BigIntegerField()
    request_from_date = models.DateField()
    name_of_problem = models.CharField(max_length=80)
    description_of_problem = models.CharField(max_length=256)
    status = models.ForeignKey(status_storage, on_delete=models.CASCADE)
    date_of_finish = models.DateField()

