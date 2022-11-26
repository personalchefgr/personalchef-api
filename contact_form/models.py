from django.db import models

# Create your models here.
class Message(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        db_table = "contact_form_messages"
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ['-created_at']