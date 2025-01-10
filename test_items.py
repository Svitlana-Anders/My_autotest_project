import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: '--language=en' or '--language=ru'")


@pytest.fixture(scope="function")
def browser(request):
    # Получение языка из командной строки
    user_language = request.config.getoption("language")

    # Настройка опций браузера
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # Запуск браузера с опциями
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)

    # Возврат браузера для тестов
    yield browser

    # Закрытие браузера после выполнения теста
    print("\nquit browser..")
    browser.quit()