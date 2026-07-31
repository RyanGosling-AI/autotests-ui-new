from elements.base_element import BaseElement
import allure


class FileInput(BaseElement):
    @property
    def type_off(self) -> str:
        return 'file Input'

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        with allure.step(f'Set file {file} to the {self.type_off} "{self.name}"'):
            locator = self.get_locator(nth, **kwargs)
            locator.set_input_files(file)