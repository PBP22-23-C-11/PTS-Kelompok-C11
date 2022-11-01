import datetime
from http import HTTPStatus
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from obrolan.models import Diskusi

# Create your tests here.
class ObrolanTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_obrolan_not_logged_in(self):
        response = self.client.get(reverse('obrolan:show_obrolan'))
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'obrolan_not_logged_in.html')

    def test_obrolan(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('obrolan:show_obrolan'))
        self.assertEquals(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'obrolan.html')

    def test_json(self):
        response = self.client.get(reverse('obrolan:show_diskusi_json'))
        self.assertEquals(response.status_code, HTTPStatus.OK)

    def test_add(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('obrolan:create_diskusi_ajax'), data={
            'title': 'Reply',
            'toWho': 'All',
            'message': 'Halo',
        })
        self.assertEquals(response.status_code, HTTPStatus.OK)

    def test_delete(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        date = datetime.datetime.now(datetime.timezone.utc)+ datetime.timedelta(hours=7)
        Diskusi.objects.create(user=self.user, username='testuser', date=date, title='Reply', toWho='All', message='Halo')
        id = Diskusi.objects.filter(user=self.user, title='Reply', toWho='All', message='Halo').values('id')[0]['id']
        response = self.client.post(reverse('obrolan:delete-disc', args=[id]), data={})
        self.assertEquals(response.status_code, HTTPStatus.OK)
    
