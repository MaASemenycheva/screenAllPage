from selenium import webdriver
from PIL import Image as image

driver = webdriver.Chrome("C:/Users/tabbo/OneDrive/Документы/drivers/chromedriver.exe")
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
while i < total_height:
	driver.save_screenshot('screen{0}.png'.format(count))

	time_img = image.open('screen{0}.png'.format(count))
	img.paste(time_img, (0, i))

	i += client_height
	driver.execute_script("window.scrollBy(0, {0})".format(client_height))
	count += 1

img.save("image.png")

driver.quit()