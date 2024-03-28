from behave import *
from tests.acceptance.locators.home_page import HomePageLocators

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    title_tag = context.browser.find_element(*HomePageLocators.TITLE)
    assert title_tag.is_displayed()

@step('The title tag has content "(.*)"')
def step_impl(context, content):
    title_tag = context.browser.find_element(*HomePageLocators.TITLE)
    assert title_tag.text == content
