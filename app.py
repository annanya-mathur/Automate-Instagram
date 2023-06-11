from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the WebDriver (ensure you have the appropriate webdriver installed for your browser)
driver = webdriver.Chrome('path_to_chrome_webdriver')

# Open Instagram login page
driver.get('https://www.instagram.com/accounts/login/')

# Wait for the page to load
time.sleep(2)

# Log in to Instagram
username_input = driver.find_element_by_name('username')
password_input = driver.find_element_by_name('password')

username_input.send_keys('your_username')
password_input.send_keys('your_password')

login_button = driver.find_element_by_xpath('//button[@type="submit"]')
login_button.click()

# Wait for the login process to complete
time.sleep(5)

# Perform actions on Instagram
# For example, let's like the first 5 posts on the home feed and follow some users
for _ in range(5):
    # Locate the heart (like) button
    like_button = driver.find_element_by_xpath('//span[@aria-label="Like"][@role="button"]')
    like_button.click()

    # Wait for a moment before liking the next post
    time.sleep(2)

# Scroll down to load more posts
scroll_element = driver.find_element_by_tag_name('body')
for _ in range(3):
    scroll_element.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

# Find and follow some users
for _ in range(3):
    # Locate the follow button
    follow_button = driver.find_element_by_xpath('//button[text()="Follow"]')
    follow_button.click()

    # Wait for a moment before following the next user
    time.sleep(2)

# Go to your profile page
profile_link = driver.find_element_by_xpath('//a[@href="/your_username/"]')
profile_link.click()

# Wait for the page to load
time.sleep(2)

# Edit your profile
edit_profile_button = driver.find_element_by_xpath('//button[text()="Edit Profile"]')
edit_profile_button.click()

# Update your profile information (e.g., bio)
bio_input = driver.find_element_by_xpath('//textarea[@name="biography"]')
bio_input.clear()
bio_input.send_keys("Hello, I'm automating Instagram!")

# Save the changes
submit_button = driver.find_element_by_xpath('//button[text()="Submit"]')
submit_button.click()

# Wait for a moment before closing the browser
time.sleep(2)

# Close the browser
driver.quit()
