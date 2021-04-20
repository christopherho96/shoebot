# Shoebot Automation

The goal of this repository is to automate the purchasing of a shoe from the item shoe page all the way to end of checkout. 

## Requirements
- python
- selenium
- Google Chrome

## Steps
1. Clone this directory
2. Create an `info.txt` file within the cloned directory.
3. Use the following template to fill out your information. Make sure the template is exact.

    shoe_size: 8.5
    first_name: John  
    last_name: Doe  
    address: 1 Apple Road    
    address_unit: 10
    town: Oakville   
    province: Ontario  
    postalCode: Z1L2F4    
    email: test@gmail.com  
    phone: 4161111111    
    card_number: 0000111122223333  
    expiry_date_text: 0522  
    cvd: 111  

4. Open the `purchase.py` file in a text editor. Change the `url` variable to the url of the shoe detail page on Sportchek. Save and close.
5. Open command prompt/terminal, cd into the directory. Run `python purchase.py`
