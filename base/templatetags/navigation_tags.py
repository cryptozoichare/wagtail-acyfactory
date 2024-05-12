from django import template
from wagtail.models import Site


register = template.Library()



@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page

def is_active(page, current_page):
    # To give us active state on main navigation
    return current_page.url_path.startswith(page.url_path) if current_page else False