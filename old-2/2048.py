#!/usr/bin/env python3.46
# programa para o jogo 2048

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser= webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('html')
x=0
while x<190:
	htmlElem.send_keys(Keys.UP)
	htmlElem.send_keys(Keys.RIGHT)
	htmlElem.send_keys(Keys.DOWN)
	htmlElem.send_keys(Keys.LEFT)
	x+=1
