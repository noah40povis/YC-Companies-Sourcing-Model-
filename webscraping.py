import bs4 as bs
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 
import pandas as pd



url = 'https://yclist.com'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("tr", {"class":"operating"})
table = page_soup.findAll('div', {'id':'companies'})
data_frame = pd.read_html(str(table))[0]

data_frame.to_csv('yc_list.csv')
# for container in containers:
#     name = container.td[1].text  
#     url = container.td[2].text 
#     cohort = container.td[3].text
#     status = container.td[4].text
#     description = container.td[5].text
# print(containers[0].text    )

# # df = pd.read_html('https://yclist.com')
# # df[0]
# companies = containers[:].text
# for i in range(len(containers.text)): 
#     print(containers.text[i])
#     i += 1 