# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 13:42:19 2019
this script contain a function that will use selenium driver to login to a webpage
to use this install selenium driver for chrome (or any other browser) on operating system first
@author: Moji h safa
"""
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep

def automated_log_in_selenium (path_to_driver,website, username_xpath, password_xpath,
                               signin_xpath, username, password):
    '''
    path_to_driver : a string for path to the selenium driver exe file on your system
    website        : a string for the login website address
    username_xpath : a string a string for xpath of username field (can be found with inspect element of browser)
    password_xpath : a string for xpath of password field (can be found with inspect element of browser)
    signin_xpath   : a string for xpath of sign-in button  (can be found with inspect element of browser)
    username :  astring for user name that was created
    password : a string for password that was created
    return driver : driver object that is now inside the website  and can be used to scrap the website after that
    '''
    driver = webdriver.Chrome(executable_path= path_to_driver)

    driver.get(website)
    sleep(2) # waits 2 seconds
    driver.find_element_by_xpath(username_xpath).send_keys(username)
    driver.find_element_by_xpath(password_xpath).send_keys(password)
    driver.find_element_by_xpath(signin_xpath).click()
    wait = WebDriverWait(driver, 5) # another method to wait
    return driver
    

driver_logged_in = automated_log_in_selenium ('''with all parameters''') # we are in! so get any page after this ....
driver_logged_in.get('''another page of the website''')    
    
    