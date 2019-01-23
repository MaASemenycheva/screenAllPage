from selenium import webdriver
from datetime import datetime
from PIL import Image as image
from PIL import ImageFont, ImageDraw
import os
import random
import time

# [path driver] - путь до папки с драйвером

driver = webdriver.Chrome('''[path driver]''')
driver.maximize_window()
now = datetime.now()
file = open(r"test.txt", "r")
rows = file.read().split('\n')
for row in rows:
	print(row)
	driver.get(row)

	# кнопочки для некоторых сайтов
	#driver.execute_script('return document.getElementsByClassName("item-phone-button")[1].click()')
	#time.sleep(3)
	#driver.execute_script('return document.getElementsByClassName("close")[2].click()')

	total_height = driver.execute_script("return document.body.scrollHeight")
	print("Total height: " + str(total_height))
	client_height = driver.execute_script("return innerHeight")
	print("Client height: " + str(client_height))
	client_width = driver.execute_script("return innerWidth")
	print("Client width: " + str(client_width))

	'''
		Автоматизация задания случайных имен
	'''

	nameImg = ""

	for counterRandName in range(0, 12):
		A = random.randint(0,2)
		if A == 0:
			nameImg += str(random.choice("qwertyuiopasdfghjklzxcvbnm"))
		elif A == 1:
			nameImg += str(random.randint(0,10))
		elif A == 2:
			nameImg += str(random.choice("QWERTYUIOPASDFGHJKLZXCVBNM"))
	#nameImg = str(row.split("_")[-1])
	'''
		Рассчитаем высоту изображения с учетом возможности появления
		фиксированных строк
	'''
	fixedSize = 60
	sizeImgBuild = 0
	count = 0
	sizeImgUnit = total_height/client_height
	#sizeImg = client_height + (client_height - fixedSize)*(sizeImgUnit-1)
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

	while sizeImgBuild < total_height:
		driver.save_screenshot('tmp/{1}_tmp_{0}.png'.format(count, nameImg))
		time_img = image.open('tmp/{1}_tmp_{0}.png'.format(count, nameImg))

		if sizeImgBuild + (client_height - fixedSize) <= total_height:
			if sizeImgBuild >= client_height:
				time_img = time_img.crop((0, fixedSize, client_width, client_height))
				img.paste(time_img, (0, sizeImgBuild))
			else:
				img.paste(time_img, (0, sizeImgBuild))
		else:
			time_img = time_img.crop((0, (sizeImgBuild + (client_height) - total_height), client_width, client_height))
			img.paste(time_img, (0, sizeImgBuild))

		'''
			Временные файлы служат для склеивания из множества изображений в одно
			Так как таких файлов может быть множество, то для немедленного удаления
			их разблокируйте блок ниже
		'''
		#os.remove('tmp/{1}_tmp_{0}.png'.format(count, nameImg))

		if sizeImgBuild < client_height:
			sizeImgBuild += client_height
		else:
			sizeImgBuild += (client_height - fixedSize)

		driver.execute_script("window.scrollBy(0, {0})".format(client_height - fixedSize))
		count += 1

	ImageDraw.Draw(img).text((10, 10), '{0}'.format(row), fill=(255, 0, 0))
	ImageDraw.Draw(img).text((10, 30), '{0}'.format(now.strftime('%d.%m.%Y - %H:%M:%S')), fill=(255, 0, 0))
	img.save("result/{0}.png".format(nameImg))

file.close()
driver.quit()
