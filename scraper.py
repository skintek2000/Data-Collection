from time import sleep

"""
                                                                   Import of necessary modules
"""

from selenium.common import NoSuchElementException
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import json

"""

                                                                Definition a class Scraper()
                                                                
"""
class Scraper():
        """
        Definition of the the method of class
        """
        # Reserved method __init__, known as a constructor.
        def __init__(self):
              #Create a variable (type dict)  to contain data obtained from web scraping
              self._data = dict()
              # Call the method  read_cities_user

              """
              Installation chrome driver.
              """
              self.chrome_driver = ChromeDriverManager().install()

        # Method to read name of cities to scraping from a programmer input
        def read_cities_programmer(self, cities_list):

                """  Create a private variable instance named cities_list  """
                self._cities_list = cities_list


        # Method to read name of cities to scraping from a user input
        def read_cities_user(self):

                #Define a variable to contain the name list cities
                cities_list= []

                #Input number of cities
                number_cities= int(input("Insert the number of cities : "))

                #Input name of city from user
                for index in range(1,number_cities + 1):
                     city_name = input("Insert the name of the city " + str(index) + " : ")
                     cities_list.append(city_name)

                     """  Create a private variable instance named cities_list  """
                     self._cities_list = cities_list


              # Method to read name of city to scraping from a file
        def read_cities_file_csv(self):
                # Input name file
                file_name = input("Inserisci il nome del file: ")
                 # Add extension to name_file
                file_name += ".txt"

                # Read a list of city strings
                with open(file_name) as file:
                        rows = file.readlines()

                """  Create a private variable instance named cities_list  """
                self._cities_list = rows


        #Method to scrape single city for the crime attributes
        def scraper_single_city_crime(self, citta):


                #Reduce the probabily to no finding web element
                self.driver.maximize_window()
                # Write the name in the menu selector city
                self.driver.find_element(By.ID, 'city_selector_menu_city_id').send_keys(citta)
                # Suspends execution of the current thread for a 3  seconds.
                sleep(3)

                #Select the name of the city from the menu selector city
                self.driver.find_element(By.CLASS_NAME, 'ui-menu-item').click()

                # Suspends execution of the current thread for a 3 seconds
                sleep(3)

                #Define the instruction that can generate a exception
                try:
                        self.driver.find_element_by_xpath('//span[@class = "ui-button-text"]').click();
                #Manage the exception
                except NoSuchElementException as e:
                        print("Exception captureted: " + repr(e))
                # Suspends execution of the current thread for a 5 seconds.
                sleep(5)
                #Obtain the web element associated to the attributes
                list_key_elements = self.driver.find_elements_by_class_name("columnWithName")
                # Suspends execution of the current thread for a 2 seconds
                sleep(2)
                #Obtain the web element associated to the values of attributes
                list_value_elements= self.driver.find_elements_by_class_name("indexValueTd")
                # Suspends execution of the current thread for a 5 seconds
                sleep(5)

                #Create a list, that will contain the keys (attribute, obtained from web scraping)  of the dictionary
                list_keys_text= [elem.text for elem in list_key_elements ]

                # Create a list, that will contain the values (attribute, obtained from web scraping)  of the dictionary
                list_values_text=[elem.text for elem in list_value_elements]

                #Create a dict about all information about crime
                city_crime= dict(zip(list_keys_text, list_values_text))
                # Suspends execution of the current thread for a 5 seconds
                sleep(5)

                #return the dict with the information about crime of one city
                return city_crime


        #Method to scrape single city for the health attributes
        def scraper_singol_city_health(self, city):


                #Reduce the probabily to no finding web element
                self.driver.maximize_window()
                # write name of the city
                self.driver.find_element(By.ID, 'city_selector_menu_city_id').send_keys(city)
                # Suspends execution of the current thread for a 3 seconds
                sleep(3)
                # Select the city
                self.driver.find_element(By.CLASS_NAME, 'ui-menu-item').click()
                # Suspends execution of the current thread for a 5 seconds
                sleep(5)
                # Define the instruction that can generate a exception
                try:
                        self.driver.find_element_by_xpath('//span[@class = "ui-button-text"]').click();
                #Manage the exception
                except NoSuchElementException as e:
                        print("Exception captureted: " + repr(e))
                # Suspends execution of the current thread for a 5 seconds
                sleep(5)
                # Obtain the web element associated to the attributes
                list_key_elements = self.driver.find_elements_by_class_name("columnWithName")
                # Suspends execution of the current thread for a 2 seconds
                sleep(2)
                # Obtain the web element associated to the values of attributes
                list_value_elements = self.driver.find_elements_by_class_name("indexValueTd")
                # Suspends execution of the current thread for a 5 seconds
                sleep(5)
                # Create a list, that will contain the keys (attribute, obtained from web scraping)  of the dictionary
                list_keys_text = [elem.text for elem in list_key_elements]
                # Create a list, that will contain the values (attribute, obtained from web scraping)  of the dictionary
                list_values_text = [elem.text for elem in list_value_elements]
                # Create a dict about all information about health
                city_health = dict(zip(list_keys_text, list_values_text))

                # Suspends execution of the current thread for a 5 seconds
                sleep(5)

                # return the dict with the information about health of one city
                return city_health
                # Method to scrape single city for the health attributes

        #Method to scrape single city for the pollution attributes
        def scraper_singol_city_pollution(self, city):


                #Reduce the probabily to no finding web element
                self.driver.maximize_window()
                # write name of the city
                self.driver.find_element(By.ID, 'city_selector_menu_city_id').send_keys(city)
                # Suspends execution of the current thread for a 3 seconds
                sleep(3)
                # select the city
                self.driver.find_element(By.CLASS_NAME, 'ui-menu-item').click()
                # Suspends execution of the current thread for a 5 seconds
                sleep(5)
                # Define the instruction that can generate a exception
                try:
                        self.driver.find_element_by_xpath('//span[@class = "ui-button-text"]').click();
                # Manage the exception
                except NoSuchElementException as e:
                        print("Exception captureted: " + repr(e))
                # Suspends execution of the current thread for a 5 seconds
                sleep(5)
                # Obtain the web element associated to the attributes
                list_key_elements = self.driver.find_elements_by_class_name("columnWithName")
                # Suspends execution of the current thread for a 2 seconds
                sleep(2)
                # Obtain the web element associated to the values of attributes
                list_value_elements = self.driver.find_elements_by_class_name("indexValueTd")
                # Suspends execution of the current thread for a 5 seconds
                sleep(5)
                # Create a list, that will contain the keys (attribute, obtained from web scraping)  of the dictionary
                list_keys_text = [elem.text for elem in list_key_elements]
                # Create a list, that will contain the values (attribute, obtained from web scraping)  of the dictionary
                list_values_text = [elem.text for elem in list_value_elements]
                # Create a dict about all informations about pollution
                city_pollution = dict(zip(list_keys_text, list_values_text))

                # Suspends execution of the current thread for a 5 seconds
                sleep(5)

                # return the dict with the informations about pollution of one city
                return city_pollution

        # Method to scrape multiple cities for the attributes passed
        def scraper_multiple_city(self, name_attributes):
                # Suspends execution of the current thread for a 5 seconds
                sleep(5)
                """Create an instance of a web driver"""
                self.driver = Chrome(service=Service(self.chrome_driver))
                # Definition a link to connect the instance of web driver
                link = 'https://www.numbeo.com/pollution/'
                # Connect the instance of the web driver with the link
                self.driver.get(link)
                #Create  a dict to contain all couple key-value(attribute - value_attribute)
                cities_attributes= {}

                #iterate over list with the name of cities
                for city in ["Bari", "Lecce"]:
                        print("sono dentro 1")
                        #Check the value of name_attributes
                        if name_attributes == "Crime":
                                #Call the method singol_city_crime
                                city_value = self.scraper_single_city_crime(city)
                                #Add a new element to a dict
                                cities_attributes[city] = city_value
                                print("sono dentro 1")

                        elif name_attributes == "Health":
                                # Call the method scraper_singol_city_health
                                city_value = self.scraper_singol_city_health(city)
                                # Add a new element to a dict
                                cities_attributes[city] = city_value
                                # call the method scrapers_health_city
                        elif name_attributes == "Pollution":
                                # Call the method scraper_singol_city_health
                                city_value = self.scraper_singol_city_pollution(city)
                                # Add a new element to a dict
                                cities_attributes[city] = city_value
                #close the connection with driver
                self.driver.close()
                # Suspends execution of the current thread for a 5 seconds
                sleep(5)
                print(self._cities_list)
                # return the dict with the informations about pollution of all cities
                return cities_attributes

        #Method to scrape single city for the pollution attributes
        def scraper_all(self):
                #Define a list of attribute where to do web scraping
                list_attributes=["Crime","Health","Pollution"]

                #Iterate over list_attributes
                for attribute in list_attributes:

                        #scraper multiple
                        self._data[attribute] = self.scraper_multiple_city(attribute)

                # WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '//span[@class = "ui-button-text"]'))).click()

        # Method to write the dict data to a json file
        def show_dict(self):
                return self._data

        #Method to write the dict data to a json file
        def write_json(self):
            with open("data_scraping.json", "w") as file:
                 json.dump(self._data, file)


#Execute the script realized
if __name__ == "__main__":
        #Create an instance of class Scraper
        scraper = Scraper()


        #Call the method scraper all
        scraper.scraper_all()
        #Call the method write_json
        scraper.write_json()
        # Serializing json
        scraper.show_dict()
