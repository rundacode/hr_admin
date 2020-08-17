from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class HrCompany(models.Model):
    hr_company_name         = models.CharField(max_length=50)
    company_user            = models.OneToOneField(User, # this will reference/retrive the employees associated with the hr company that
                                                on_delete=models.CASCADE,  # the employee was registered
                                                )
    def __str__(self):
       return self.hr_company_name



class Employee(models.Model):
    # Attributes
    company             = models.ForeignKey(HrCompany, # this will reference/retrive the employees associated with the hr company that
                                              on_delete=models.CASCADE,  # the employee was registered
                                            )
    first               = models.CharField(max_length=20)
    last                = models.CharField(max_length=20)
    age                 = models.CharField(max_length=2)
    department          = models.CharField(max_length=25)
    mail                = models.CharField(max_length=50)
    date_posted         = models.DateTimeField(default=timezone.now)
    employe_id          = models.IntegerField()

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    def __str__(self):
        return self.first + " " + self.last
