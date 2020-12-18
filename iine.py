from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time
import streamlit as st

#タイトル
st.title('Instagram Like Tool')

login_id = st.text_input('login ID')
password = st.text_input('password')

key_word = st.text_input('いいねしたい#キーワード')


button = st.button('スタート')



if button :


    # ブラウザを開く。
    driver = webdriver.Chrome()
    # Googleの検索TOP画面を開く。
    driver.get("https://www.instagram.com/")
    time.sleep(3)

    # ログインIDを入力する
    id_box = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    id_box.send_keys(login_id)

    #パスワードを入力する
    id_pass = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    id_pass.send_keys(password)

    #ログインボタンを押す
    lg_box = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
    lg_box.click()

    time.sleep(5)
    #後でのボタンを押す
    later = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    later.click()

    time.sleep(3)
    waite = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    waite.click()

    time.sleep(1)
    #ハッシュタグ検索を行う
    srech = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div')
    srech.click()
    enter = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    enter.send_keys(key_word)
    time.sleep(5)
    push = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]')
    push.click()


    time.sleep(3)

    #投稿をクリックする
    touko = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div/div[2]')
    touko.click()

    time.sleep(3)

    iine = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
    iine.click()

    time.sleep(2)

    next = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a')
    next.click()


    for i in range(100):
        time.sleep(3)
        iine2 = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button')
        iine2.click()
        if driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button').is_displayed():


            time.sleep(3)

            next2 = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]')
            next2.click()
        else:
            time.sleep(2)

            next2 = driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/div/a[2]')
            next2.click()

    print('終了しました')
