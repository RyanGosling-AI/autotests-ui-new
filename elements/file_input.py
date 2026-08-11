from elements.base_element import BaseElement
import allure
from tools.playwright.logger import get_logger

logger = get_logger("FILE_INPUT")


class FileInput(BaseElement):
    @property
    def type_off(self) -> str:
        return 'file Input'

    def set_input_files(self, file: str, nth: int = 0, **kwargs):
        step = f'Set file {file} to the {self.type_off} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.set_input_files(file)
