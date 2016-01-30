from selenium import webdriver

# Bob has heard about a cool new to-do online app
# He goes to check out its homepage
browser = webdriver.Firefox()
browser.get('http://127.0.0.1:9000/')

# He notices page title and header mentioned on to-do list
assert 'To-Do' in browser.title

# He is invited to enter a to-do item straight away

# He types "Buy Kites" into a text box (Bob's hobby is kite flying)

# When he hits enter, the page updates, and now the page lists
# "1: Buy Kites" as an item in a to-do list

# There is still a text box inviting her to add another item. He enters
# "make kites ready to fly"

# The page updates again, and now shows both items on his list

# Bob wonders whehter the site will remember his list. Then he sees that the site has generated
# a unique URL for him -- there is some explanatory text to that effect.

# He visits that URL - his to-do list is still there

# Satisfied, he goes back to sleep

browser.quit()
