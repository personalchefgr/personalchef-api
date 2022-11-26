from django.db import models

# Create your models here.
class PostcodeArea(models.Model):
    postcode = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=25)
    town = models.CharField(max_length=25)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str("%s, %s, %s" % (self.town, self.state, self.postcode))

    class Meta:
        db_table = "postcode_areas"
        verbose_name = "Postcode Area"
        verbose_name_plural = "Postcode Areas"