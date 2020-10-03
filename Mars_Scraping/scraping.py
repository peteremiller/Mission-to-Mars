#!/usr/bin/env python
# coding: utf-8

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import  pandas as pd
import datetime as dt

def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one("ul.item_list li.slide")
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find("div", class_="content_title").get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find("div", class_="article_teaser_body").get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_id('full_image')[0]
    full_image_elem.click()

    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.links.find_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'

    return img_url

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())
    
##NEW CODE    
    
    # Declare Dependencies 
#from bs4 import BeautifulSoup as bs
#from splinter import Browser
#import pandas as pd
#import os
#import time
#import requests
#import warnings
#warnings.filterwarnings('ignore')

#def init_browser():
#    # @NOTE: Path to my chromedriver
#    executable_path = {"executable_path": "C:\\Users\\charm\\Desktop\chromedriver"}
#    return Browser("chrome", **executable_path, headless=False)

# Create Mission to Mars global dictionary that can be imported into Mongo
#mars_info = {}

# NASA MARS NEWS
#def scrape_mars_news():

        # Initialize browser 
#        browser = init_browser()

        #browser.is_element_present_by_css("div.content_title", wait_time=1)

        # Visit Nasa news url through splinter module
#        url = 'https://mars.nasa.gov/news/'
#        browser.visit(url)

        # HTML Object
#        html = browser.html

        # Parse HTML with Beautiful Soup
#        soup = bs(html, 'html.parser')

        # Retrieve the latest element that contains news title and news_paragraph
#        news_title = soup.find('div', class_='content_title').find('a').text
#        news_p = soup.find('div', class_='article_teaser_body').text

        # Dictionary entry from MARS NEWS
#        mars_info['news_title'] = news_title
#        mars_info['news_paragraph'] = news_p

#        return mars_info

#        browser.quit()

# FEATURED IMAGE
#def scrape_mars_image():

        # Initialize browser 
#        browser = init_browser()

        #browser.is_element_present_by_css("img.jpg", wait_time=1)

        # Visit Mars Space Images through splinter module
#        featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
#        browser.visit(featured_image_url)# Visit Mars Space Images through splinter module

        # HTML Object 
#        html_image = browser.html

        # Parse HTML with Beautiful Soup
#        soup = bs(html_image, 'html.parser')

        # Retrieve background-image url from style tag 
#        image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

        # Website Url 
#        main_url = 'https://www.jpl.nasa.gov'

        # Concatenate website url with scrapped route
#        image_url = main_url + image_url

        # Display full link to featured image
#        image_url 

        # Dictionary entry from FEATURED IMAGE
#        mars_info['image_url'] = image_url 
        
#        browser.quit()

#        return mars_info

        

# Mars Weather 
#def scrape_mars_weather():

        # Initialize browser 
#        browser = init_browser()

        #browser.is_element_present_by_css("div", wait_time=1)

        # Visit Mars Weather Twitter through splinter module
#        weather_url = 'https://twitter.com/marswxreport?lang=en'
#        browser.visit(weather_url)

        # HTML Object 
#        html_weather = browser.html

        # Parse HTML with Beautiful Soup
#        soup = bs(html_weather, 'html.parser')

        # Find all elements that contain tweets
#        latest_tweets = soup.find_all('div', class_='js-tweet-text-container')

        # Retrieve all elements that contain news title in the specified range
        # Look for entries that display weather related words to exclude non weather related tweets 
#        for tweet in latest_tweets: 
#            mars_weather = tweet.find('p').text
#            if 'Sol' and 'pressure' in mars_weather:
                #print(mars_weather)
#                break
#            else: 
#                pass
         # Dictionary entry from WEATHER TWEET
#        mars_info['mars_weather'] = mars_weather

#        browser.quit()

#        return mars_info
        
# Mars Facts
#def scrape_mars_facts():

        # Initialize browser 
#        browser = init_browser()

         # Visit Mars facts url 
#        url = 'http://space-facts.com/mars/'
#        browser.visit(url)

        # Use Pandas to "read_html" to parse the URL
#        tables = pd.read_html(url)
        #Find Mars Facts DataFrame in the lists of DataFrames
#        df = tables[1]
        #Assign the columns
#        df.columns = ['Description', 'Value']
#        html_table = df.to_html(table_id="html_tbl_css",justify='left',index=False)

        # Dictionary entry from Mars Facts

#        mars_info['tables'] = html_table

#        return mars_info

# Mars Hemisphere

#def scrape_mars_hemispheres():

        # Initialize browser 
#        browser = init_browser()

        # Visit hemispheres website through splinter module 
#        hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#        browser.visit(hemispheres_url)

        # HTML Object
#        html_hemispheres = browser.html

        # Parse HTML with Beautiful Soup
#        soup = bs(html_hemispheres, 'html.parser')

        # Retreive all items that contain mars hemispheres information
#        items = soup.find_all('div', class_='item')

        # Create empty list for hemisphere urls 
#        hiu = []

        # Store the main_ul 
#        hemispheres_main_url = 'https://astrogeology.usgs.gov' 

        # Loop through the items previously stored
#        for i in items: 
            # Store title
#            title = i.find('h3').text
            
            # Store link that leads to full image website
#            partial_img_url = i.find('a', class_='itemLink product-item')['href']
            
            # Visit the link that contains the full image website 
#            browser.visit(hemispheres_main_url + partial_img_url)
            
            # HTML Object of individual hemisphere information website 
#            partial_img_html = browser.html
            
            # Parse HTML with Beautiful Soup for every individual hemisphere information website 
#            soup = bs( partial_img_html, 'html.parser')
            
            # Retrieve full image source 
#            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
            
            # Append the retreived information into a list of dictionaries 
#            hiu.append({"title" : title, "img_url" : img_url})

#        mars_info['hiu'] = hiu
        
       
#        browser.quit()

        # Return mars_data dictionary 

#        return mars_info
    
    
    #NEW CODE
    
    # Dependencies
#@import pandas as pd
#from splinter import Browser
#from bs4 import BeautifulSoup

# Function to choose the executable path to driver
#def init_browser():
#    executable_path = {"executable_path": "C:/chromedriver/chromedriver"}
#    return Browser("chrome", **executable_path, headless=False)

# Full Scrape function.
#def scrape():

#    """ NASA Mars News """

    # Run init_browser/driver.
#    browser = init_browser()

    # Visit Nasa news url.
#    news_url = "https://mars.nasa.gov/news/"
#    browser.visit(news_url)

    # HTML Object.
#    html = browser.html

    # Parse HTML with Beautiful Soup
#    news_soup = BeautifulSoup(html, "html.parser")

    # Retrieve the most recent article's title and paragraph.
    # Store in news variables.
#    news_title = news_soup.find("div", class_="content_title").find('a').text
#    news_paragraph = news_soup.find("div", class_="article_teaser_body").get_text()

    # Exit Browser.
#    browser.quit()

    # Print Title and Text.
#    print(f'Title: {news_title}\nText: {news_paragraph}')

#    """ JPL Mars Space Images - Featured Image """

    # Run init_browser/driver.
#    browser = init_browser()

    # Visit the url for JPL Featured Space Image.
#    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
#    browser.visit(jpl_url)

    # Select "FULL IMAGE".
#    browser.click_link_by_partial_text("FULL IMAGE")

    # Find "more info" for first image, set to variable, and command click.
#    browser.is_element_present_by_text("more info", wait_time=1)
#    more_info_element = browser.find_link_by_partial_text("more info")
#    more_info_element.click()

    # HTML Object.
#    html = browser.html

    # Parse HTML with Beautiful Soup
#    image_soup = BeautifulSoup(html, "html.parser")

    # Scrape image URL.
#    image_url = image_soup.find("figure", class_="lede").a["href"]

    # Concatentate https://www.jpl.nasa.gov with image_url.
#    featured_image_url = f'https://www.jpl.nasa.gov{image_url}'

    # Exit Browser.
#    browser.quit()

    # Print Faetured Image URL.
#    print(featured_image_url)

#    """ Mars Weather """

    # Run init_browser/driver.
#    browser = init_browser()

    # Visit the url for Mars Weather twitter account.
#    weather_url = "https://twitter.com/marswxreport?lang=en"
#    browser.visit(weather_url)

    # HTML Object.
#    html = browser.html

    # Parse HTML with Beautiful Soup
#    weather_soup = BeautifulSoup(html, "html.parser")

    # Retrieve ALL 'ol' tags and save to variable 'tweets'.
#    tweets = weather_soup.find_all('ol', class_='stream-items')
    # Iterate through all 'tweets' and find text in 'p' tag.
    # Break for most recent tweet if keyword 'InSight' in text.
    # Otherwise move onto next tweet.
#    for tweet in tweets:
#        mars_weather = tweet.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
#        if 'InSight' in tweet:
#            break
#        else:
#            continue

    # Exit Browser.
#    browser.quit()

    # Remove 'anchor' tag text from "mars_weather" via split on 'pic'.
#    mars_weather = mars_weather.split('pic')[0]

    # Replace '\n' with ' '.
#    mars_weather = mars_weather.replace('\n', ' ')

    # Print most recent Mars Weather.
#    print(mars_weather)

#    """ Mars Facts """

    # URL for Mars Facts.
#    facts_url = "https://space-facts.com/mars/"

    # Use Panda's `read_html` to parse the URL.
#    facts_tables = pd.read_html(facts_url)

    # Required table stored in index "1".
    # Save as DF.
#    df_mars_facts = facts_tables[1]

    # Rename columns.
#    df_mars_facts.columns = ['Description', 'Value']

    # Set index to 'Description'.
#    df_mars_facts.set_index('Description', inplace=True)

    # # Convert DF to html and save in Resources Folder.
    # df_mars_facts.to_html('Resources/mars_facts.html')

    # Convert DF to HTML string.
#    mars_facts = df_mars_facts.to_html(header=True, index=True)

 #   """ Mars Hemispheres """

    # Run init_browser/driver.
 #   browser = init_browser()

    # Visit the url for USGS Astrogeology.
 #   astrogeo_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
 #   browser.visit(astrogeo_url)

    # HTML Object.
 #   html = browser.html

    # Parse HTML with Beautiful Soup
 #   astrogeo_soup = BeautifulSoup(html, "html.parser")

    # Store main URL in a variable so that 'href' can be appended to it after each iteration.
 #   main_astrogeo_url = "https://astrogeology.usgs.gov"

    # Each link is located in 'div' tag, class "item".
    # Locate all 4 and store in variable.
 #   hems_url = astrogeo_soup.find_all("div", class_="item")

    # Create empty list for each Hemisphere URL.
 #   hemis_url = []

 #   for hem in hems_url:
 #       hem_url = hem.find('a')['href']
 #       hemis_url.append(hem_url)

 #   browser.quit()

    # Create list of dictionaries called hemisphere_image_urls.
    # Iterate through all URLs saved in hemis_url.
    # Concatenate each with the main_astrogeo_url.
    # Confirm the concat worked properly: confirmed.
    # Visit each URL.

 #   hemisphere_image_urls = []
 #   for hemi in hemis_url:
 #       hem_astrogeo_url = main_astrogeo_url + hemi
 #       print(hem_astrogeo_url)
        
        # Run init_browser/driver.
 #       browser = init_browser()
 #       browser.visit(hem_astrogeo_url)
        
        # HTML Object.
 #       html = browser.html

        # Parse HTML with Beautiful Soup
 #       hemi_soup = BeautifulSoup(html, "html.parser")

        # Locate each title and save to raw_title, to be cleaned.
 #       raw_title = hemi_soup.find("h2", class_="title").text
        
        # Remove ' Enhanced' tag text from each "title" via split on ' Enhanced'.
 #       title = raw_title.split(' Enhanced')[0]
        
        # Locate each 'full.jpg' for all 4 Hemisphere URLs.
 #       img_url = hemi_soup.find("li").a['href']
        
        # Append both title and img_url to 'hemisphere_image_url'.
 #       hemisphere_image_urls.append({'title': title, 'img_url': img_url})
        
 #       browser.quit()

 #   print(hemisphere_image_urls)

 #   """ Mars Data Dictionary - MongoDB """

    # Create empty dictionary for all Mars Data.
 #   mars_data = {}

    # Append news_title and news_paragraph to mars_data.
 #   mars_data['news_title'] = news_title
 #   mars_data['news_paragraph'] = news_paragraph

    # Append featured_image_url to mars_data.
 #   mars_data['featured_image_url'] = featured_image_url

    # Append mars_weather to mars_data.
 #   mars_data['mars_weather'] = mars_weather

    # Append mars_facts to mars_data.
 #   mars_data['mars_facts'] = mars_facts

    # Append hemisphere_image_urls to mars_data.
 #   mars_data['hemisphere_image_urls'] = hemisphere_image_urls

 #   print("Scrape Complete!!!")

 #   return mars_data


