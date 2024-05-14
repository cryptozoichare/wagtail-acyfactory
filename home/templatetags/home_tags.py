from django import template
from home.models import Todo

register = template.Library()

@register.inclusion_tag('home/includes/todos.html', takes_context=True)
def todos(context):
    return {
        'todos': Todo.objects.all(),
        'request': context['request'],
    }