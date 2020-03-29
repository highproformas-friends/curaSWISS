from django.conf import settings
from django.db import models
from apps.role.models import Function

class Skill(models.Model):

    certificate_needed = models.BooleanField(default=False)
    short_text = models.CharField(max_length=20, null=True)
    description = models.TextField(default='')
    bla = models.BooleanField(default=False)
    # parent_skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True)
    valid_function = models.ManyToManyField(
        Function,
    )

    class Meta:
        ordering = ['short_text']

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.short_text

