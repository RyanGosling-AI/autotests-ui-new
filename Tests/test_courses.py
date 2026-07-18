import pytest
from playwright.sync_api import expect
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CourseListPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses',
                                  wait_until='networkidle')

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


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(course_list_page: CourseListPage, create_course_page: CreateCoursePage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.check_visible_create_course_title()
    create_course_page.check_visible_create_course_button()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_empty_view_preview()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(
        title="",
        description="",
        estimated_time="",
        max_score="0",
        min_score="0"
    )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image('./testdata/files/image.png')
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_course_page.click_create_course_button()
    course_list_page.check_courses_title()
    course_list_page.check_visible_create_course_button()
    course_list_page.check_course_card(
        index=0,
        title="Playwright",
        estimated_time="2 weeks",
        max_score="100",
        min_score="10"
    )