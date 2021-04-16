from selenium import webdriver
import time

url = "https://www.deadstock.ca/products/adidas-originals-superstar-core-black-10?variant=32981988343893"
info = []
try:
    with open('info.txt') as f:
        for line in f.readlines():
            info.append(line.split(":")[1].strip())
except Exception as e:
    print("Error populating personal info into script. Please make sure info.txt is created with correct formatting below:")
    print("shoe_size: 9\nfirst_name: John\nlast_name: Doe\naddress: 1 Apple Road\ntown: Oakville\nprovince: "
          "Ontario\npostalCode: Z1X0K7\nemail: johndoe@gmail.com\nphone: 4161111111\ncard_number: "
          "0000111122223333\nexpiry_date_text: 0522\ncvd: 111")
    quit()
try:
    #start up chrome browser
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\path\\to\\chrome\\user data")
    browser = webdriver.Chrome("./chromedriver", options=options)
    browser.set_window_size(1024, 600)
    browser.maximize_window()
    start_time = time.time()
    browser.get(url)
    time.sleep(2)

    #add shoe to cart
    browser.find_element_by_xpath("//label[@for='ProductSelect-option-Size-{}']".format(info[0])).click()
    browser.find_element_by_xpath("//button[@id='AddToCart']").click()
    time.sleep(1)
    browser.find_element_by_xpath("//a[@class='btn--secondary btn--full cart__checkout']").click()
    time.sleep(1)
    browser.find_element_by_xpath("//button[@class='btn cart__checkout giftbox-checkout giftbox-checkout-cloned']").click()

    # fill out personal info
    try:
        browser.find_element_by_xpath("//input[@placeholder='Email']").send_keys(info[7])
        browser.find_element_by_xpath("//input[@placeholder='First name']").send_keys(info[1])
        browser.find_element_by_xpath("//input[@placeholder='Last name']").send_keys(info[2])
        browser.find_element_by_xpath("//input[@placeholder='Address']").send_keys(info[3])
        browser.find_element_by_xpath("//input[@placeholder='Apartment, suite, etc. (optional)']").send_keys("202")
        browser.find_element_by_xpath("//input[@placeholder='City']").send_keys(info[4])
        browser.find_element_by_xpath("//input[@placeholder='Postal code']").send_keys(info[6])
        browser.find_element_by_xpath("//input[@placeholder='Phone']").send_keys(info[8])
        browser.find_element_by_id("continue_button").click()
    except Exception as e:
        print("Form for personal info now found. Skipping to next page")
        print(e)

    #fill payment info
    time.sleep(1)
    credit_card_text_fields = browser.find_elements_by_class_name("card-fields-iframe")
    credit_card_text_fields[0].click()
    credit_card_text_fields[0].send_keys("0000")
    credit_card_text_fields[0].send_keys("1111")
    credit_card_text_fields[0].send_keys("2222")
    credit_card_text_fields[0].send_keys("3333")

    credit_card_text_fields[1].send_keys("TEST")
    credit_card_text_fields[2].send_keys("04")
    credit_card_text_fields[2].send_keys("25")
    credit_card_text_fields[3].send_keys("111")
    time.sleep(1)
    browser.find_element_by_id("continue_button").click()

    end_time = time.time()
    print("Time Elapsed: {}".format(end_time-start_time))

except Exception as e:
    print("Automation failed due to error: {}".format(e))
