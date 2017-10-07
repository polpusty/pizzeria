from django import template

register = template.Library()


@register.filter(name='add_css_to_field')
def add_css_to_field(value, arg):
    css_classes = value.field.widget.attrs.get('class', '').split(' ')
    if css_classes and arg not in css_classes:
        css_classes = '%s %s' % (css_classes, arg)
    return value.as_widget(attrs={'class': css_classes})
