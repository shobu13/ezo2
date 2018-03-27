from django.forms.widgets import Widget
from django.template import loader
from django.utils.safestring import mark_safe

class BootstrapTextArea(Widget):
    template_name='widgets/WidTest.html'

    def __init__(self, attrs=None, placeholder="", style=""):
        self.attrs = attrs or {}
        self.placeholder=placeholder
        self.style=style


    def get_context(self, name, value, attrs=None):
        return {'widget':{
                'name':name,
                'value':value,
                'placeholder':self.placeholder,
                'class':'form-control',
                'style':self.style,
                }}

    def render(self, name, value, attrs=None):
        context=self.get_context(name, value, attrs)
        template=loader.get_template(self.template_name).render(context)
        return mark_safe(template)