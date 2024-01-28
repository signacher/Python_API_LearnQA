<table width="100%" border='0'>
 <tr><td width="30%" valign="bottom"><img src="https://github.com/signacher/signacher/blob/main/images/learnqa.png" title="api" alt="api" width="200" height="200"/></td><td valign="middle">
 <h2>Демо проект по автоматизации тестирования API  <a target="_blank" href="https://playground.learnqa.ru/api/map"> playground.learnqa.ru/api<a></h2>
 </td></tr>
</table>

<h3>Проект создан в рамках обучения на курсе <a target="_blank" href="https://www.learnqa.ru/python_api"> Автоматизация тестирования REST API на Python.</a></h3>

## :open_book: Содержание:
- [Описание проекта](#heavy_check_mark-описание)
- [Технологии и инструменты](#gear-технологии-и-инструменты)
- [Реализованные проверки](#ballot_box_with_check-реализованные-проверки)
- [Как запускать тесты](#on-как-запускать-тесты)
- [Allure отчет](#bar_chart-allure-отчет-о-прохождении-тестов)
  
## :heavy_check_mark: Описание:
>В этом репозитории:
>- Демо-проект с примерами автотестов API, написанных на языке <code>Python</code> с помощью библиотеки <code>Requests</code>.
>- Ссылка на API <a target="_blank" href="https://playground.learnqa.ru/api/map"> https://playground.learnqa.ru/api/map/api<a>
>- Тесты можно запускать в Docker контейнере.
>- Лог прохождения тестов пишется а файлы в папке <code>logs</code>
>- После окончания тестов можно сформировать allure отчет.

## :gear: Технологии и инструменты:
<div align="center">
  <img src="https://github.com/signacher/signacher/blob/main/images/python.png" title="Python" alt="Python" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/pycharm.png" title="Pycharm" alt="Pycharm" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/pytest.png" title="Pytest" alt="Pytest" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/requests.png" title="Requests" alt="Requests" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/github.png" title="GitHub" alt="GitHub" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/docker.png" title="Docker" alt="Docker" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/yaml.png" title="yaml" alt="yaml" width="40" height="40"/>&nbsp;
  <img src="https://github.com/signacher/signacher/blob/main/images/allure.png" title="Allure" alt="Allure" width="40" height="40"/>&nbsp;
</div>

## :ballot_box_with_check: Реализованные проверки:
- [x] Авторизация зарегистрированного пользователя
- [x] Авторизация пользователя(параметризованный тест)
>-   без токена
>-   без cookie      
- [x] Создание нового пользователя с уже зарегистрированным email`ом
- [x] Создание нового пользователя
- [x] Просмотр данных пользователя
- [x] Редактирование данных пользователя
- [x] Удаление пользователя

## :on: Как запускать тесты:

>Запуск тестов в докер контейнере
```bash
docker-compose up --build
```

>Команды для установки переменной окружения ENV чтобы выбрать окружение перед запуском тестов (по умолчанию установлен dev)

<code>set ENV=dev</code>  Тесты запускаются на https://playground.learnqa.ru/api_dev

<code>set ENV=prod</code> Тесты запускаются на https://playground.learnqa.ru/api
<br/><br/>
>Запуск из командной строки с формированием результатов отчета
```bash
python -m pytest --alluredir=test_rusult
```
## :bar_chart: Allure отчет о прохождении тестов

> для формирования отчета ввести в командной строке: 
```bash
allure serve .\allure-results
```

*Главная страница Allure-отчета содержит следующие информационные блоки:*

> - [x] <code><strong>*ALLURE REPORT*</strong></code> - отображается дату и время прохождения теста, общее количество тест кейсов, а также диаграмма с указанием процента и количества успешных, упавших и сломавшихся в процессе выполнения тестов
>- [x] <code><strong>*TREND*</strong></code> - отображает тренд прохождения тестов от сборки к сборке
>- [x] <code><strong>*SUITES*</strong></code> - отображает распределение результатов тестов по тестовым наборам
>- [x] <code><strong>*CATEGORIES*</strong></code> - отображает распределение неуспешно прошедших тестов по видам дефектов
>- [x] <code><strong>*ENVIRONMENT*</strong></code> - отображает тестовое окружение, на котором запускались тесты 
>- [x] <code><strong>*FEATURES BY STORIES*</strong></code> - отображает распределение тестов по функционалу, который они проверяют

##### Пример отчета
![Screen Allure3](images/allurereport3.png)
