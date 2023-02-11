from django.views import generic
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Reminder
from .serializers import ReminderSerializer
from .task import remind_mail


class ReminderCreateAPI(APIView):
    """
     View to create reminder api and send mail after delay minutes
    """

    def post(self, request):
        serializer = ReminderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        remind_mail.apply_async(args=[(request.data['email'])],
                                countdown=((request.data['delay_minutes']) * 60))

        return Response(serializer.data)


class ReminderListApi(generics.ListAPIView):
    """ View to show list of all reminders """
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class ReminderRUD(generics.RetrieveUpdateDestroyAPIView):
    """ View to CUD current remind """
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    permission_classes = [permissions.IsAdminUser, ]

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
