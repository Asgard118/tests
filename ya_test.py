import unittest
import requests

class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        with open('Ya_token.txt', 'r') as file:
            self.token = file.readline().strip()

        self.base_url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def test_create_folder(self):
        folder_name = 'Test'
        headers = {'Authorization': f'OAuth {self.token}'}
        params = {'path': folder_name}
        response = requests.put(self.base_url, headers=headers, params=params)

        self.assertEqual(response.status_code, 201)

        response = requests.get(self.base_url, headers=headers, params=params)
        self.assertEqual(response.status_code, 200)

    def test_create_existing_folder(self):
        folder_name = 'TestFolder'
        headers = {'Authorization': f'OAuth {self.token}'}
        params = {'path': folder_name}
        response = requests.put(self.base_url, headers=headers, params=params)

        self.assertEqual(response.status_code, 409)

    def test_create_folder_without_token(self):
        folder_name = 'TestFolder'
        params = {'path': folder_name}
        response = requests.put(self.base_url, params=params)

        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
