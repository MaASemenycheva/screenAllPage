from selenium import webdriver
from PIL import Image as image
import os

# [path driver] - путь до папки с драйвером
# [site] - сайт, для которого необходимо сделать скриншот

driver = webdriver.Chrome("C:/drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://habr.com/")

total_height = driver.execute_script("return document.body.scrollHeight")
print("Total height: " + str(total_height))
client_height = driver.execute_script("return innerHeight")
print("Client height: " + str(client_height))
client_width = driver.execute_script("return innerWidth")
print("Client width: " + str(client_width))

i, count = 0, 0
img = image.new("RGB", (client_width, total_height))

# создаем папку /tmp (временных файлов) если она отсутствует
try:
	os.mkdir('tmp')
	print('New folder /tmp')
except FileExistsError:
	print('Folder /tmp exists')

# создаем папку /result (готовые скрины) если она отсутствует
try:
	os.mkdir('result')
	print('New folder /result')
except FileExistsError:
	print('Folder /result exists')

while i < total_height:
	driver.save_screenshot('tmp/screen{0}.png'.format(count))
	time_img = image.open('tmp/screen{0}.png'.format(count))

	if (count + 1) * client_height < total_height:
		img.paste(time_img, (0, i))
	else:
		area = (0, (count + 1) * client_height - total_height, client_width, client_height)
		time_img = time_img.crop(area)
		img.paste(time_img, (0, i))

	os.remove('tmp/screen{0}.png'.format(count))

	i += client_height

	driver.execute_script("window.scrollBy(0, {0})".format(client_height))
	count += 1

img.save("result/image.png")

driver.quit()
