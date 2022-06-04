from django import template

register = template.Library()
@register.filter(name='get')
def get(d, k):
    return d.get(k, None)

@register.filter
def get_range(value,current=1):
    return range(current,value+1)

