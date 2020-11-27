from selenium import webdriver
import time
# score.txt yi her seferinde sıfırlamak için 4-5
dosya = open("score.txt","w")
dosya.close()

driver = webdriver.Firefox()
driver.get("https://tr.whoscored.com")
time.sleep(2)
# pop-up 'ı kapatmak için 11-12
elements = driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]')
elements.click()

time.sleep(2)
k=1
while k<30:
    try:
        # önizleye tıklamak için 19-22
        xpath = '//*[@id="today"]/div/div[1]/div/div['+str(k)+']/div[9]/a[1]'
        element = driver.find_element_by_xpath(xpath)
        element.click()
        time.sleep(2)

# tahminler için
        team1 = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[3]/div[1]/div[1]/div/div[1]/div[1]/div[1]/a/span').text
        team2 = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/a/span').text
        score_team1 = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[3]/div[1]/div[1]/div/div[1]/div[1]/span').text
        score_team2 = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div/div[3]/div[1]/div[1]/div/div[1]/div[2]/span').text
        print(team1+" "+score_team1+"-"+score_team2+" "+team2)

        file = open("score.txt","a")
        file.write(team1+" "+score_team1+"-"+score_team2+" "+team2+"\n")
        file.close()
        time.sleep(1)
        driver.back()
    except:
        pass
    finally:
        k+=1
driver.close()