from django import views
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from .forms import ContactForm
from university.mixins import TitleViewMixin


class ContactFormView(TitleViewMixin, views.generic.FormView):
    template_name = 'university/contacts/contacts_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('course-list')
    page_title = _('Contacts')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
