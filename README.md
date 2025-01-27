# Diploma_ui_api_auto_test

## Дипломная работа по автоматизации тестирования на Python.
## [Тест план лежит здесь.](https://kosstegg-n.yonote.ru/share/2522f7b0-61db-40b3-a396-f5f263b29490)

### Шаги
1. Склонировать проект 'git clone https://github.com/NKosteg/Diploma_ui_api_auto_test.git'
2. Установить зависимости 'pip install -r requirements.txt'
3. Запустить тесты 'python -m pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

### Стек:
 - pytest
 - selenium
 - webdriver manager
 - requests
 - _sqlalchemy_
 - allure
 - configparser
 - json

### Структура:
 - ./test - тесты
 - ./pages - описание страниц
 - ./api - хелперы для работы с API
 - ./db - хелперы для работы с БД
 - ./configuration - провайдер настроек 
   - test_config.ini - настройки для тестов
 - ./testdata - провайдер тестовых данных
   - test_data.json - данные для тестов

### Полезные ссылки:
 - [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
 - [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)
 - [Про configparser](https://docs.python.org/3/library/configparser.html)
 - [Про pip freeze](https://pip.pypa.io/en/latest/cli/pip_freeze/#pip-freeze)
