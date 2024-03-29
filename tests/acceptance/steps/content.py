from behave import *
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()

@step('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    tag = page.title
    assert tag.text == content

@then('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.driver)
    tag = page.posts_section

    assert tag.is_displayed()