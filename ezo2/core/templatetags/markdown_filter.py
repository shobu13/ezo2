from django import template
from markdownx import utils

register = template.Library()

@register.filter
def markdownify(text):
    # safe_mode governs how the function handles raw HTML
    return utils.markdown(text, safe_mode='escape')