from rest_framework import status
from rest_framework.test import APITestCase


class GetSingleFieldTemplateTestCase(APITestCase):

    def test_get_only_email(self):
        data = {'contact_email': 'user@mail.com'}
        response = self.client.post(
            path='/api/get_form/',
            data=data,
        )
        self.assertEqual(
            first=response.status_code,
            second=status.HTTP_200_OK,
            msg='HTTP статус не 200.')
        self.assertEqual(
            first=response.content,
            second=b'"Only email"',
            msg='Не тот шаблон')

    def test_get_only_date(self):
        data = {'registration_date': '12.12.1212'}
        response = self.client.post(
            path='/api/get_form/',
            data=data,
        )
        self.assertEqual(
            first=response.status_code,
            second=status.HTTP_200_OK,
            msg='HTTP статус не 200.')
        self.assertEqual(
            first=response.content,
            second=b'"Only date"',
            msg='Не тот шаблон')

    def test_get_only_text(self):
        data = {'bio': 'Some information'}
        response = self.client.post(
            path='/api/get_form/',
            data=data,
        )
        self.assertEqual(
            first=response.status_code,
            second=status.HTTP_200_OK,
            msg='HTTP статус не 200.')
        self.assertEqual(
            first=response.content,
            second=b'"Only text"',
            msg='Не тот шаблон')

    def test_get_only_telephone(self):
        data = {'telephone_number': '+79998887766'}
        response = self.client.post(
            path='/api/get_form/',
            data=data,
        )
        self.assertEqual(
            first=response.status_code,
            second=status.HTTP_200_OK,
            msg='HTTP статус не 200.')
        self.assertEqual(
            first=response.content,
            second=b'"Only telephone"',
            msg='Не тот шаблон')


class IncorrectFormatTestCase(APITestCase):

    def test_incorrect_email(self):
        data = {'contact_email': 'not email format'}
        response = self.client.post(
            path='/api/get_form/',
            data=data,
        )
        self.assertEqual(
            first=response.status_code,
            second=status.HTTP_404_NOT_FOUND,
            msg='При некорректном вводе HTTP статус не 404.')
        self.assertEqual(
            first=response.content,
            second=b'{"contact_email":"text"}',
            msg='Валидация не сработала.')

    def test_incorrect_date(self):
        data = {'registration_date': 'not date format'}
        response = self.client.post(
            path='/api/get_form/',
            data=data,
        )
        self.assertEqual(
            first=response.status_code,
            second=status.HTTP_404_NOT_FOUND,
            msg='При некорректном вводе HTTP статус не 404.')
        self.assertEqual(
            first=response.content,
            second=b'{"registration_date":"text"}',
            msg='Валидация не сработала.')

    def test_incorrect_telephone(self):
        data = {'telephone_number': 'not telephone format'}
        response = self.client.post(
            path='/api/get_form/',
            data=data,
        )
        self.assertEqual(
            first=response.status_code,
            second=status.HTTP_404_NOT_FOUND,
            msg='При некорректном вводе HTTP статус не 404.')
        self.assertEqual(
            first=response.content,
            second=b'{"telephone_number":"text"}',
            msg='Валидация не сработала.')


class ReadMeTestCase(APITestCase):


    def test_personal_data(self):
        data = {
            "contact_email": "user@gmail.com",
            "telephone_number": "+7 999 888 77 66"
        }
        response = self.client.post(
            path='/api/get_form/',
            data=data,
        )
        self.assertEqual(
            first=response.status_code,
            second=status.HTTP_200_OK,
            msg='HTTP статус не 200.')
        self.assertEqual(
            first=response.content,
            second=b'"Contact data"',
            msg='Валидация не сработала.')


    def test_incorrect_telephone(self):
        data = {
            "contact_email": "I am email",
            "telephone_number": "12.12.1212"
        }
        response = self.client.post(
            path='/api/get_form/',
            data=data,
        )
        self.assertEqual(
            first=response.status_code,
            second=status.HTTP_404_NOT_FOUND,
            msg='При некорректном вводе HTTP статус не 404.')
        self.assertEqual(
            first=response.content,
            second=b'{"contact_email":"text","telephone_number":"date"}',
            msg='Не тот шаблон')