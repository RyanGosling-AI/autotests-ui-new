from playwright.sync_api import Page, expect

from Components.views.empty_view_component import EmptyViewComponent
from Components.courses.course_view_component import CourseViewComponent
from pages.base_page import BasePage
from Components.navigation.navbar_component import NavbarComponent
from Components.navigation.sidebar_component import SidebarComponent
from Components.courses.courses_list_toolbar_view_component import CourseListToolbarViewComponent


class CourseListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.empty_view = EmptyViewComponent(page, identifier='courses-list')
        self.course_view = CourseViewComponent(page)
        self.toolbar_view = CourseListToolbarViewComponent(page)
        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)

    def check_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
    )