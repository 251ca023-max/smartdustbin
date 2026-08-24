from django.db import models


class WasteData(models.Model):

    bin_id = models.IntegerField(default=1)

    distance = models.FloatField()

    waste_level = models.FloatField()

    status = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

class Alert(models.Model):
    bin_id = models.IntegerField()
    alert_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bin {self.bin_id} - {self.waste_level}%"