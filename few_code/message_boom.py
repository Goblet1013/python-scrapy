from selenium import webdriver
import time

html_1='https://passport2.eastmoney.com/pub/login?backurl=http%3A//stock.eastmoney.com/'
#############################
driver = webdriver.Chrome()
driver.get(html_1)#获取大量网站验证码输入界面
driver.switch_to_frame('frame_login')#输入框为一嵌套网页框架，需转入该框架
driver.find_element_by_xpath("/html/body/div[1]/div[1]/span[2]").click()
#time.sleep(1)
driver.find_element_by_id('txt_mobile').send_keys('13012436861')
#防刷措施
#driver.find_element_by_id('btn_getvcode').click()
