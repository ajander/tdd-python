from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Heard about a web app, go check out the url
        self.browser.get(self.live_server_url)

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
        self.check_for_row_in_list_table('1: first item')

        # Still has a text box inviting you to enter a to-do item. Adds a second one.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('second item')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Page updates and shows both items
        self.check_for_row_in_list_table('1: first item')
        self.check_for_row_in_list_table('2: second item')

        self.fail('Finish writing the test!')

        # Site generates a url with her items, with explanatory text telling her that

        # Visits the url, the to-do items are there

        # Done

