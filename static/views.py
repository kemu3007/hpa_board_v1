from django.views import generic

from static.models import StaticPage


class StaticPageView(generic.TemplateView):
    template_name = 'static/static_page.html'
    pagetype = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['static_page'] = StaticPage.objects.filter(pagetype=self.pagetype).first()
        return context
