from django.utils.translation import ugettext_lazy as _
from django.utils.simplejson import loads

from taggit.forms import TagField
from taggit.managers import TaggableManager as BaseTaggableManager

from widgets import TagAutocomplete


class AutocompleteTagField(TagField):
    widget = TagAutocomplete

    def clean(self, value):
        words = loads(value)
        words.sort()
        return words


class TaggableManager(BaseTaggableManager):
    def formfield(self, form_class=AutocompleteTagField, **kwargs):
        defaults = {
            "label": _("Tags"),
            "help_text": "",
        }
        defaults.update(kwargs)
        kwargs['widget'] = TagAutocomplete
        return form_class(**kwargs)
