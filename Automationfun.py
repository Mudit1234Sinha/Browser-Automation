from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By  # These 3 are for explicit wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time

path = "C:/Users/ADMIN/Desktop/chromedriver.exe"
browser = webdriver.Chrome(path)

# Below code is for mouse hovering and clicking

browser.get("https://www.apunkagames.biz/#")

others = browser.find_element_by_xpath("//*[@id='menu-item-34809']/a")
horror = browser.find_element_by_xpath("//*[@id='menu-item-34822']/a")
action = ActionChains(browser)
action.move_to_element(others)
time.sleep(4)
action.move_to_element(horror).click().perform()


# Below is the Code for double Clicking of mouse
browser.get("https://demo.guru99.com/test/simple_context_menu.html")
time.sleep(3)
double_click_button = browser.find_element_by_xpath("")
action = ActionChains(browser)
action.double_click(double_click_button).perform()


# Below is the Code for right clicking

browser.get("https://www.google.co.in/")
time.sleep(3)
right_click_button = browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
action = ActionChains(browser)
action.context_click(right_click_button).perform()
time.sleep(3)


# Below is the Code for drag and drop performed using mouse

browser.get("https://demos.telerik.com/kendo-ui/dragdrop/index")

source_element = browser.find_element_by_xpath('//*[@id="draggable"]')
target_element = browser.find_element_by_xpath('//*[@id="droptarget"]')
action = ActionChains(browser)

action.drag_and_drop(source_element, target_element).perform()


# Below is the code for  Maximizing the screen
browser.get("https://rifinder.com")
time.sleep(3)
browser.maximize_window()
# Below is the code for scrolling to a specific point and to the end
browser.execute_script("window.scrollBy(0,1500)","")
browser.execute_script("window.scrollBy(0,document.body.scrollHeight)") # Scroll down to the end
time.sleep(3)
viewing = browser.find_element_by_xpath('//*[@id="content"]/article/div/div/div/div/section[3]/div[3]/div/div/div/div/section[3]/div/div/div[1]/div/div/div[1]/div/div/div/h3')
browser.execute_script("arguments[0].scrollIntoView();", viewing)

# Below code is for uploading of the file

browser.get("https://tus.io/demo.html")
time.sleep(3)
browser.maximize_window()

choose_file = browser.find_element_by_xpath('//*[@id="js-file-input"]')
choose_file.send_keys("C:\\Users\ADMIN\Pictures\js.jpg")

time.sleep(30)
file_show = browser.find_element_by_xpath('//*[@id="js-upload-container"]/a[1]')
file_show.click()


# Below is the code for downloading file

browser.get("https://filehippo.com/download_avast_antivirus/")
time.sleep(4)

download = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/section/div[2]/div/div[2]/a")
download.click()


# Below is the  code for Downloading a file  in a specific folder

browser.get("http://demo.astra-net.com/download/")
time.sleep(4)

chrome_opt = Options()
chrome_opt.add_experimental_option("prefs",{"download.default_directory": "C:\\Users\ADMIN\Desktop\\"})

browser = webdriver.Chrome(executable_path=path, options=chrome_opt)
browser.get("http://demo.astra-net.com/download/")
time.sleep(4)

download = browser.find_element_by_xpath('//*[@id="content_container"]/div/table/tbody/tr[12]/td[1]/a')
download.click()


# Below is the  code for getting cookies and adding cookies to a browser

browser.get("https://www.amazon.in/")

# cookie_get = browser.get_cookies()
# print(cookie_get)
# print(len(cookie_get))

new_cookies = {'name': 'rifinder', 'value': 'de345ty'}
browser.add_cookie(new_cookies)


cookie = browser.get_cookies()
print(len(cookie), end="\n")
print(cookie)

# Below is th ecode for Delete a cookie
browser.delete_cookie("rifinder")
cookie1 = browser.get_cookies()
print(len(cookie1), end="\n")
print(cookie1)

# browser.delete_all_cookies() [For deleting all the cookies]


# For Getting screenshot
browser.get("https://rifinder.com")
browser.save_screenshot("C:\\Users\ADMIN\Videos\screenshot.png")

# With below code, we can type on search bar and see the results
browser.get("https://www.selenium.dev/")
search = browser.find_element_by_id("gsc-i-id1")
search.clear()
time.sleep(2)
search.send_keys("test")
search.send_keys(Keys.RETURN)

# IN the below Code we can Switc between different tabs in our browser
browser.get("https://www.apunkagames.biz/2020/07/out-of-shapes-game.html")
time.sleep(5)

browser.find_element_by_link_text("Click Here to Download This Game").click()
time.sleep(5)

tabs = browser.window_handles
for tab in tabs:
    browser.switch_to.window(tab)
    print(browser.current_url)
    print(browser.title, "\n\n")

