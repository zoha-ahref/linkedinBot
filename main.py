from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

DRIVER_PATH = "your/driver/path"
EMAIL_ADDR = "youremail@email.com"
PASSWORD = "yourpassword"
PHONE = "1234567890"


chrome_driver_path = DRIVER_PATH
driver = webdriver.Chrome(executable_path=chrome_driver_path)

#Automate Sign in
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=sales&location=London%2C%20England%2C%20United%20Kingdom")
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)

email = driver.find_element_by_css_selector("input#username")
email.send_keys(EMAIL_ADDR)

password = driver.find_element_by_css_selector("input#password")
password.send_keys(PASSWORD)

button = driver.find_element_by_class_name("login__form_action_container")
button.click()



#find elements in job-card-container
time.sleep(5)
job_card = driver.find_elements_by_css_selector(".job-card-container--clickable")

for job in job_card:
    print("called")
    job.click()
    time.sleep(2)

    try:
        apply = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply.click()
        time.sleep(5)

        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)
        submit = driver.find_element_by_css_selector("footer button")
#Check for next button
        if submit.get_attribute("data-control-name") == "continue_unify":

            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("multistep process skipped")
            continue


        else:
            submit.click()

        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()


    except NoSuchElementException:
        print("No button, skipped")
        continue

time.sleep(5)
driver.quit()