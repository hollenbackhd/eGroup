from django import template
register = template.Library()


@register.simple_tag
def define(the_string):
    return the_string

register.simple_tag(define)
