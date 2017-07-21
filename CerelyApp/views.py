from django.views.generic.edit import FormView
from CerelyApp.forms import CelerybackForm


class CelerybackView(FormView):
    template_name = 'cerelyback/contact.html'
    form_class = CelerybackForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        return super(CelerybackView, self).form_valid(form)
