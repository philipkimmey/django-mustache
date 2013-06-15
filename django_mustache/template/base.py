from django.template.base import TemplateEncodingError
from django.utils.encoding import force_text

import pystache


class Template(object):
    def __init__(self, template_string, origin=None,
                 name='<Unknown Template>'):
        try:
            template_string = force_text(template_string)
        except UnicodeDecodeError:
            raise TemplateEncodingError("Templates can only be constructed"
                                        " from unicode or UTF-8 strings.")
        self.template_string = template_string
        self.name = name

    def render(self, context):
        context_dict = {}
        for d in context.dicts:
            context_dict.update(d)
        return pystache.render(self.template_string, context_dict)
