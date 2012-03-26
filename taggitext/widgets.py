from django import forms
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.simplejson import dumps


DEFAULT_JS_FILENAME = 'jquery-textext-1.3.0.js'
DEFAULT_BASE_URL = '/'.join([settings.STATIC_URL, 'js'])
DEFAULT_JS_PATH = '/'.join([DEFAULT_BASE_URL, DEFAULT_JS_FILENAME])

JS_PATH = getattr(settings, 'TAGGITEXT_JS_PATH', DEFAULT_JS_PATH)


class TagAutocomplete(forms.Textarea):
    input_type = 'text'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'rows': '3', 'cols': '80'})
        super(TagAutocomplete, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        list_view = reverse('taggitext-search')
        if value is not None and not isinstance(value, basestring):
            value = dumps([o.tag.name for o in value.select_related("tag")])
        html = super(TagAutocomplete, self).render(name, '', attrs)
        js = u'''
<script type="text/javascript">
    django.jQuery('#%s').textext({
        plugins: 'ajax tags autocomplete',
        ajax: {
            url: '%s',
            dataType: 'json'
        },
        tags: {
            items: %s
        }
    });
</script>
''' % (attrs['id'], list_view, value or '[]')
        return mark_safe("\n".join([html, js]))

    class Media:
        js = (JS_PATH,)
