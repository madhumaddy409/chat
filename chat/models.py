from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='sender_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='receiver_messages')
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} to {}'.format(self.sender.username, self.receiver.username)


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='chat/')
    uploaded_at = models.DateTimeField(auto_now_add=True)