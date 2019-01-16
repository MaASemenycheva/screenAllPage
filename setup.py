from selenium import webdriver
from PIL import Image as image
import os

# [path driver] - путь до папки с драйвером
# [site] - сайт, для которого необходимо сделать скриншот

driver = webdriver.Chrome("C:/drivers/chromedriver.exe")
driver.maximize_window()
file = open(r"test.txt", "r")
rows = file.read().split('\n')
for row in rows:
	print(row)
	driver.get(row)

	total_height = driver.execute_script("return document.body.scrollHeight")
	print("Total height: " + str(total_height))
	client_height = driver.execute_script("return innerHeight")
	print("Client height: " + str(client_height))
	client_width = driver.execute_script("return innerWidth")
	print("Client width: " + str(client_width))

	i, count = 0, 0
	nameImg = str(row.split("_")[-1])
	'''
	Для сайтов с фиксированым меню рассчитаем размеры изображения
	'''
	fixedSize = 60
	sizeImg = total_height/client_height
	if int(sizeImg) < sizeImg:
		sizeImg = int(sizeImg)
	else:
		sizeImg = int(sizeImg)

	img = image.new("RGB", (client_width, total_height - (fixedSize*(sizeImg-1))))

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
		driver.save_screenshot('tmp/{1}_tmp_{0}.png'.format(count, nameImg))
		time_img = image.open('tmp/{1}_tmp_{0}.png'.format(count, nameImg))

		if (count + 1) * client_height < total_height:
			if count > 0:
				time_img = time_img.crop((0, fixedSize, client_width, client_height))
				img.paste(time_img, (0, i))
			else:
				img.paste(time_img, (0, i))

		else:
			area = (0, (count + 1) * client_height - total_height - (fixedSize*(sizeImg-1)), client_width, client_height)
			time_img = time_img.crop(area)
			img.paste(time_img, (0, i))

		#os.remove('tmp/{1}_tmp_{0}.png'.format(count, nameImg))

		i += client_height - fixedSize

		driver.execute_script("window.scrollBy(0, {0})".format(client_height - fixedSize))
		count += 1

	img.save("result/{0}.png".format(nameImg))

file.close()
driver.quit()
