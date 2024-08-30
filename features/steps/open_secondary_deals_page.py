from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


@given ('Open main page')
def open_main_page(context):
    context.driver.get('https://soft.reelly.io/sign-in')
    sleep(2)


@when ('Log in to the page')
def click_on_email_box(context):
    context.driver.find_element(By.ID, 'email-2').send_keys('nsimic1989@gmail.com')
    context.driver.find_element(By.ID, 'field').send_keys('Jaz1989@@')
    context.driver.find_element(By.XPATH, "//a[@class='login-button w-button']").click()
    sleep(2)


@when ('Click on Secondary option at the left side menu')
def click_on_secondary(context):
    context.driver.find_element(By.XPATH, "//a[@href='/secondary-listings']").click()
    # context.driver.find_elements(By.XPATH, "//div[@text()='Secondary']").click()
    # context.driver.find_elements(By.XPATH, "//a[@text()='Secondary']").click()
    sleep(2)


@then ('Verify the right page opens')
def verify_right_page_opens(context):
    context.driver.find_elements(By.XPATH, "//a[@wized='addListingButtonMLS']")
    sleep(2)


@then('Go to the final page using the pagination button')
def go_to_final_page(context):
    total_page_element = context.driver.find_element(By.XPATH, "//div[@wized='totalPageProperties']")
    total_page = int(total_page_element.text)
    for page in range(1, total_page):
        next_button = context.driver.find_element(By.XPATH, "//a[@class='pagination__button w-inline-block']")
        next_button.click()
        sleep(1)


@then ('Go back to the first page using the pagination button')
def go_to_beginning_page(context):
    first_page_element = context.driver.find_element(By.XPATH, "//div[@wized='currentPageProperties']")
    first_page = int(first_page_element.text)
    for page in range(1, first_page):
        previous_button = context.driver.find_element(By.XPATH, "//div[@wized='previousPageMLS']")
        previous_button.click()
        sleep(1)