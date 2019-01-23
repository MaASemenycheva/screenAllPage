# `#screenshotAllPage`

[![Python](https://cdn2.iconfinder.com/data/icons/amazon-aws-stencils/100/SDKs_copy_Python-48.png)](https://www.python.org/)[![JavaScript](https://cdn2.iconfinder.com/data/icons/designer-skills/128/code-programming-javascript-software-develop-command-language-48.png)](https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/JavaScript_basics)[![git](https://cdn1.iconfinder.com/data/icons/iconza-circle-social/64/697061-github-48.png)](https://github.com/tabbols95)

### Предыстория

Очень часто сталкивался с таким вопросом &quot; Как сделать скриншот html страницы в Python &quot;, &quot; Как сделать скриншот всей страницы в Python &quot; и даже пытался найти ответ на вопрос &quot; Screenshot all page from python &quot;, но поиски не давали упешных результатов и пришлось самостоятельно решать данную проблему. Именно этим и хочу с Вами поделиться.

### Подключаемся к работе

Качаем [python](https://www.python.org/) и библиотеку [Pillow](https://pillow.readthedocs.io/en/5.3.x/installation.html), а конкретно её module Image.

``` sh
pip install Pillow
```

``` python
from PIL import Image as image
```

И конечно же сама библиотека [selenium](https://www.seleniumhq.org/), а точнее её module webdriver

``` sh
pip install selenium
```

``` python
from selenium import webdriver
driver = webdriver.Chrome([path]) # как я уже и упоминал я использую Google Chrome, поэтому драйвер chromedriver, также вы можете использовать geckodtiver для Firefox и прочее
driver.maximize_window()
driver.get("https://habr.com/")
```

### Последние обновления

##### `Date and time`

 * надпись на скриншотах даты и времени.

##### `commit v 1.2.0`

В версии `v 1.2.0` мы

* изобрели генератор имен для файлов;
* проделали большую работу над исправлением массы ошибок;
* мы написали кнопку, но пока не нашли ей применения, поэтому закомментировали, но данная кнопка сможет открывать мобильные номера на [avito](https://www.avito.ru/).

>Сегодня 16.01.2019 мы запустили аж целых 2 нормальных `commits`:

`commit conveyor`

* конвеер способствует построению множества скринов за один запуск программы;
* ну и затестили файлом `test.txt`

`commit Update fixed string`
* скриншот страницы с фиксированной строкой;
* упрощенный вариант задания имен скриншота;
* примеры скриншотов сайтов [habr](https://habr.com/), [avito](https://www.avito.ru/), [progLib](https://proglib.io/) с сохранением временных файлов.

#### От автора

Подключившись к работе наслаждаемся, дописываем, переписываем, ждем обновлений.
