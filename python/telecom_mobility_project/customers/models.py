from django.db import models

class Plan(models.Model):
    PLAN_CHOICES = [
        ('Platinum365', 'Platinum365'),
        ('Gold180', 'Gold180'),
        ('Silver90', 'Silver90'),
    ]
    name = models.CharField(max_length=50, choices=PLAN_CHOICES)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    validity = models.IntegerField()  # Number of days
    status = models.BooleanField(default=True)  # Active or Inactive

    def __str__(self):
        return self.name
