# Install required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

website_url = "https://anycallmobilemm.com/product-category/smartphone/"

def create_page_urls(main_url):
    """Create web page urls from the website url."""
    
    # Step 1 - Get website HTML and store into web_data
    web_data = requests.get(main_url).text
    
    # Step 2 - Create a beautifulsoup object to read web data
    bsObj = BeautifulSoup(web_data, "html.parser")
    
    # Create web page urls
    # Find Max Page Number
    max_page_num = int(bsObj.find_all("a", "page-numbers")[-2].text)
    page_url_list = []
    for i in range(1, max_page_num+1):
        page_url = main_url + "page/" + str(i)
        page_url_list.append(page_url)
    return page_url_list

def extract_p_info_tags(url):
    """ Extract Product Info Tags and return as a list. """
    
    # step 1 - Get website HTML and store into web_data
    web_data = requests.get(url).text
    
    # Step 2 - Create a beautifulsoup object to read web data
    bsObj = BeautifulSoup(web_data, "html5lib")

    # Step 3 - Extract all product info
    product_info_tags_list = bsObj.find_all("div", "product-element-bottom")
    
    return product_info_tags_list

def extract_p_name(p_info_tags_list):
    """ Create product name from the product info tag. and create a product name list. """
    
    p_name_list = []
    # get product name list 
    for p_info_tag in p_info_tags_list:
        p_name_tag = p_info_tag.find("h3", "wd-entities-title")
        product_name = p_name_tag.text
        p_name_list.append(product_name)
        
    return p_name_list

def extract_p_price(p_info_tags_list):
    """ Create product price from the product info tag. and create a product price list. """
    
    p_price_list = []
    # get product price list
    for p_info_tag in p_info_tags_list:
        p_price_tag = p_info_tag.find("span", "price")
        p_price = p_price_tag.text.replace(",", "").replace("K", "")
        try:
            p_price = int(p_price)
            p_price_list.append(p_price)
        except ValueError:
            discount_price_list = p_price.split("\xa0s")
            p_price = discount_price_list[0]
            p_price = p_price.strip()
            p_price = int(p_price)
            p_price_list.append(p_price)
            
    return p_price_list
    
########################## Main Program ###################################
def main():
    # Step 1 - Create URLs for all web pages
    web_url_list = create_page_urls(website_url)

    ## step 2 - Extract Data From Each Web Page of the Web URL List.
    ##          Store all page data in final_df
    url_count = 0
    final_df = pd.DataFrame()
    for web_page in tqdm(web_url_list):
        # Extract product info tags
        p_info_tags_list = extract_p_info_tags(web_page)

        # create Product Name List
        p_name_list = extract_p_name(p_info_tags_list)
        
        # create Product Price List
        p_price_list = extract_p_price(p_info_tags_list)
        
        # create page level dataframe
        page_df = pd.DataFrame({"Product Name":p_name_list,
                                "Product Price":p_price_list})
        url_count += 1
        print(f"Web Page {url_count} is completed successfully!.")
        
         # collect final_df from all web pages
        final_df = pd.concat([final_df, page_df])
        
     ## step 3 -  Export the final data as excel file.
    file_path = ""
    try:
        file_path = "D://Output//"
        final_df.to_excel(f"{file_path}Final Data.xlsx", index=False)
    except:
        file_path = "current"
        final_df.to_excel("Final Data.xlsx", index=False)
    print(f"File export is completed successfully in \"{file_path}\" folder.\n")
    
    # Process is Finish!!
    print("Project is completed successfully!")

########################## main function call ##############################
if __name__ == "__main__":
    main()