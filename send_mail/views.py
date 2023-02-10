from django.views import generic

from .forms import MailForm
from .models import Mail
from .servises import send


class SendMail(generic.CreateView):
    template_name = 'send_mail/send_mail.html'
    form_class = MailForm
    success_url = '/'
    context_object_name = 'form'

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form)
