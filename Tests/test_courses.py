import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses', wait_until='networkidle')

    title_element1 = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(title_element1).to_be_visible()
    expect(title_element1).to_have_text('Courses')

    icon_element = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_element).to_be_visible()

    title_element2 = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(title_element2).to_be_visible()
    expect(title_element2).to_have_text('There is no results')

    title_element3 = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(title_element3).to_be_visible()
    expect(title_element3).to_have_text('Results from the load test pipeline will be displayed here')
