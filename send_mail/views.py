from django.views import generic
from rest_framework import generics, permissions
from .models import Reminder
from .serializers import ReminderSerializer

class ReminderCreateAPI(generics.CreateAPIView):
    """ View to create reminder api """
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


# class SendMail(generic.CreateView):
#     template_name = 'send_mail/send_mail.html'
#     form_class = MailForm
#     success_url = '/'
#     context_object_name = 'form'
#
#     def form_valid(self, form):
#         form.save()
#         send_spam.delay(form.instance.email)
#         return super().form_valid(form)
