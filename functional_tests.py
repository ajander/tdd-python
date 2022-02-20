from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Heard about a web app, go check out the url
        self.browser.get('http://localhost:8000')

        # Notices page title says something about to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # Invited to enter a to-do item

        # Type first item

        # When hits enter, page updates and shows first item

        # Still has a text box inviting you to enter a to-do item. Adds a second one.

        # Page updates and shows both items

        # Site generates a url with her items, with explanatory text telling her that

        # Visits the url, the to-do items are there

        # Done

if __name__ == '__main__':
    unittest.main()
