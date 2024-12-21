from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import datetime
from datetime import timedelta

option=webdriver.ChromeOptions()
option.add_argument("--headless")
option.add_experimental_option('detach', True) # Keep the browser open after the process has ended

driver = webdriver.Chrome() # Инициализация драйвера Chrome
# driver = webdriver.Chrome(options=option) # Инициализация headless драйвера Chrome

# file = open("../log.txt", "w")

# Sc functions ------------------------------------
def set_up(url = 'http://www.saucedemo.com/'):
    """Заходит на сайт"""
    driver.get(url) # Переход на сайт
    driver.maximize_window() # Максимизация окна
    # driver.save_screenshot(f"saucedemo_tests\\0_Screenshot_setup"
    #                        f"_{datetime.datetime.now().strftime("%Y.%m.%d_%H-%M-%S")}.png")


# End of sc functions -----------------------------

# Main block

set_up('https://demoqa.com/date-picker')
sleep(1)
action = ActionChains(driver)

# Ищем и очищаем поле ввода даты
date_input = driver.find_element(By.XPATH, '//*[@id="datePickerMonthYearInput"]')
date_input.send_keys(Keys.CONTROL + 'a')
date_input.send_keys(Keys.DELETE)
sleep(2)

# Определяем текущую дату
current_date = datetime.datetime.now()
print(f"Current date is {current_date}")

# Определяем новую дату через дельту
new_date = current_date + datetime.timedelta(days=10, hours=-8)
# print(f"New date is {new_date}")

# Задаём формат новой даты, передаём в поле ввода
new_date = new_date.strftime("%m.%d.%Y")
print(f"New date is {new_date}")
date_input.send_keys(new_date)


# Ищем и очищаем поле ввода даты и времени
date_time_input = driver.find_element(By.XPATH, '//*[@id="dateAndTimePickerInput"]')
date_time_input.send_keys(Keys.CONTROL + 'a')
date_time_input.send_keys(Keys.DELETE)
sleep(2)

# Задаём формат новой даты и времени, передаём в поле ввода
new_date = current_date + datetime.timedelta(days=9, hours=-4)
new_date_time = new_date.strftime("%B %d, %Y %H:%M %p")
print(f"New date and time is {new_date_time}")
date_time_input.send_keys(new_date_time)

action.move_by_offset(200, yoffset=200).click().perform() # передвинуть курсор и кликнуть, чтоб закрылся календарь
# driver.save_screenshot(f"C:\\SeleniumTest\\pythonProject1\\screens\\Screenshot_calendar_{datetime.datetime.now().strftime("%Y.%m.%d_%H-%M-%S")}.png")
# file.close()
sleep(2)
