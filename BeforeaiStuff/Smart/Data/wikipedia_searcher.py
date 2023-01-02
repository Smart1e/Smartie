
#Attempts to use bs4 & requests to scrape wikipedia for the first paragraph of a given article
"""

import requests
from bs4 import BeautifulSoup


def search_wikipedia(string, web_id):
    response = requests.get(
	url=f"https://en.wikipedia.org/wiki/{string}",
        )
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #gets and print the response of the id element
    element = soup.find(id=web_id)
    print(element.string)
    
search_wikipedia(input("Enter search term:  "), input("Enter web id:  "))

"""

#Attempts to use the wikipedia module instead of bs4 & requests
num = 1
def test():
    global num
    print(f"test {num}")
    num = num + 1
    
    
import wikipedia

def info(topic: str, lines: int = 3):
    """Gives Information on the Topic"""
    
    try:
        data = wikipedia.summary(topic, sentences=lines)
        
    except wikipedia.exceptions.DisambiguationError as e:
        suggestions = []
        temp_num_var = 5
        for line in e.options:
            
            if temp_num_var > 0:
                suggestions.append(line)
                temp_num_var -= 1
                
        final_search = input(f"Please select one of these: {suggestions}?  ")
        data = wikipedia.summary(final_search, sentences=lines)
        return data
            
    
    else:
        print(data)
        return data
    
    
print(info(input("Enter search term:  ")))

"""
Making qui in figma
    """