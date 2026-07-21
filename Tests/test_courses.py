import pytest
from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CourseListPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(course_list_page: CourseListPage):
    course_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    course_list_page.navbar.check_visible(username='username')
    course_list_page.sidebar.check_visible()
    course_list_page.toolbar_view.check_visible()
    course_list_page.check_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(course_list_page: CourseListPage, create_course_page: CreateCoursePage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
    create_course_page.create_course_description.check_visible_create_course_form(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0"
    )
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
    create_course_page.create_course_description.fill_create_course_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_course_page.create_course_toolbar.click_create_course_button()

    course_list_page.toolbar_view.check_visible()
    course_list_page.course_view.check_visible(
        index=0,
        title="Playwright",
        estimated_time="2 weeks",
        max_score="100",
        min_score="10"
    )