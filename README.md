# `#screenshotAllPage`

[![Python](https://cdn2.iconfinder.com/data/icons/amazon-aws-stencils/100/SDKs_copy_Python-48.png)](https://www.python.org/)[![JavaScript](https://cdn2.iconfinder.com/data/icons/designer-skills/128/code-programming-javascript-software-develop-command-language-48.png)](https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/JavaScript_basics)[![git](https://cdn1.iconfinder.com/data/icons/iconza-circle-social/64/697061-github-48.png)](https://github.com/tabbols95)

#### Предыстория

Очень часто сталкивался с таким вопросом &quot; Как сделать скриншот html страницы в Python &quot;, &quot; Как сделать скриншот всей страницы в Python &quot; и даже пытался найти ответ на вопрос &quot; Screenshot all page from python &quot;, но поиски не давали упешных результатов и пришлось самостоятельно решать данную проблему. Именно этим и хочу с Вами поделиться.

#### Алгоритм

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

#### О фиксированной строке и имени скрина

Фиксированная строка и имя - одно из последних разработок модуля `screenAllPage`. Множество компания для удобного и быстрого перехода по своим сайтам используют так называемую фиксированную строку.

> Фиксированная строка - это строка, которая при скроллинге всегда видна вверху страницы.

Для активации фиксированной строки необходимо определить `size` этой фиксированной строки на сайте.
![Example_fixedString](https://pp.userapi.com/c849216/v849216725/104a18/9B6z30voY2c.jpg)
И ввести в код `python`:

``` python
fixedSize = 60 #сюда ввести высоту фиксированной строки (с погрешностью на тень в 3 - 5 px)
```

Для удобного сохранения и дальнейшего поиска файлов `\tmp` и `\result` введите в код `python` имя файла:

``` python
nameImg = "Name Image"
```

#### О конвеере

Для потока работы запустим конвеер:

``` python
file = open(r"test.txt", "r")
rows = file.read().split('\n')
for row in rows:
    #тут много всякого различного кода
    # ...
    # ...
    # тут еще много различного кода
file.close()
```

#### О `JavaScript`

Из `JavaScript` нам нужно знать совсем не много:

``` JavaScript
document.body.scrollHeight; // высота страницы
innerHeight // высота клиентского окна
innerWidth // ширина клиентского окна
window.scrollBy(x, y) // передвижение скролл бара
```

#### Последние обновления

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
