from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexRender(LoginRequiredMixin, TemplateView):
    """ Renderizzo la Single Page Application """
    
    def get_template_names(self):
        template_name = "index.html"
        return template_name
