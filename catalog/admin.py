from django.contrib import admin

# Register your models here.

from catalog.models import Person, Gender, Education, Location

#admin.site.register(Person)
#admin.site.register(Gender)
#admin.site.register(Education)
#admin.site.register(Location)

# Define the admin class
class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_graduation', 'gender', 'education', 'location', 'creater')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_graduation'), 'gender', ('location', 'education'), 'creater']
    list_filter = ('gender', 'location')
# Register the admin class with the associated model
admin.site.register(Person, PersonAdmin)

# Register the Admin classes for Education using the decorator
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for Location using the decorator
@admin.register(Location) 
class LocationAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for Gender using the decorator
@admin.register(Gender) 
class GenderAdmin(admin.ModelAdmin):
    pass