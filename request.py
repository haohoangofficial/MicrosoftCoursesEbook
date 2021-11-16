import urllib.request
import os
from bs4 import BeautifulSoup



def main():
    # module_urls = extractCourseURL()
    # for module_url in module_urls:
    # extractModuleURL()
    extractPage()

def extractCourseURL():
    url = 'https://docs.microsoft.com/en-us/learn/paths/prepare-data-power-bi/'
    html_text = extractHTML(url)
    modules = html_text.findAll('a', class_='is-block text-decoration-none')
    module_urls = {}
    for module in modules:
        module_url = 'https://docs.microsoft.com/en-us/learn/' + module.get('href').replace('../..','')
        module_name = ((module.findAll('h3',class_='font-size-h6 margin-none has-content-margin-right-super-large-tablet'))[0]).get_text()
        module_urls[module_name] = module_url
    # print(module_urls)
    return module_urls

def extractModuleURL():
    url = 'https://docs.microsoft.com/en-us/learn/modules/get-data/'
    html_text = extractHTML(url)
    sub_modules = html_text.findAll('a',class_='unit-title is-block font-size-md has-line-height-reset')
    sub_module_urls = []
    for sub_module in sub_modules:
        sub_module_url = url + sub_module.get('href')
        sub_module_urls.append(sub_module_url)
    print((sub_module_urls))
    return sub_module_urls

def extractPage():
    url = 'https://docs.microsoft.com/en-us/learn/modules/get-data/1-introduction'

def extractHTML(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    encoding = response.headers.get_content_charset('utf-8')
    html_content = html.decode(encoding)
    html_text = BeautifulSoup(html_content,"html.parser")
    return html_text

def createFolder(parent,name):
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    path = ROOT_DIR + '/Book/' + parent + '/' + name + '/'
    os.mkdir(path)
if __name__ == '__main__':
    main()

