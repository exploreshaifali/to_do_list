from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        print("inside setup")
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        print("inside test method")
        # Bob has heard about a cool new to-do online app
        # He goes to check out its homepage
        self.browser.get('http://127.0.0.1:9000/')

        # He notices page title and header mentioned on to-do list
        print("assert is about to run :O")
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        inbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inbox.get_attribute('placeholder'), 'Enter a to-do item'
            )

        # He types "Buy Kites" into a text box (Bob's hobby is kite flying)
        inbox.send_keys('Buy Kites')

        # When he hits enter, the page updates, and now the page lists
        # "1: Buy Kites" as an item in a to-do list
        inbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1. Buy Kites' for row in rows),
            "New to-do item did not appear in table")

        # There is still a text box inviting her to add another item. He enters
        # "make kites ready to fly"
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on his list

        # Bob wonders whehter the site will remember his list. Then he sees
        # that the site has generated
        # a unique URL for him -- there is some explanatory text to that effect.

        # He visits that URL - his to-do list is still there

        # Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
