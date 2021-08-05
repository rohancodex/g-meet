# import required modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
import time
from webdriver_manager.chrome import ChromeDriverManager

from tkinter import *


def run(url):
	#login to meet
	def Glogin(mail_address, password):
		# Login Page
		driver.get(
			'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

		# input Gmail
		driver.find_element_by_id("identifierId").send_keys(mail_address)
		driver.find_element_by_id("identifierNext").click()
		driver.implicitly_wait(10)

		# input Password
		driver.find_element_by_xpath(
			'//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
		driver.implicitly_wait(10)
		driver.find_element_by_id("passwordNext").click()
		driver.implicitly_wait(10)

		# go to google home page
		
		driver.get('https://google.com/')
		driver.implicitly_wait(1000)


	def turnOffMicCam():
		# turn off Microphone
		time.sleep(1)
		button = driver.find_elements_by_css_selector(
			'div.U26fgb.JRY2Pb.mUbCce.kpROve.yBiuPb.y1zVCf.M9Bg4d')
		button[0].click()
		time.sleep(1)
		button[1].click()
		driver.implicitly_wait(1000)

		# turn off camera
		# time.sleep(1)
		# driver.find_element_by_css_selector(
		#     'div.U26fgb.JRY2Pb.mUbCce.kpROve.yBiuPb.y1zVCf.M9Bg4d.FTMc0c.N2RpBe.jY9Dbb').click()
		# driver.implicitly_wait(1000)


	def leaveMeet():
		# leave meetings
		time.sleep(30)
		driver.find_element_by_css_selector(
			'button.VfPpkd-Bz112c-LgbsSe.yHy1rc.eT1oJ.tWDL4c.jh0Tpd.Gt6sbf.QQrMi.ftJPW').click()


	def joinNow():
		# Join meet
		print(1)
		time.sleep(5)
		driver.implicitly_wait(1000)
		driver.find_element_by_css_selector(
			'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()

		print(1)


	def AskToJoin():
		# Ask to Join meet
		time.sleep(1)
		driver.implicitly_wait(2000)
		driver.find_element_by_css_selector(
			'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    # Ask to join and join now buttons have same xpaths
	# Ask to join and join now buttons have same xpaths
	# assign email id and password
	mail_address = 'desairohan2000@gmail.com'
	password = 'password@2017'
	# create chrome instance
	opt = Options()
	opt.add_argument('--disable-blink-features=AutomationControlled')
	opt.add_argument('--start-maximized')
	opt.add_experimental_option("prefs", {
			"profile.default_content_setting_values.media_stream_mic": 1,
			"profile.default_content_setting_values.media_stream_camera": 1,
			"profile.default_content_setting_values.geolocation": 0,
			"profile.default_content_setting_values.notifications": 1
		})
	opt.add_argument("user-data-dir=C:\\Users\\desai\\AppData\\Local\\Google\\Chrome\\User%Data") 
	# driver = webdriver.Chrome(options=opt)
	driver = webdriver.Chrome(ChromeDriverManager().install(),options=opt)
	# # login to Google account
	# Glogin(mail_address, password)
	# go to google meet
	driver.get('https://google.com/')
	driver.get(url)
	turnOffMicCam()
	# AskToJoin()
	joinNow()
	leaveMeet()




root = Tk()
# root.geometry("300x300")

width = 400
height=100
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(
    f'{width}x{height}+{int((screen_width/2)-(width/2))}+{int((screen_height/2)-(height/2))}')
root.title("G-meet Bot")


def Take_input():
	INPUT = inputtxt.get("1.0", "end-1c")
	url = INPUT
	run(url)
		
l = Label(text = "Enter Google meet url")
inputtxt = Text(root, height = 2,
				width = 40,
				bg = "light yellow",
				)

# Output = Text(root, height = 5,
# 			width = 10,
# 			bg = "light cyan")

Display = Button(root, height = 2,
				width = 10,
				text ="Run",
				command = lambda:Take_input())

l.pack()
inputtxt.pack()
Display.pack()
# Output.pack()
mainloop()
