import discord
from discord.ext import commands
import asyncio, datetime, sys, os, time
import pickle
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



async def check(ctx):
    global infoDict, id, dm_channel
    id=ctx.author.id
    dm_channel=ctx.author.dm_channel
    await dm_channel.send(f'Now running for ID {ctx.author.id}')
    with open('secretData/data.dat', 'rb') as f:
        infoDict=pickle.load(f)
    await dm_channel.send(f"Hello, {infoDict[id]['ID']}")
    initNlogin()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".coursebox")))
    bs=BeautifulSoup(driver.page_source,features='html.parser')
    #courses=driver.find_element_by_id('frontpage-course-list').find_elements_by_class_name('coursebox')
    try:
        courses=bs.select_one('#frontpage-course-list').select('.coursebox')
    except:
        bs=BeautifulSoup(driver.page_source,features='html.parser')
        courses=bs.select_one('#frontpage-course-list').select('.coursebox')
    for i in courses:
        #aTag=i.find_element_by_class_name('coursename').find_element_by_tag_name('a')
        aTag=i.select_one('.coursename').a
        link=aTag['href']
        courseName=aTag.get_text()
        #prof=i.find_element_by_class_name('teacher').text
        prof=i.select_one('.teacher').get_text()
        courseNum=i.select_one('.subject_id').get_text()
        await dm_channel.send(f"\n{courseNum}\n{courseName} - {prof} 교수님\n{link}")
        await asyncio.sleep(3)

def initNlogin():
    global driver
    options=webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    driver=webdriver.Chrome('../chromedriver',options=options)
    driver.implicitly_wait(10)
    driver.get('https://yscec.yonsei.ac.kr/')
    idInput=driver.find_element_by_id('username')
    idInput.click()
    idInput.send_keys(infoDict[id]['ID'])
    pwInput=driver.find_element_by_id('password')
    pwInput.click()
    pwInput.send_keys(infoDict[id]['PW'])
    loginBtn=driver.find_element_by_id('loginbtn')
    loginBtn.click()
    #driver.get('https://yscec.yonsei.ac.kr/')