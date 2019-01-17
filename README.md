# `#screenshotAllPage`

[![Python](https://cdn2.iconfinder.com/data/icons/amazon-aws-stencils/100/SDKs_copy_Python-48.png)](https://www.python.org/)[![JavaScript](https://cdn2.iconfinder.com/data/icons/designer-skills/128/code-programming-javascript-software-develop-command-language-48.png)](https://developer.mozilla.org/ru/docs/Learn/Getting_started_with_the_web/JavaScript_basics)[![git](https://cdn1.iconfinder.com/data/icons/iconza-circle-social/64/697061-github-48.png)](https://github.com/tabbols95)

### Предыстория

Очень часто сталкивался с таким вопросом &quot; Как сделать скриншот html страницы в Python &quot;, &quot; Как сделать скриншот всей страницы в Python &quot; и даже пытался найти ответ на вопрос &quot; Screenshot all html page from python &quot;, но поиски не давали упешных результатов и пришлось самостоятельно решать данную проблему. Именно этим и хочу с Вами поделиться.

### Подключаемся к работе

Качаем [python](https://www.python.org/).
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

### О фиксированной строке и имени скрина

Фиксированная строка и имя - одно из последних разработок модуля `screenAllPage`. Множество компаний для удобного и быстрого перехода по своим сайтам используют так называемую фиксированную строку (&quot; Это действительно удобно &quot;).

> Фиксированная строка - это строка, которая при скроллинге всегда видна вверху страницы.

![Example_fixedString](https://pp.userapi.com/c849216/v849216725/104a18/9B6z30voY2c.jpg)

Для удобного сохранения и дальнейшего поиска файлов `\tmp` и `\result`  `python` сам генерирует для себя имя файла из 16 символов (&quot; В них входят заглавные и строчные буквы и цифры &quot;):

``` python
for counterRandName in range(0, 12):
	A = random.randint(0,2)
	if A == 0:
		nameImg += str(random.choice("qwertyuiopasdfghjklzxcvbnm"))
	elif A == 1:
	    nameImg += str(random.randint(0,10))
	elif A == 2:
		nameImg += str(random.choice("QWERTYUIOPASDFGHJKLZXCVBNM"))
```

### О конвеере

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

### О `JavaScript`

Из `JavaScript` нам нужно знать совсем не много:

``` JavaScript
document.body.scrollHeight; // высота страницы
innerHeight // высота клиентского окна
innerWidth // ширина клиентского окна
window.scrollBy(x, y) // передвижение скролл бара
```

### Последние обновления

##### `commit v 1.2.0`

В версии `v 1.2.0` мы

* изобрели генератор имен для файлов;
* проделали большую работу над исправлением массы ошибок;
* мы написали кнопку, но пока не нашли ей применения, поэтому закомментировали, но данная кнопка сможет открывать мобильные номера на [avito](https://www.avito.ru/).

>Сегодня 16.01.2019 мы запустили аж целых 2 нормальных `commits`:

##### `commit conveyor`

* конвеер способствует построению множества скринов за один запуск программы;
* ну и затестили файлом `test.txt`

##### `commit Update fixed string`
* скриншот страницы с фиксированной строкой;
* упрощенный вариант задания имен скриншота;
* примеры скриншотов сайтов [habr](https://habr.com/), [avito](https://www.avito.ru/), [progLib](https://proglib.io/) с сохранением временных файлов.

### От автора

Подключившись к работе наслаждаемся, дописываем, переписываем, ждем обновлений.
