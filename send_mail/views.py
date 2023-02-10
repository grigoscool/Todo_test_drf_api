from django.views import generic

from .forms import MailForm
from .models import Mail
from .task import send_spam


class SendMail(generic.CreateView):
    template_name = 'send_mail/send_mail.html'
    form_class = MailForm
    success_url = '/'
    context_object_name = 'form'

    def form_valid(self, form):
        form.save()
        send_spam.delay(form.instance.email)
        return super().form_valid(form)
