from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


@method_decorator(login_required, name='dispatch')
class ReportView(TemplateView):
    template_name = 'report/reports.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={

        })

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, context={

        })

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ReportView, self).dispatch(*args, **kwargs)
