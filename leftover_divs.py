from PIL import Image
import pytesseract
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
browser.find_by_id("btnsubmit").click()                     # submit to login

#------------------------------------------------ LOGED IN ----------------------------------------------#


#------------------------------------------------- FORM FILLING ------------------------------------------#
no_box = browser.find_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_drp_pagejump"]/option')
print "#----------------------START HERE -----------------------------------#"

tic = time.clock()
print "#------------------ INFORMATION ON THE PAGE ARE : -----------------#"
print "THE LENGTH OF THE TOTAL PAGES ARE: "
print len(no_box)
i = 0
box = ['471', '621', '793', '918', '952', '955', '985', '986', '1053', '1084', '1113', '1137', '1153', '1292',
           '1346', '1358', '1523', '1525', '1557', '1610', '1669', '1678', '1683', '1718', '1829', '1845', '1862',
           '1876', '1881', '1898', '1910', '1911', '1970', '1975', '2020', '2042', '2093', '2102', '2124', '2199',
           '2200']
print(i)
while i <len(box):
    print i
    a = int(box[i])
    id = a-1
    print id
    while id <= 2197 and id >= 2092:
        no_box = browser.find_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_drp_pagejump"]/option')

        no_box[id].click()
        time.sleep(1)

        # ------------------------------------------------ PRINTING THE IMAGE URL FOR DOWNLOAD ----------------------------------------------#
        image_url = browser.find_by_id('ctl00_ContentPlaceHolder1_MainImg')['src']

        # ----------------------------------------- SAVING IMAGE VIA URLLIB --------------------------------#
        urllib.urlretrieve(image_url, "locol1.png")
        # -------------------------------------------- IMAGE SAVED AS (loco.png) -----------------------------#

        # ----------------------------------------- PYTESSRACT OCR -------------------------------------------#
        def ocr_space_file(filename, overlay=True, api_key='4474728a7888957', language='eng'):

            payload = {'isOverlayRequired': overlay,
                       'apikey': api_key,
                       'language': language,
                       }
            with open(filename, 'rb') as f:
                r = requests.post('https://api.ocr.space/parse/image',
                                  files={filename: f},
                                  data=payload,
                                  )
            return r.content.decode()


        test_file = ocr_space_file(filename='locol1.png', language='eng')

        b = json.loads(test_file)
        c = b["ParsedResults"][0]["ParsedText"]

        # -------------------------------------- TEXT COVERTERD BY THE OCR --------------------------------------#
        out = c.split("*")
        print "THE LENGTH OF OUT IS AFTER SEP OF * : "
        print len(out)
        final1 = []
        for items in out:
            final1.append(re.sub('\n', '', items))
        final = []
        for items in final1:
            final.append(re.sub('\r', '', items))
        # print final
        time.sleep(1)
        print "THE CURRENT PAGE IS"
        print id +1
        toc = time.clock()
        c = tic - toc
        print("THE TIME TAKEN TO COLLECT ALL THE INFORMATION IS : ")
        print c
        print "#----------------------------------THE FORM FILLING STARET FROM HERE--------------------------------#"
        tic = time.clock()

        # -------------------------------------------# SECTION ONE (7) -------------------------------------------#
        try:
            browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail").click()
            time.sleep(1)
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_tbc").fill(final[0].strip())
            time.sleep(1)# first name
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_name").fill(final[1].strip())
            time.sleep(1)# last name
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_email").fill(final[2].strip())
            time.sleep(1)# email
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_mobno").fill(final[3].strip())
            time.sleep(1)# mobile number
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_gender").fill(final[4].strip())
            time.sleep(1)# gender
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_licenceno").fill(final[5].split('\\')[0].strip())
            time.sleep(1)# licence number
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabPersonalDetail_txt_girno").fill(final[6].strip())  # grid number
            time.sleep(1)

            # ------------------------------------------- SECTION ONE END -------------------------------------------#

            # ------------------------------------------- SECTION TWO START (7) -------------------------------------#

            browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail").click()
            time.sleep(1)
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_panno").fill(final[7].strip())
            time.sleep(1)# pan number
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_HState").fill(final[8].strip())
            time.sleep(1)# state
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Hcity").fill(final[9].strip())
            time.sleep(1)# city
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Hpin").fill(final[10].strip())
            time.sleep(1)# pin
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Hadd").fill(final[11].strip())
            time.sleep(1)# address
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Oadd").fill(final[12].strip())
            time.sleep(1)# address
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabProviderDetail_txt_Ocity").fill(final[13].strip())# city
            time.sleep(1)
            # ------------------------------------------- SECTION TWO END ----------------------------------------------#

            # -------------------------------------------##### SECTION THREE START (6) ----------------------------------#
            browser.find_by_id("__tab_ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail").click()
            time.sleep(1)
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_Opincode").fill(final[14].strip())
            time.sleep(1)# pincode
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_loanapproval").fill(final[15].strip())
            time.sleep(1)# loan approval
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_menno").fill(final[16].strip())
            time.sleep(1)# men number
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_af").fill(final[17].strip())
            time.sleep(1)# af
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_nri").fill(final[18].strip())
            time.sleep(1)# nri
            browser.find_by_id("ctl00_ContentPlaceHolder1_tabForm_tabTransactionDetail_txt_cp").fill(final[19].strip())
            time.sleep(1)# cpi
            time.sleep(1)
            # ------------------------------------------------- SECTION THREE END -------------------------------------------#

            # ------------------------------------------------ SUBMISION ON END -------------------------------------------#

            browser.find_by_id("ctl00_ContentPlaceHolder1_btnsubmit").click()  # submit
            toc = time.clock()
            a = tic - toc
            print
            print ("THE TIME TAKEN TO COMPLETE THE FORM IS : ")
            print(a)
            print "#------------------------ PAGE COMPLETED SUCESSFULL--------------------------#"
            time.sleep(1)
        except:
            f = open("erreorlog_div.txt", "a")
            f.write(str(id+1))
            f.write("\n")
            f.close()
            continue
        break
    i = i + 1
    #------------------------------------------- SUBMIT END -------------------------------------------#


#---------------------------------------- FORM FILLING END -------------------------------------------#



#------------------------------------------ LOGOUT -----------------------------#

# browser.find_by_id("ctl00_lnklogout").click()

#----------------------------------------- DONE ---------------------------------#

