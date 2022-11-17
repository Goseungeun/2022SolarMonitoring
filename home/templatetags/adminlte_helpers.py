from hashlib import md5

from django import template
from django.conf import settings
from django.urls import reverse
from django.contrib import auth

from home.compat import is_authenticated

register = template.Library()

"""
@register.simple_tag(takes_context=True)
def logout_url(context):
    user = context['request'].user
    if user.is_superuser:
        setattr(settings, 'LOGOUT_REDIRECT_URL', '/admin')
    else : 
        setattr(settings, 'LOGOUT_REDIRECT_URL', '/')
    return auth.logout(context['request'])"""
    


@register.simple_tag(takes_context=True)
def avatar_url(context, size=None, user=None):
    # TODO: Make behaviour configurable
    user = context['request'].user if user is None else user
    # return "/static/admin-lte/dist/img/user3-128x128.jpg"
    return 'https://www.gravatar.com/avatar/{hash}?s={size}&d=mm'.format(
        hash=md5(user.email.encode('utf-8')).hexdigest() if is_authenticated(user) else '',
        size=size or '',
    )


@register.simple_tag(takes_context=True)
def add_active(context, url_name, *args, **kwargs):
    exact_match = kwargs.pop('exact_match', False)
    not_when = kwargs.pop('not_when', '').split(',')
    not_when = [nw.strip() for nw in not_when if nw.strip()]

    path = reverse(url_name, args=args, kwargs=kwargs)
    current_path = context.request.path

    if not_when and any(nw in current_path for nw in not_when):
        return ''

    if not exact_match and current_path.startswith(path):
        return ' active '
    elif exact_match and current_path == path:
        return ' active '
    else:
        return ''