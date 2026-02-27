from playwright.sync_api import sync_playwright, expect, Page
import pytest


@pytest.mark.usefixtures('initialize_browser_state')
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_label = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_label).to_be_visible()
    expect(courses_label).to_have_text('Courses')

    result_block = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(result_block).to_be_visible()
    expect(result_block).to_have_text('There is no results')

    empty_result_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_result_icon).to_be_attached()
    expect(empty_result_icon).to_be_visible()

    no_result_description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(no_result_description).to_be_visible()
    expect(no_result_description).to_have_text('Results from the load test pipeline will be displayed here')
