# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.base import TemplateView
import datetime
from .tasks import debug_task
from structlog import get_logger


class Home(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        logger = get_logger(__name__)
        logger.info("view")
        context = super(Home, self).get_context_data(**kwargs)
        now = str(datetime.datetime.now())
        debug_task.delay(now)
        context["now"] = now
        logger.info("done_sending_task")
        return context



