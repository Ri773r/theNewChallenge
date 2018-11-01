from django import template

register = template.Library()

@register.filter()
def label_with_classes(value,args):
    return value.label_tag(attrs=eval(args))

@register.filter()
def widget_with_classes(value,args):
    return value.as_widget(attrs=eval(args))

