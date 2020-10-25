from django.db import models

class Project(models.Model):
    """Project you worked for."""
    name = models.CharField(max_length=32, primary_key=True)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Entry(models.Model):
    """Single entry for work time."""
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)
    duration_in_minutes = models.IntegerField(
        "Duration in Minutes", null=True, blank=True)

    def save(self, *args, **kwargs):
        """Calculate duration on save."""
        if self.end_at:
            time_delta = self.end_at - self.start_at
            total_seconds = time_delta.total_seconds()
            self.duration_in_minutes = total_seconds / 60

        super().save(*args, **kwargs)
