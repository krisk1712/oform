# -*- coding: utf-8 -*-
import os
import re
import time
import urllib
from AbbyyOnlineSdk import *
from splinter import Browser
from PIL import Image
import PIL.ImageOps

processor = None


def setup_processor():
    processor.ApplicationId = "fiveocrtext"
    processor.Password = "FTlHcR6n5oyH3FwoGfN39I6F"

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
        print(".................")
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

    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_Uname").fill("C31052018427")  # Enter the Users name
    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_pass").fill("5SSGS")  # entering the password
    browser.find_by_id("ctl00_ContentPlaceHolder1_btnsubmit").click()  # submit to login

    # ------------------------------------------------ LOGED IN ----------------------------------------------#

    # ------------------------------------------------- FORM FILLING ------------------------------------------#
    no_box = browser.find_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_drp_pagejump"]/option')
    print "#----------------------START HERE -----------------------------------#"

    tic = time.clock()
    print "#------------------ INFORMATION ON THE PAGE ARE : -----------------#"
    print "THE LENGTH OF THE TOTAL PAGES ARE: "
    print len(no_box)
    id = 502

    while 0 <= id <= 599:

        no_box = browser.find_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_drp_pagejump"]/option')

        no_box[id].click()
        time.sleep(1)

        # ------------------------------------------------ PRINTING THE IMAGE URL FOR DOWNLOAD --#
        image_url = browser.find_by_id('ctl00_ContentPlaceHolder1_MainImg')['src']

        # ----------------------------------------- SAVING IMAGE VIA URLLIB --------------------------------#
        urllib.urlretrieve(image_url, "locol1.png")
        time.sleep(0.5)
        image = Image.open('locol1.png')
        inverted_image = PIL.ImageOps.invert(image)
        time.sleep(0.5)
        inverted_image.save('final.png')
        time.sleep(0.5)
        # -------------------------------------------- IMAGE SAVED AS (loco.png) -----------------------------#

        processor = AbbyyOnlineSdk()

        setup_processor()

        source_file = 'final.png'
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
        if num_lines == 3 or num_lines == 2:
            for k in range(0, num_lines):
                a = a + text[k]
            b = a.decode('unicode_escape').encode('ascii', 'ignore')
            c = str(b).split("-")
            final = []
            for items in c:
                final.append(re.sub('       ', '', items))
            time.sleep(1)
            print len(final)
            final1 = []
            for items in final:
                final1.append(re.sub('\n', '', items))
            flist1 = []
            for i in range(0, len(final1)):
                if i == 14:
                    flist1.extend(final1[i].split(" "))
                else:
                    flist1.append(final1[i])
            last_arr = []
            for i in flist1:
                if i != '':
                    last_arr.append(i)
            print last_arr
            print len(last_arr)
            if len(last_arr) == 20:
                print("The page that is filling now is  :  " + str(id+1))
                print "----------Filling starts from here-------------------"
                try:
                    time.sleep(1)
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_tbc").fill(last_arr[0].strip())
                    time.sleep(1)  # first name
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_name").fill(last_arr[1].strip())
                    time.sleep(1)  # last name
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_email").fill(last_arr[2].strip())
                    time.sleep(1)  # email
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_mobno").fill(last_arr[3].strip())
                    time.sleep(1)  # mobile number
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_gender").fill(last_arr[4].strip())
                    time.sleep(1)  # gender
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_licenceno").fill(last_arr[5].strip())
                    time.sleep(1)  # licence number
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_girno").fill(last_arr[6].strip()) # grid number
                    time.sleep(1)
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_panno").fill(last_arr[7].strip())
                    time.sleep(1)  # pan number
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_Hadd").fill(last_arr[8].strip())
                    time.sleep(1)  # state
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_Hcity").fill(last_arr[9].strip())
                    time.sleep(1)  # city
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_Hpin").fill(last_arr[10].strip())
                    time.sleep(1)  # pin
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_HState").fill(last_arr[11].strip())
                    time.sleep(1)  # address
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_Oadd").fill(last_arr[12].strip())
                    time.sleep(1)  # address
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_Ocity").fill(last_arr[13].strip())  # city
                    time.sleep(1)
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_Opincode").fill(last_arr[14].strip())
                    time.sleep(1)  # pincode
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_loanapproval").fill(last_arr[15].strip())
                    time.sleep(1)  # loan approval
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_menno").fill(last_arr[16].strip())
                    time.sleep(1)  # men number
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_af").fill(last_arr[17].strip())
                    time.sleep(1)  # af
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_nri").fill(last_arr[18].strip())
                    time.sleep(1)  # nri
                    browser.find_by_id("ctl00_ContentPlaceHolder1_txt_cp").fill(last_arr[19].strip())
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
                except:
                    print("------------THERe WAS AN ERROR SO PLEASE CHECK THE PAGE FOR THE ERROR IN THE ERROR LOG---------")
                    f = open("error_seethatosee.txt", "a")
                    f.write("--------------THIS IS A EXCEPT LOOP ERROR CHECK THAT -------------------- \n ")
                    f.write("----->  " +"       "+  str(id + 1) + "     " + "<---THis is the page that is not filled")
                    f.write("\n")
                    f.write(str(len(last_arr)) + "\n")
                    f.write("\n")
                    f.write(str(last_arr) + "\n")
                    f.write("Please Check the above page because it was not filled \n ")
                    f.close()
                    id = id + 1
            else:
                    print("------------THERe WAS AN ERROR SO PLEASE CHECK THE PAGE FOR THE ERROR IN THE ERROR LOG---------")
                    f = open("error_seethatosee.txt", "a")
                    f.write("--------------THIS IS ELSE LOOP ERROR CHECK THAT -------------------- \n ")
                    f.write("----->  " +"       "+  str(id + 1) + "     " + "<---THis is the page that is not filled")
                    f.write("\n")
                    f.write(str(len(last_arr)) + "\n")
                    f.write("\n")
                    f.write(str(last_arr) + "\n")
                    f.write("Please Check the above page because it was not filled \n ")
                    f.close()
                    id = id + 1
        else:
            print "--------------------THERE IS AN ERROR CHECK FOR THE ERROR---------------"
            f = open("error_seethatosee.txt", "a")
            f.write("-----------------------LESS COMPONENT ERROR (CASE 2)-------------------- \n ")
            f.write(str(id + 1))
            f.write("\n")
            f.write(str(len(last_arr))+ "\n")
            f.write("\n")
            f.write(str(last_arr)+"\n")
            f.write("Please Check the above page because it was not filled \n ")
            f.close()
            id = id + 1
            continue

if __name__ == "__main__":


    main()