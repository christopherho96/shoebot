from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

url = "https://www.sportchek.ca/categories/men/footwear/basketball-shoes/product/nike-mens-air-jordan-13-retro-basketball-shoes-color-333316063_10-333316063.html#333316063%5Bcolor%5D=333316063_10"
info = []
try:
    with open('info.txt') as f:
        for line in f.readlines():
            info.append(line.split(":")[1].strip())
except Exception as e:
    print("Error populating personal info into script. Please make sure info.txt is created with correct formatting below:")
    print("shoe_size: 9\nfirst_name: John\nlast_name: Doe\naddress: 1 Apple Road\naddress_unit: 10\ntown: "
          "Oakville\nprovince: Ontario\npostalCode: Z1X0K7\nemail: johndoe@gmail.com\nphone: 4161111111\ncard_number: "
          "0000111122223333\nexpiry_date_text: 0522\ncvd: 111")
    quit()
try:
    #start up chrome browser
    # options = webdriver.ChromeOptions()
    # options.add_argument("user-data-dir=C:\\path\\to\\chrome\\user data")
    # browser = webdriver.Chrome("./chromedriver", options=options)
    browser = webdriver.Chrome("./chromedriver")
    browser.set_window_size(1024, 600)
    browser.maximize_window()
    start_time = time.time()
    browser.get(url)

    #add shoe to cart
    try:
        browser.find_element_by_xpath("//button[@class='pop-up__newsletter-close']").click()
        time.sleep(1)
    except Exception as e:
        print("Could not find bottom banner popup")
        print(e)
    browser.find_element_by_xpath("//*[@class='option-tiles__items']/*[@title='{}']/span[text()='{}']".format(info[0], info[0])).click()
    time.sleep(1)
    browser.find_element_by_xpath("//button[@class='add-cart product-detail__button product-detail__button-icon']").click()
    time.sleep(1)
    browser.find_element_by_xpath("//a[@class='header-cart__trigger drawer-ui__toggle']").click()

    time.sleep(2)
    browser.find_element_by_xpath("//button[@class='button button_color_red continue-checkout']").click()
    time.sleep(10)
    browser.find_element_by_xpath("//input[@value='Checkout as a guest']").click()

    time.sleep(2)
    #fill in personal info
    browser.find_element_by_xpath("//input[@name='firstName']").send_keys(info[1])
    browser.find_element_by_xpath("//input[@name='lastName']").send_keys(info[2])
    browser.find_element_by_xpath("//input[@name='line1']").send_keys("{}-{}".format(info[4], info[3]))
    browser.find_element_by_xpath("//input[@name='town']").send_keys(info[5])
    browser.find_element_by_xpath("//select[@id='province']/option[text()='{}']".format(info[6])).click()
    browser.find_element_by_xpath("//input[@name='postalCode']").click()
    browser.find_element_by_xpath("//input[@name='postalCode']").send_keys(info[7])
    time.sleep(1)
    browser.find_element_by_xpath("//input[@name='email']").send_keys(info[8])
    time.sleep(1)
    browser.find_element_by_xpath("//input[@name='phone']").click()
    browser.find_element_by_xpath("//input[@name='phone']").send_keys(info[9])
    browser.find_element_by_xpath("//label[@name='Sportchek_Regular_Shipping']/span[@class='radio']").click()
    browser.find_element_by_xpath("//button[@class='button button_color_red continue-checkout']").click()
    time.sleep(2)
    try:
        browser.find_element_by_xpath("//input[@value='Continue']").click()
    except Exception as e:
        print("No address warning popup found")
        print(e)

    #fill in bank info
    time.sleep(10)
    browser.switch_to.frame(browser.find_element_by_id("ctfs-iframe"))
    time.sleep(2)
    browser.find_element_by_xpath("//input[@id='card_number']").send_keys(info[10])
    browser.find_element_by_xpath("//input[@id='expiry_date_text']").send_keys(info[11])
    browser.find_element_by_xpath("//input[@id='cvd_input']").send_keys(info[12])
    browser.find_element_by_xpath("//button[@class='btn btn_lg btn_block btn_primary place-order-proceed__button']").click()

    end_time = time.time()
    print("Time Elapsed: {}".format(end_time-start_time))

except Exception as e:
    print("Automation failed due to error: {}".format(e))
