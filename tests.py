# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests.py

from selenium.webdriver.common.by import By
import time

def test_skript_automation(selenium):

    # открываем главную страницу
    selenium.get("https://www.chitai-gorod.ru")
    selenium.set_window_size(1920, 1080)

    time.sleep(5)

    # Выполняем поиск по слову "тестирование" в поле
    search_input = selenium.find_element(By.NAME, 'phrase')

    search_input.clear()
    search_input.send_keys('тестирование')

    search_button = selenium.find_element(By.CLASS_NAME, 'header-search__button')
    search_button.submit()

    time.sleep(5)

    # Добавляем книги в корзину
    buy_button_1 = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div/section/section/div/article[5]/div[3]/div[1]')
    selenium.execute_script("arguments[0].click();", buy_button_1)

    time.sleep(2)

    buy_button_2 = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div/section/section/div/article[10]/div[3]/div[1]')
    selenium.execute_script("arguments[0].click();", buy_button_2)

    time.sleep(2)

    buy_button_3 = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div/section/section/div/article[13]/div[3]/div[1]')
    selenium.execute_script("arguments[0].click();", buy_button_3)

    time.sleep(2)

    # Переходим в корзину
    basket_button = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[5]/div[3]/div[1]')
    selenium.execute_script("arguments[0].click();", basket_button)

    time.sleep(5)

    # Проверяем, что в корзине находятся все выбранные книги, в нужном количество, за выбранную цену
    name_1 = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]')
    assert name_1.text == "Тестирование программного обеспечения: учебное пособие для вузов"

    #num_1 = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]')
    #assert num_1.text == "1"

    get_price_1 = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[3]/div[1]/div[1]')
    assert get_price_1.text == "701 ₽"
    price_1 = str(get_price_1.text)
    price_1 = price_1.replace(" ", "")
    price_1 = price_1.replace("₽", "")
    price_1 = int(price_1)


    name_2 = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]')
    assert name_2.text == "Что такое тестирование. Курс молодого бойца"

    #num_2 = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]')
    #assert num_2.text == "1"

    get_price_2 = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/div[1]/div[2]')
    assert get_price_2.text == "1 291 ₽"
    price_2 = str(get_price_2.text)
    price_2 = price_2.replace(" ", "")
    price_2 = price_2.replace("₽", "")
    price_2 = int(price_2)



    name_3 = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]/div[1]/div[1]')
    assert name_3.text == "Принципы юнит-тестирования"

    #num_3 = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]')
    #assert num_3.text == "1"

    get_price_3 = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[2]')
    assert get_price_3.text == "1 394 ₽"
    price_3 = str(get_price_3.text)
    price_3 = price_3.replace(" ", "")
    price_3 = price_3.replace("₽", "")
    price_3 = int(price_3)


    get_total_sum_1 = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]')
    total_sum_1 = str(get_total_sum_1.text)
    total_sum_1 = total_sum_1.replace(" ", "")
    total_sum_1 = total_sum_1.replace("₽", "")
    total_sum_1 = int(total_sum_1)
    my_total_sum_1 = price_1 + price_2 + price_3
    assert total_sum_1 == my_total_sum_1

    get_total_num_1 = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]/div[1]')
    total_num_1 = str(get_total_num_1.text)
    total_num_1 = total_num_1.replace(" ", "")
    total_num_1 = total_num_1.replace("товара", "")
    total_num_1 = int(total_num_1)


    # Удалим одну книгу из заказа
    delete_button = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]')
    selenium.execute_script("arguments[0].click();", delete_button)

    time.sleep(5)

    # Проверим, что итоговая цена изменилась
    get_total_sum_2 = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]')
    total_sum_2 = str(get_total_sum_2.text)
    total_sum_2 = total_sum_2.replace(" ", "")
    total_sum_2 = total_sum_2.replace("₽", "")
    total_sum_2 = int(total_sum_2)
    my_total_sum_2 = price_1 + price_2
    assert total_sum_2 == my_total_sum_2
    assert price_3 == total_sum_1 - total_sum_2

    # Проверим, что изменилось количество товара
    get_total_num_2 = selenium.find_element(By.XPATH, '//*[@id="__layout"]/div/div[3]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]/div[1]')
    total_num_2 = str(get_total_num_2.text)
    total_num_2 = total_num_2.replace(" ", "")
    total_num_2 = total_num_2.replace("товара", "")
    total_num_2 = int(total_num_2)

    assert total_num_2 == total_num_1 - 1



