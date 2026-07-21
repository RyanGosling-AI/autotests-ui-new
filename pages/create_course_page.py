from playwright.sync_api import Page, expect

from Components.views.empty_view_component import EmptyViewComponent
from Components.views.image_upload_widget_component import ImageUploadWidgetComponent
from Components.courses.create_course_exercise_form_component import CreateExerciseFormComponent
from Components.courses.create_course_form_component import CreateCourseFormComponent
from Components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from Components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_exercise_toolbar = CreateCourseExercisesToolbarViewComponent(page)
        self.create_course_toolbar = CreateCourseToolbarViewComponent(page)
        self.create_course_description = CreateCourseFormComponent(page)
        self.image_upload_widget = ImageUploadWidgetComponent(page, identifier='create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page, identifier='create-course-exercises')
        self.create_course_form = CreateExerciseFormComponent(page)

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )