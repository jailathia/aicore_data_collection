from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import uuid
import os
import json

class Scraper:
    '''
    Attributes
    ----------
    URL:str
        the link to the website
    driver:class
        the webdriver

    Methods
    -------

    '''
    def __init__(self, driver, URL, wait_time):
        self.wait_time = wait_time
        self.driver = driver
        self.URL = URL

    def open_url(self):
        self.driver.get(self.URL)

    def accept_cookies(self):
        try:
            sleep(self.wait_time)
            accept_cookies_button = self.driver.find_element(By. XPATH, '//*[@class="_2hTJ5th4dIYlveipSEMYHH BfdVlAo_cgSVjDUegen0F js-accept-all-close"]')
            accept_cookies_button.click()
        except:
            pass

    def get_fixture_link_list(self):
        '''Retrieves the href links to each match and stores them in a list.'''
        sleep(self.wait_time)
        fixture_list = self.driver.find_element(By.XPATH, '//*[@class="fixtures"]')
        home_games = fixture_list.find_elements(By.XPATH, '//*[@data-home="Arsenal"]')
        away_games = fixture_list.find_elements(By.XPATH, '//*[@data-away="Arsenal"]')
        link_list = []
        for game in home_games:
            link_class = game.find_element(By.XPATH, "./div")
            link = link_class.get_attribute('data-href')
            link_list.append(link)
        for game in away_games:
            link_class = game.find_element(By.XPATH, "./div")
            link = link_class.get_attribute('data-href')
            link_list.append(link)
        if len(link_list) != 38:
            print(f'Only {len(link_list)} fixtures in list.')
        else:
            print('All 38 fixtures in list.')

    def scroll_to_bottom(self):
        '''Scrolls to bottom of any page.'''
        last_height = self.driver.execute_script('return document.body.scrollHeight')
        print(f'previous height is: {last_height}')
        new_height = None
        while last_height != new_height:
            self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(self.wait_time)
            new_height = self.driver.execute_script('return document.body.scrollHeight')
            print(f'new height is: {new_height}')
            last_height = new_height
    
    def get_link_list():
        pass


    def click_statistics(self):
        pass


    def get_winner(self):
        pass


    def get_stats(self):
        pass


    def close_browser(self):
        self.driver.quit()


    def scrape_links(self):
        self.open_url()
        self.accept_cookies()
        self.scroll_to_bottom()
        self.get_fixture_link_list()
        #self.close_browser()


if __name__ == '__main__':
    premierleague = Scraper(driver=webdriver.Chrome(),
                            URL='https://www.premierleague.com/results?co=1&se=418&cl=-1',
                            wait_time=2)
    premierleague.scrape_links()