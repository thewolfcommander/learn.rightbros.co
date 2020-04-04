from django.db import models

class EnrollForDemo(models.Model):
    """
    This model contains the data about the students who have registered for the demo of the learning platform.
    """
    STUDENT_CHOICES = [
        ('school', 'School Student'),
        ('college', 'College Student'),
        ('self', 'Self Learner'),
        ('working', 'Working Person'),
        ('other', 'Other')
    ]
    first_name = models.CharField(max_length=124, null=True)
    last_name = models.CharField(max_length=124, null=True)
    email = models.EmailField(null=True)
    father_name = models.CharField(max_length=255, null=True)
    mobile_number = models.CharField(max_length=10, null=True)
    student = models.CharField(max_length=124, null=True, choices=STUDENT_CHOICES, default="school")
    about = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['first_name', 'last_name', 'father_name']
        verbose_name = 'Enrollment for Demo'
        verbose_name_plural = 'Enrollements for Demo'

    def __str__(self):
        return "{} - {} {}".format(str(self.id), self.first_name, self.last_name)

