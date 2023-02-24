'''from django.db import models
from accounts.models import User
# Create your models here.
class Ticket(models.Model):
    TIME_SLOT = [
    (1, '9:00'),
    (2, '11:00'),
    (3, '1:00'),
    (4, '3:00'),
    (5, '5:00'),
    (6, '7:00'),
    (7, '9:00'),
    ]
    women = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'user_type': 'W'}, related_name='Women')
    catering = models.ForeignKey(User,on_delete=models.CASCADE, limit_choices_to={'user_type': 'C'})
    date =  models.DateField()
    time = models.TimeField(null=True)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'ticket'
        constraints = [
            models.UniqueConstraint(fields=['women','date'], name='unique_booking')
        ]
        ordering = ['date', 'time']

    def __str__(self):
        return f"{self.women.get_full_name()}'sbooking on {self.women.time} on {self.date}"'''

