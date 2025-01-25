# Diploma_ui_api_auto_test

## Дипломная работа по автоматизации тестирования на Python.

### Шаги
1. Склонировать проект 'git clone https://github.com/NKosteg/Diploma_ui_api_auto_test.git'
2. Установить зависимости
3. Запустить тесты командой 'python -m pytest'
4. Сгенерировать отчет командой 'allure generate allure-files -o allure-report'

### Стек:
 - pytest
 - selenium
 - requests
 - _sqlalchemy_
 - allure
 - config

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

### Библиотеки (!):
 - pip install pytest
 - pip install selenium
 - pip install webdriver-manager
 - pip install allure-pytest
 - pip install requests
