from browser.createbrowser import CreatBrowser
from browser.src.shapeshift_pars import ShapeShiftPars


def main():
    filter_count_day = 5

    browser_core = CreatBrowser()

    print(f'Парсер запущен. Захожу на сайт')

    response_job = ShapeShiftPars(browser_core.driver, filter_count_day).start_pars()

    print(f'Работу закончил. Сохранил \n{response_job}.xlsx\n{response_job}.json')


if __name__ == '__main__':
    main()
