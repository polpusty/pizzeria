from django import template

register = template.Library()


@register.filter(name='div')
def div(value, arg):
    try:
        value = int(value)
        arg = int(arg)
        if arg: return value / arg
    except (ZeroDivisionError, TypeError,):
        pass
    return ''
