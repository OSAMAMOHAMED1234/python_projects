from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
browser.get('https://github.com/osama-mohamed/')


followers = browser.find_element(By.CSS_SELECTOR, 'div.mb-3 a span').text
following = browser.find_element(By.CSS_SELECTOR, 'div.mb-3 a:nth-of-type(2) span').text
repos = browser.find_elements(By.CSS_SELECTOR, 'span.Counter')[0].text
stars = browser.find_elements(By.CSS_SELECTOR, 'span.Counter')[3].text
print(f'followers => {followers}, following => {following}, repos => {repos}, stars => {stars}')


# browser.find_element(By.LINK_TEXT , 'Download My CV').click()

# al = browser.find_element(By.ID , 'user-content---download-my-cv').find_elements(By.TAG_NAME, 'a')
# al[1].click()

# al = browser.find_element(By.XPATH , '//h2[@id="user-content---download-my-cv"]/a[2]')
# al.click()