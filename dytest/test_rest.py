import unittest
import requests

class UserTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8001/users'
        self.auth=('admin','admin123456')

    def test_user1(self):
        r=requests.get(self.base_url+'/1/',auth=self.auth)
        result=r.json()
        self.assertEqual(result['username'],'admin')
        self.assertEqual(result['email'],'admin@mail.com')

    def test_user2(self):
        r = requests.get(self.base_url + '/2/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'kara')
        self.assertEqual(result['email'], 'kara@mail.com')


    def test_user3(self):
        r = requests.get(self.base_url + '/3/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'xiong')
        self.assertEqual(result['email'], 'xiong@mail.com')


class GroupsTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8001/Groups'
        self.auth=('admin','admin123456')

    def test_group1(self):
        r=requests.get(self.base_url+'/1/',auth=self.auth)
        result=r.json()
        self.assertEqual(result['name'],'test')

    def test_group2(self):
        r = requests.get(self.base_url + '/2/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['name'], 'developer')


if __name__=='__main__':
    unittest.main()