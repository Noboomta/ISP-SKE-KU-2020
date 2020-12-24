from os import name
from typing import List
from selenium import webdriver
import sys
import requests

def find_true_min_index(query, fragments):
    if(query == -1 and fragments == -1):
        return None
    elif(query == -1):
        return fragments
    elif(fragments == -1):
        return query
    else:
        return min(query, fragments)

def get_links(url: str):
    """Find all links on page at the given url.

       Returns:
          a list of all unique hyperlinks on the page,
          without page fragments or query parameters.
    """

    browser = webdriver.Firefox(executable_path=r'C:\Users\NoBoomTa\Desktop\Coding\geckodriver.exe')
    browser.get(url)

    elements = browser.find_elements_by_tag_name('a')

    new_element = []

    for element in elements:
        url_link = element.get_attribute('href')
        if(url_link != None):
            first_query = url_link.find('?')
            first_fragment = url_link.find('#')
            cut = find_true_min_index(first_query, first_fragment)
            link = ""
            if(cut == None):
                link = url_link
            else:
                link = url_link[0:cut]
            new_element.append(link)

    return list(set(new_element))

def is_valid_url(url: str):
    """check if the url is valid

    Returns:
        a boolean of the valid of the url.
    """

    try:
        req = requests.get(url)
        # print(req.status_code)
        return req.status_code == requests.codes['ok']
    except:
        return False

def invalid_urls(urllist: List[str]) -> List:
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    """

    invalid_urls_list = []
    for url in urllist:
        if not is_valid_url(url):
            invalid_urls_list.append(url)
    return invalid_urls_list

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print("Usage:  python3 link_scan.py url\n\nTest all hyperlinks on the given url.")
    else:
        url_link = sys.argv[1]
        if(is_valid_url(url= url_link)):
            all_link_list = get_links(url= url_link)
            print()
            for link in all_link_list:
                print(link)
            bad_link_list = invalid_urls(all_link_list)
            print()
            if(bad_link_list != []):
                print("Bad Links:")
                for bad_link in bad_link_list:
                    print(bad_link)
                print()
        else:
            print("Argument (the URL to check) is not an HTML page.")
