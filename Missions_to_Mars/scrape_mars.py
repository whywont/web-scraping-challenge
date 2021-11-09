from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager  
import pandas as pd


def scrape():

    scrape_dict = {}
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    #Scrape latest news site
    url_news = 'https://redplanetscience.com/'
    browser.visit(url_news)

    html = browser.html
    soup = bs(html, 'html.parser')
    
    news_title = soup.find('div', class_= 'content_title').text
    desc = soup.find('div', class_ = 'article_teaser_body').text

    scrape_dict['news_title'] = news_title
    scrape_dict['news_desc'] = desc

    #Scrape Mars images
    url_space = 'https://spaceimages-mars.com/'
    browser.visit(url_space)
    
    html = browser.html
    soup = bs(html, 'html.parser')

    featured_image_src = soup.find('img', class_ = 'headerimage fade-in')['src']
    featured_image = url_space + featured_image_src

    scrape_dict['featured_image'] = featured_image

    #Scrape table
    url_table = 'https://galaxyfacts-mars.com/'
    table = pd.read_html(url_table)

    df = table[0]
    df.head()
    df = df.transpose()
    table_df = df.rename(columns=df.iloc[0])
    html_table = table_df.to_html()
    html_table


    scrape_dict['facts_table'] = html_table
    #Scrape Hemisphere images
    url_hemi = 'https://marshemispheres.com/'
    browser.visit(url_hemi)

    html = browser.html
    soup = bs(html, 'html.parser')

    tests = soup.find_all('div', class_='item')

    hemisphere_imgs = []
    for test in tests:
        title = test.find('h3').text
        browser.links.find_by_partial_text(title).click()
    
        html_link = browser.html
        soup_link = bs(html_link, 'html.parser')
    
        img_scr = soup_link.find('img', class_ = 'wide-image')['src']
        img_scr_full = url_hemi + img_scr
    
        links = {}
        links['title'] = title
        links['img_url'] = img_scr_full
    
        browser.back()
        hemisphere_imgs.append(links)

    scrape_dict['hemisphere_images'] = hemisphere_imgs

    browser.quit()

    return scrape_dict


scrape()



    
    
