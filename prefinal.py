# -*- coding: utf-8 -*-
import os
import re
import time
import urllib
from AbbyyOnlineSdk import *
from splinter import Browser

processor = None


def setup_processor():
    processor.ApplicationId = "oneocrtext"
    processor.Password = "Fy7cgwlQe6ICdgE6SQpa/EOM"

    # Proxy settings
    if "http_proxy" in os.environ:
        proxy_string = os.environ["http_proxy"]
        print("Using http proxy at {}".format(proxy_string))
        processor.Proxies["http"] = proxy_string

    if "https_proxy" in os.environ:
        proxy_string = os.environ["https_proxy"]
        print("Using https proxy at {}".format(proxy_string))
        processor.Proxies["https"] = proxy_string


# Recognize a file at filePath and save result to resultFilePath
def recognize_file(file_path, result_file_path, language, output_format):
    print("Uploading..")
    settings = ProcessingSettings()
    settings.Language = language
    settings.OutputFormat = output_format
    task = processor.process_image(file_path, settings)
    if task is None:
        print("Error")
        return
    if task.Status == "NotEnoughCredits":
        print("Not enough credits to process the document. Please add more pages to your application's account.")
        return

    print("Id = {}".format(task.Id))
    print("Status = {}".format(task.Status))
    print("Waiting..")

    while task.is_active():
        time.sleep(5)
        print(".")
        task = processor.get_task_status(task)

    print("Status = {}".format(task.Status))

    if task.Status == "Completed":
        if task.DownloadUrl is not None:
            processor.download_result(task, result_file_path)
            print("Result was written to {}".format(result_file_path))
    else:
        print("Error processing task")


def main():
    global processor

    # ------------------------------------ GLOBAL -----------------------------------------------------#
    browser = Browser('chrome')
    url = "https://goo.gl/gTWejF"
    browser.visit(url)

    # ------------------------------------------------------- LOGIN -----------------------------------------#

    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_Uname").fill("")  # Enter the Users name
    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_pass").fill("")  # entering the password
    browser.find_by_id("ctl00_ContentPlaceHolder1_btnsubmit").click()  # submit to login

    # ------------------------------------------------ LOGED IN ----------------------------------------------#

    # ------------------------------------------------- FORM FILLING ------------------------------------------#
    no_box = browser.find_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_drp_pagejump"]/option')
    print "#----------------------START HERE -----------------------------------#"

    tic = time.clock()
    print "#------------------ INFORMATION ON THE PAGE ARE : -----------------#"
    print "THE LENGTH OF THE TOTAL PAGES ARE: "
    print len(no_box)
    id = 0

    while 0 <= id <= 1050:

        no_box = browser.find_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_drp_pagejump"]/option')

        no_box[id].click()
        time.sleep(1)

        # ------------------------------------------------ PRINTING THE IMAGE URL FOR DOWNLOAD ----------------------------------------------#
        image_url = browser.find_by_id('ctl00_ContentPlaceHolder1_MainImg')['src']

        # ----------------------------------------- SAVING IMAGE VIA URLLIB --------------------------------#
        urllib.urlretrieve(image_url, "locol1.png")
        # -------------------------------------------- IMAGE SAVED AS (loco.png) -----------------------------#

        processor = AbbyyOnlineSdk()

        setup_processor()

        source_file = 'locol1.png'
        target_file = 'result.txt'
        language = 'English'
        output_format = 'txt'

        if os.path.isfile(source_file):
            recognize_file(source_file, target_file, language, output_format)
        else:
            print("No such file: {}".format(source_file))

        with open('result.txt', 'r') as res:
            text = res.readlines()
        # print text
        lin_cnt = text.count("\n")
        print lin_cnt
        a = ''
        num_lines = sum(1 for line in open('result.txt'))
        print num_lines
        if num_lines == 3:
            for k in range(0, num_lines):
                a = a + text[k]
            b = a.decode('unicode_escape').encode('ascii', 'ignore')
            c = str(b).split("-")
            final = []
            for items in c:
                final.append(re.sub('       ', '', items))
            time.sleep(1)
            print final
            print len(final)
            final1 = []
            for items in final:
                final1.append(re.sub('\n', '', items))
            time.sleep(1)
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_tbc").fill(final1[0].strip())
            time.sleep(1)  # first name
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_name").fill(final1[1].strip())
            time.sleep(1)  # last name
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_email").fill(final1[2].strip())
            time.sleep(1)  # email
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_mobno").fill(final1[3].strip())
            time.sleep(1)  # mobile number
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_gender").fill(final1[4].strip())
            time.sleep(1)  # gender
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_licenceno").fill(final1[5].strip())
            time.sleep(1)  # licence number
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_girno").fill(final1[6].strip())  # grid number
            time.sleep(1)
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_panno").fill(final1[7].strip())
            time.sleep(1)  # pan number
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_Hadd").fill(final1[8].strip())
            time.sleep(1)  # state
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_Hcity").fill(final1[9].strip())
            time.sleep(1)  # city
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_Hpin").fill(final1[10].strip())
            time.sleep(1)  # pin
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_HState").fill(final1[11].strip())
            time.sleep(1)  # address
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_Oadd").fill(final1[12].strip())
            time.sleep(1)  # address
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_Ocity").fill(final1[13].strip())  # city
            time.sleep(1)
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_Opincode").fill(final1[14].strip())
            time.sleep(1)  # pincode
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_loanapproval").fill(final1[15].strip())
            time.sleep(1)  # loan approval
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_menno").fill(final1[16].strip())
            time.sleep(1)  # men number
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_af").fill(final1[17].strip())
            time.sleep(1)  # af
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_nri").fill(final1[18].strip())
            time.sleep(1)  # nri
            browser.find_by_id("ctl00_ContentPlaceHolder1_txt_cp").fill(final1[19].strip())
            time.sleep(1)  # cpi

            # ------------------------------------------------ SUBMISSION ON END #

            browser.find_by_id("ctl00_ContentPlaceHolder1_btnsubmit").click()  # submit
            toc = time.clock()
            a = tic - toc
            print
            print ("THE TIME TAKEN TO COMPLETE THE FORM IS : ")
            print(a)
            print "#------------------------ PAGE COMPLETED SUCCESSFULLY--------------------------#"
            time.sleep(1)
            id = id + 1
        else:
            id = id + 1
            f = open("error_s.txt", "a")
            f.write("Error Start from here-------------------- \n ")
            f.write(str(id + 1))
            f.write("Please Check the above page because it was not filled \n ")
            f.close()
            continue

if __name__ == "__main__":


    main()