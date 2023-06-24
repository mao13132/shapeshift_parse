from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShapeShiftPars:
    def __init__(self, driver, filter_count_day):
        self.driver = driver
        self.url = f'https://forum.shapeshift.com'
        self.source_name = 'ShapeShift'
        self.links_post = []
        self.filter_count_day = filter_count_day

    def load_page(self, url):
        try:
            self.driver.get(url)
            return True
        except Exception as es:
            print(f'Ошибка при заходе на стартовую страницу "{self.source_name}" "{es}"')
            return False

    def __check_load_page(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'sign-up-button')]")))
            return True
        except:
            return False

    def loop_load_page(self):
        count = 0
        count_ower = 10

        while True:

            count += 1

            if count >= count_ower:
                print(f'Не смог открыть {self.source_name}')
                return False

            start_page = self.load_page(self.url)

            if not start_page:
                continue

            check_page = self.__check_load_page()

            if not check_page:
                self.driver.refresh()
                continue

            print(f'Успешно зашёл на {self.source_name}')

            return True

    def get_all_post(self):
        try:
            rows_post = self.driver.find_elements(by=By.XPATH,
                                                  value=f"//table[contains(@class, 'topic-list')]//tr")
        except Exception as es:
            print(f'Ошибка при получение постов"{es}"')
            return False

        return rows_post

    def step_one_parse(self):

        rows_post = self.get_all_post()

        if not rows_post:
            return False

        response = self.itter_rows_post(rows_post)

        print(f'Обнаружил {len(self.links_post)} постов')

        return True

    def start_pars(self):
        result_start_page = self.loop_load_page()

        if not result_start_page:
            return False

        print(f'Успешно зашёл на {self.source_name}')

        response_one_step = self.step_one_parse()
