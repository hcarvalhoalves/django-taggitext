django-taggitext
================

This app extends **django-taggit** with an autocomplete field provided by the awesome **jQuery's TextExt plugin** (http://textextjs.com/).

Using it
--------

1. Add to `settings.py`:

        INSTALLED_APPS = (
            # ...
            'taggitext',
        )
        
2. Add to URLs:

        url(r'^admin/taggitext/', include('taggitext.urls')),

3. Add to your models:

        from django.db import models
        from taggitext.managers import TaggableManager
        
        
        class Page(models.Model):
            # ...
            tags = TaggableManager()

4. Enjoy a sane tagging widget on the admin

This package includes a slightly modified copy of the TextExt plugin to work smooth with Django's admin, but you can serve your own by setting `TAGGITEXT_JS_PATH` on `settings.py`.