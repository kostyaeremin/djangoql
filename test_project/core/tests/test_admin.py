import json

from django.contrib.auth.models import User
from django.test import TestCase

from djangoql.models import SavedQuery

try:
    from django.core.urlresolvers import reverse
except ImportError:  # Django 2.0
    from django.urls import reverse


class DjangoQLAdminTest(TestCase):
    def setUp(self):
        self.credentials = {'username': 'test', 'password': 'lol'}
        User.objects.create_superuser(email='herp@derp.rr', **self.credentials)

    def test_introspections(self):
        url = reverse('admin:core_book_djangoql_introspect')
        # unauthorized request should be redirected
        response = self.client.get(url)
        self.assertEqual(302, response.status_code)
        self.assertTrue(self.client.login(**self.credentials))
        # authorized request should be served
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        introspections = json.loads(response.content.decode('utf8'))
        self.assertEqual('core.book', introspections['current_model'])
        for model in ('core.book', 'auth.user', 'auth.group'):
            self.assertIn(model, introspections['models'])


class DjangoQLSavedQueryTest(TestCase):
    def setUp(self):
        self.credentials = {'username': 'test', 'password': 'lol'}
        User.objects.create_superuser(email='herp@derp.rr', **self.credentials)
        SavedQuery.objects.create(
            description='description',
            query='query',
            is_public=True,
            model_id=7,
            author=User.objects.get(username='test')
        )

    def test_create_query(self):
        url = reverse('admin:core_book_djangoql_create_saved_query')
        post_data = {
            'description': 'description',
            'query': 'query',
            'is_public': True
        }
        # unauthorized request should be redirected
        response = self.client.post(url, post_data)
        self.assertEqual(302, response.status_code)
        self.assertTrue(self.client.login(**self.credentials))
        # authorized request should be served
        response = self.client.post(url, post_data)
        self.assertEqual(201, response.status_code)

        saved_query = json.loads(response.content.decode('utf8'))
        self.assertEqual(post_data.get('description'), saved_query.get('description'))
        self.assertEqual(post_data.get('query'), saved_query.get('query'))
        self.assertEqual(post_data.get('is_public'), saved_query.get('is_public'))


    def test_update_query(self):
        url = reverse('admin:core_book_djangoql_edit_saved_query', kwargs={'pk':1})
        post_data = {
            'id': 1,
            'description': 'new description',
            'query': 'new query',
            'is_public': False
        }
        # unauthorized request should be redirected
        response = self.client.post(url, post_data)
        self.assertEqual(302, response.status_code)
        self.assertTrue(self.client.login(**self.credentials))
        # authorized request should be served
        response = self.client.post(url, post_data)
        self.assertEqual(200, response.status_code)

        saved_query = json.loads(response.content.decode('utf8'))
        self.assertEqual(post_data.get('id'), saved_query.get('id'))
        self.assertEqual(post_data.get('description'), saved_query.get('description'))
        self.assertEqual(post_data.get('query'), saved_query.get('query'))
        self.assertEqual(post_data.get('is_public'), saved_query.get('is_public'))

    def test_fail_update_query(self):
        url = reverse('admin:core_book_djangoql_edit_saved_query', kwargs={'pk':2})
        post_data = {
            'id': 2,
            'description': 'new description',
            'query': 'new query',
            'is_public': False
        }
        # unauthorized request should be redirected
        response = self.client.post(url, post_data)
        self.assertEqual(302, response.status_code)
        self.assertTrue(self.client.login(**self.credentials))
        # authorized request should be served
        response = self.client.post(url, post_data)
        self.assertEqual(404, response.status_code)

    def test_delete_query(self):
        url = reverse('admin:core_book_djangoql_edit_saved_query', kwargs={'pk': 1})
        # unauthorized request should be redirected
        response = self.client.delete(url)
        self.assertEqual(302, response.status_code)
        self.assertTrue(self.client.login(**self.credentials))
        # authorized request should be served
        count_before = SavedQuery.objects.count()
        response = self.client.delete(url)
        self.assertEqual(200, response.status_code)
        count_after = SavedQuery.objects.count()
        self.assertEqual(count_before, count_after+1)