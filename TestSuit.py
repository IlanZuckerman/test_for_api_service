import unittest, json, requests

class TestSuit(unittest.TestCase):

    def setUp(self):
        pass

#section 1
    def test_1(self):
        url = 'http://localhost:5000/api/books/1'
        response = requests.get(url=url)
        data = response.json()
        if not((data['book']['id'] == 1) and (data['book']['description'] == 'first element')
               and (data['book']['title'] == 'first')):
            self.fail("Actual responce is not as expected")
        print("test_1 passed")

# section 2
    def test_2(self):
        url = 'http://localhost:5000/api/books/1'
        data_to_put = {
            'title': u'put test title',
            'description': u'put test description'
        }
        headers = {'Content-Type': 'application/json'}

        response = requests.put(url=url, data=json.dumps(data_to_put), headers=headers)
        self.assertEquals(response.status_code, 200, "test_put has failed. status code is not as expected")

# section 3
        data = requests.get(url=url).json()
        if not((data['book']['id'] == 1) and (data['book']['description'] == 'put test description')
               and (data['book']['title'] == 'put test title')):
            self.fail("test_put has failed. Looks like the book wasnt updated")

        print("test_2 passed")

# section 4
    def test_3(self):
        url = 'http://localhost:5000/api/books/1'
        response = requests.delete(url=url)
        self.assertEquals(response.status_code, 200, "test_delete failed. status code is not as expected")

# section 5
        response = requests.get(url=url)
        self.assertEquals(response.status_code, 404, "test_delete failed. it appears that item wasn't deleted")

        print("test_3 passed")

if __name__ == '__main__':
    unittest.main()