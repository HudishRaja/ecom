from django import template

register = template.Library()

@register.filter(name='replace_underscore')
def replace_underscore(value):
    """Replaces underscores with spaces."""
    return value.replace('_', ' ').upper()
@register.filter(name='replace_underscores')
def replace_underscores(value):
    """Replaces underscores with spaces."""
    return value.replace('_', ' ')
@register.filter(name='camelcase_to_spaces')
def camelcase_to_spaces(value):
    import re
    # Convert camel case to words with spaces
    words_with_spaces = re.sub(r'([a-z])([A-Z])', r'\1 \2', value)
    # Remove underscores
    return words_with_spaces.replace('_', ' ').title()