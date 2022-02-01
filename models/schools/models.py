# source: https://learndjango.com/tutorials/django-best-practices-models

from django.db import models

# Create your models here.

# Models should always be Capitalized (eg. University, User, Article)
# and singular (eg. University not Universities)
# since they represents a single object
from django.urls import reverse


class University(models.Model):
    # define each choice as a tuple of tuples, with an all-uppercase name as a class attribute on the model
    # u = University(full_name='College of William and Mary', university_type='PUBLIC')
    # u.university_type # 'PUBLIC'
    # u.get_university_type_display() # 'A public university'
    UNIVERSITY_TYPE = (
        ('PUBLIC', 'A public university'),
        ('PRIVATE', 'A private university')
    )
    # Fields should be all lowercase using underscores not camelCase so full_name not FullName.
    full_name = models.CharField(max_length=100,
                                 verbose_name='university full name')

    # whenever you define a new database model both null and blank are set to false
    # null is database-related. When a field has null=True it can store a database entry as NULL, meaning no value.
    # blank is validation-related, if blank=True then a form will allow an empty value
    # for string-type Fields Django convention is instead to use the empty string '', not NULL
    # An exception is that if CharField has both unique=True and blank=True then null=True is also required to avoid unique constraint violations

    class Meta:
        # adding an index to speed things up. An index usually is a good idea
        # but maintaining it also requires some overhead so you'll want to test which implementation is more performant
        indexes = [models.Index(fields=['full_name'])]
        # ordering which sets the default order of a list of objects.
        # If we wanted to have a webpage where we listed all universities alphabetically
        ordering = ['-full_name']
        # explicitly name your model
        verbose_name = 'university'
        verbose_name_plural = 'universities'

    # The str method defines a human-readable representation of the model that is displayed in the Django admin site
    def __str__(self):
        return self.full_name

    # The get_absolute_url() method sets a canonical URL for the model.
    # This is required when using the reverse() function.
    # This example assumes a university_detail named URL referencing a detail view.
    def get_absolute_url(self):
        return reverse('university_detail', args=[str(self.id)])

# refering a model in template:
# <a href="{{ object.get_absolute_url }}/">{{ object.full_name }}</a>


class Student(models.Model):
    first_name = models.CharField('first name', max_length=30)
    last_name = models.CharField('last name', max_length=30)
    # ForeignKey means following a relationship "backward".
    # Django sets this in our example to student_set and any filter names to student__first_name.
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        # related_name() should be the plural of the model containing the ForeignKey (students for the Student model)
        related_name='students',
        # related_query_name() should be singular
        related_query_name='person',
    )

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('student_detail', args=[str(self.id)])

    # dartmouth = University.objects.get(full_name='Dartmouth')
    # dartmouth.student_set.all()  # returns all students at Dartmouth
    # dartmouth.objects.filter(student__first_name='william')  # returns all Dartmouth students named William