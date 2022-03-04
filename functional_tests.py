from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
                )

        # Type first item
        inputbox.send_keys('first item')

        # When hits enter, page updates and shows first item
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: first item', [row.text for row in rows])

        # Still has a text box inviting you to enter a to-do item. Adds a second one.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('second item')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Page updates and shows both items
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: first item', [row.text for row in rows])
        self.assertIn('2: second item', [row.text for row in rows])

        # Site generates a url with her items, with explanatory text telling her that

        # Visits the url, the to-do items are there

        # Done

if __name__ == '__main__':
    unittest.main()
