from selenium import webdriver
from time import sleep

class anglebot():

    j = 0

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://app.angle3d.co/')

        i = 0
        domain = '' # your shopname
        email = ''
        password = ''

        while True:
            sleep(0.5)
            if i == 0:
                try:
                    domain_btn = self.driver.find_element_by_xpath('/html/body/app-root/app-login/div/div/div[2]/form/div[2]/div[2]/input')
                    domain_btn.clear()
                    domain_btn.send_keys(domain)

                    login_btn = self.driver.find_element_by_xpath('/html/body/app-root/app-login/div/div/div[2]/form/button/span')
                    login_btn.click()
                    i = 1
                    continue
                except Exception:
                    pass
            elif i == 1:
                try:
                    email_btn = self.driver.find_element_by_xpath("//*[@id='account_email']")
                    email_btn.clear()
                    email_btn.send_keys(email)

                    next_btn = self.driver.find_element_by_xpath("//*[@id='body-content']/div[1]/div/div/div/div[2]/div/form/button")
                    next_btn.click()
                    i = 2
                    continue
                except Exception:
                    pass

            elif i == 2:
                try:
                    pass_btn = self.driver.find_element_by_xpath('//*[@id="account_password"]')
                    pass_btn.clear()
                    pass_btn.send_keys(password)

                    next_btn = self.driver.find_element_by_xpath('//*[@id="login_form"]/div[2]/ul/button')
                    next_btn.click()
                    i = 3
                    continue
                except Exception:
                    pass

            elif i == 3:
                try:
                    next_btn = self.driver.find_element_by_xpath('/html/body/app-root/app-layout/div/div/div/app-sidebar/nav/div/ul/li[2]/a/i')
                    next_btn.click()
                    i = 4
                    continue
                except Exception:
                    pass

            elif i == 4:
                try:
                    next_btn = self.driver.find_element_by_xpath('//*[@id="product-table"]/div/div/table/tbody/tr[1]/td[2]/span/span/img')
                    next_btn.click()
                    i = 5
                    continue
                except Exception:
                    pass
            
            elif i == 5:
                try:
                    next_btn = self.driver.find_element_by_xpath('/html/body/app-root/app-layout/div/div/div/main/div[1]/app-customizer/div[4]/div[2]/app-customizer-mode/div[1]/span/strong')
                    next_btn.click()
                    i = 6
                    continue
                except Exception:
                    pass

            elif i == 6:
                try:
                    self.select()
                except Exception:
                    pass

    def select(self):
        self.j += 1

        content = ""
        for number in range(1,7):
            content += self.driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/div/main/div[1]/app-customizer/div[4]/div[2]/app-customizer-model-settings/app-model-settings/div/div[2]/div[2]/div/app-binding-types/div[2]/div[4]/div[" + str(self.j) + "]/div[2]/div[1]/div[" + str(number) + "]").text
            if number < 6:
                content += " "
                
        
        print(content)

        self.driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/div/main/div[1]/app-customizer/div[4]/div[2]/app-customizer-model-settings/app-model-settings/div/div[2]/div[2]/div/app-binding-types/div[2]/div[4]/div[" + str(self.j) + "]/div[2]/div[2]/p-dropdown/div/div[3]/label/div/strong").click()
        sleep(0.3)

        self.driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/div/main/div[1]/app-customizer/div[4]/div[2]/app-customizer-model-settings/app-model-settings/div/div[2]/div[2]/div/app-binding-types/div[2]/div[4]/div[" + str(self.j) + "]/div[2]/div[2]/p-dropdown/div/div[5]/div[1]/input").send_keys(content)
        sleep(1)

        self.driver.find_element_by_xpath("/html/body/app-root/app-layout/div/div/div/main/div[1]/app-customizer/div[4]/div[2]/app-customizer-model-settings/app-model-settings/div/div[2]/div[2]/div/app-binding-types/div[2]/div[4]/div[" + str(self.j) + "]/div[2]/div[2]/p-dropdown/div/div[5]/div[2]/ul/p-dropdownitem/li/div/strong").click()
        driver.find_element_by_xpath("//option[@value=[" + self.j + "]").click()

bot = anglebot()
bot.login()
