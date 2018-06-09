from splinter import Browser
import time
import urllib
import re
import json
import requests
#------------------------------------ GLOBAL -----------------------------------------------------#
browser = Browser('chrome')
url = "http://www.worksfromhome.in"
browser.visit(url)


#------------------------------------------------------- LOGIN -----------------------------------------#

browser.find_by_id("txt_Uname").fill("C230520184025")     # Enter the Users name
browser.find_by_id("txt_pass").fill("bharathi123*")             # entering the password
browser.find_by_id("btnsubmit").click()

#------------------------------------------------ LOGED IN ----------------------------------------------#


#------------------------------------------------- FORM FILLING ------------------------------------------#
no_box = browser.find_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_drp_pagejump"]/option')
print "#----------------------START HERE -----------------------------------#"
print "#------------------ INFORMATION ON THE PAGE ARE : -----------------#"
print "THE LENGTH OF THE TOTAL PAGES ARE: "
print len(no_box)
id = 1181
while id <= 2199 and id >= 0:
    no_box = browser.find_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_drp_pagejump"]/option')
    no_box[id].click()
    browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail").click()
    if str(browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_tbc")['value']) == "":
        print "This page is empty" + str(id + 1)
        f = open("nonfilled.txt", "a")
        f.write("THIS IS THE PAGE TO BE FILLED: " + str(id+1))
        f.write("\n")
    else:
        print " The PAGE IS FULL ENJOY MY DEAR AND PAGE NO IS : " + str(id+1)
    id = id + 1