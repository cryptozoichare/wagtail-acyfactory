import hashlib
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from django.contrib.contenttypes.models import ContentType
from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe

from django_comments.models import CommentFlag
from django_comments_xtd import get_model as get_comment_model
from django_comments_xtd.api import frontend
from django_comments_xtd.models import LIKEDIT_FLAG, DISLIKEDIT_FLAG
from django_comments_xtd.utils import (
    get_app_model_options, get_current_site_id, get_html_id_suffix
)


XtdComment = get_comment_model()



register = template.Library()

# ----------------------------------------------------------------------
@register.filter
def xtd_comment_libravatar_url(email, size=48, avatar='identicon'):
    """
    This is the parameter of the production avatar.
    The first parameter is the way of generating the
    avatar and the second one is the size.
    The way os generating has mp/identicon/monsterid/wavatar/retro/hide.
    """
    return ("//seccdn.libravatar.org/avatar/%s?%s&d=%s" %
            (hashlib.md5(email.lower().encode('utf-8')).hexdigest(),
             urlencode({'s': str(size)}), avatar))


# ----------------------------------------------------------------------
@register.filter
def xtd_comment_libravatar(email, config='48,identicon'):
    size, avatar = config.split(',')
    url = xtd_comment_libravatar_url(email, size, avatar)
    return mark_safe('<img src="%s" height="%s" width="%s">' %
                     (url, size, size))


# ----------------------------------------------------------------------