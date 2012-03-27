from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from taggit.models import Tag
from taggitext.views import search_tags


class SearchViewTest(TestCase):
    fixtures = ['test.json']

    def setUp(self):
        self.client = Client()
        self.view = reverse('taggitext-search')

    def test_can_query(self):
        response = self.client.get(self.view, {'q': 'matrix'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '["The Matrix"]')

    def test_bad_request_on_empty_query(self):
        response = self.client.get(self.view, {})
        self.assertEqual(response.status_code, 400)
