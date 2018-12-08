from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Gender(models.Model):
    """Model representing a person's gender."""
    name = models.CharField(max_length=200, help_text='Enter a gender')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Person(models.Model):
    """Model representing an person."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_graduation = models.DateField('Graduated', null=True, blank=True)

    # Foreign Key used because person can only have one education, but educations can have multiple persons
    # Education as a string rather than object because it hasn't been declared yet in the file
    education = models.ForeignKey('Education', on_delete=models.SET_NULL, null=True)
    
    # Foreign Key used because gender can contain many persons. Persons can cover one gender.
    # Gender class has already been defined so we can specify the object above.
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    
    # Foreign Key used because person can only have one location, but locations can have multiple persons
    # Location as a string rather than object because it hasn't been declared yet in the file
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True)
    creater = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
    
    def get_absolute_url(self):
        """Returns the url to access a particular person instance."""
        return reverse('person-detail', args=[str(self.id)])

    def display_gender(self):
        """Create a string for the Gender. This is required to display gender in Admin."""
        return ', '.join(gender.name for gender in self.gender.all())
    
    display_gender.short_description = 'Gender'

class Education(models.Model):
    """Model representing a person's education."""
    name = models.CharField(max_length=200, help_text='Enter an education')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name   
    def get_absolute_url(self):
        """Returns the url to access a particular education instance."""
        return reverse('education-detail', args=[str(self.id)])

class Location(models.Model):
    """Model representing a person's location."""
    name = models.CharField(max_length=200, help_text='Enter an location')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name  

    def get_absolute_url(self):
        """Returns the url to access a particular location instance."""
        return reverse('location-detail', args=[str(self.id)])