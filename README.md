# ScreenshotAllPage

[![Python](https://cdn2.iconfinder.com/data/icons/amazon-aws-stencils/100/SDKs_copy_Python-48.png)](https://www.python.org/)[![JavaScript](https://cdn2.iconfinder.com/data/icons/designer-skills/128/code-programming-javascript-software-develop-command-language-48.png)](https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/JavaScript_basics)[![git](https://cdn1.iconfinder.com/data/icons/iconza-circle-social/64/697061-github-48.png)](https://github.com/tabbols95)

### Предыстория

Очень часто сталкивался с таким вопросом &quot; Как сделать скриншот html страницы в Python &quot;, &quot; Как сделать скриншот всей страницы в Python &quot; и даже пытался найти ответ на вопрос &quot; Screenshot all page from python &quot;, но поиски не давали упешных результатов и пришлось самостоятельно решать данную проблему. Именно этим и хочу с Вами поделиться.

### Алгоритм

Отвечаем на вопрос:

> &quot; Как сделать скриншот всей html страницы в python? &quot;

Как ни странно, но ответ на данный вопрос очень прост. Заранее оговорюсь, что работать мы будем в тестовом режиме, т.е. используя библиотеку [selenium](https://www.seleniumhq.org/), и драйвер [chromedriver](http://chromedriver.chromium.org/).
1. С помощью драйвера загружаем сайт, для которого необходимо сделать скриншот;
2. Используя `JavaScript` высчитываем ширину, высоту клиентского окна и высоту всей `html` страницы (Я подразумеваю, что ширина моей страницы не выходит за рамки клиентского окна);
3. Объявляем новый обект `img` для дальнейшего построения в нем нашего скриншота;
4. Используя `JavaScript` делаем прокрутку страницы на высоту клиентского окна и скриним каждый шаг, параллельно склеивая изображения в созданном объекте `img`.

#### Подключаемся к работе

Как мы можем обратить внимание, алгоритм довольно таки прост. Теперь поговорим о том, что мы будем использовать.
Логично, что так как программа написана на [python](https://www.python.org/), то нам необходимо скачать его самого.
Для построения объекта img нам понадобится библиотека [Pillow](https://pillow.readthedocs.io/en/5.3.x/installation.html), а конкретно её module Image.

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

### О `JavaScript`

Из `JavaScript` нам нужно знать совсем не много:

``` JavaScript
document.body.scrollHeight; // высота страницы
innerHeight // высота клиентского окна
innerWidth // ширина клиентского окна
window.scrollBy(x, y) // передвижение скролл бара
```

### Последние обновления

`v 1.0.1`
* Проработаны исключительные ситуации;
* Папка временных файлов `/tmp`, папка с результатом `/result`;
* Исправлена ошибка приклеивания последнего изображения;
* Приведен пример скриншота сайта [habr](https://habr.com/).

### От автора

Подключившись к работе наслаждаемся, дописываем, переписываем, ждем обновлений.
