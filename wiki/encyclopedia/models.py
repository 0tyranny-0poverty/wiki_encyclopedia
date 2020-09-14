from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User  # Required to assign User

# Create your models here.

class CaseInsensitiveFieldMixin:
    """
    Field mixin that uses case-insensitive lookup alternatives if they exist.
    """

    LOOKUP_CONVERSIONS = {
        'exact': 'iexact',
        'contains': 'icontains',
        'startswith': 'istartswith',
        'endswith': 'iendswith',
        'regex': 'iregex',
    }

    def get_lookup(self, lookup_name):
        converted = self.LOOKUP_CONVERSIONS.get(lookup_name, lookup_name)
        return super().get_lookup(converted)

class CICharField(CaseInsensitiveFieldMixin, models.CharField):
    pass

class Entry(models.Model):
    subject = CICharField(max_length=20, unique=True)
    content = models.TextField(blank=False)
    
    class Meta:
        ordering = ['subject']

    def __str__(self):
        """String for representing the Model object."""
        return self.subject
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this entry."""
        return reverse('entry_detail', args=[int(self.id)])


    
