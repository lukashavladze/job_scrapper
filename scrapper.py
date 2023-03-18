import requests
from bs4 import BeautifulSoup
import json

# word to search in jobs sites
# search_word = input("Please enter your search word: ")
search_word = "python"   # Todo delete it
# first site jobs.ge
url = 'https://jobs.ge/?page=1&q={0}&cid=&lid=&jid='.format(search_word)
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
results = soup.find_all('a', class_='vip')

# making list for all jobs and links
vacancy_list = []

# extracting results and adding to list
for result in results:
    a = result.text
    sites_links = result.get('href')
    b = ("https://jobs.ge" + sites_links)
    vacancy_list.append([a, b])

# second site hr.ge
hr_url = 'https://www.hr.ge/search-posting?q={}'.format(search_word)
page1 = requests.get(hr_url)
soup1 = BeautifulSoup(page1.text, 'html.parser')
results1 = soup1.find_all('a', class_='title')
# print(results1)

for result1 in results1:
    a1 = result1.text
    links = result1.get('href')
    b1 = ("https://www.hr.ge" + links)
    vacancy_list.append([a1, b1])


# third site ss.ge
ss_url = "https://ss.ge/ka/jobs/l?IsEducation=false&EmployerType=0&MonthOrDay=0&JobsDealTypeId=1&Fields%5B0%5D.FieldId=49&Fields%5B0%5D.Type=SingleSelect&Fields%5B0%5D.StandardField=None&Fields%5B1%5D.FieldId=75&Fields%5B1%5D.Type=0&Fields%5B1%5D.StandardField=none&Fields%5B1%5D.FieldId=75&Fields%5B1%5D.Type=0&Fields%5B1%5D.StandardField=none&Fields%5B1%5D.FieldId=71&Fields%5B1%5D.Type=0&Fields%5B1%5D.StandardField=none&Fields%5B1%5D.FieldId=53&Fields%5B1%5D.Type=0&Fields%5B1%5D.StandardField=none&Fields%5B1%5D.FieldId=77&Fields%5B1%5D.Type=0&Fields%5B1%5D.StandardField=none&Query={}".format(search_word)
page2 = requests.get(ss_url)
soup2 = BeautifulSoup(page2.text, 'html.parser')
results2 = soup2.find_all(class_='latest_title')
results3 = soup2.find_all(class_="jobs_latest_article_each-link")
# print(results2)

vacancy_list2 = []
vacancy_list3 = []

for result3 in results3:
    links = result3.get('href')
    b3 = ("https://ss.ge" + links)
    vacancy_list.append(b3)


for result2 in results2:
    a3 = result2.text.strip("\n")
    if [a3] not in vacancy_list:
        vacancy_list.append([a3])


def add_list(list1, list2):
    for z in range(len(list1)):
        list1[z].append(list2[z])
    return list1


# combining ss.ge 2 lists into one.
a = add_list(vacancy_list2, vacancy_list3)

# appending our main vacancy list ss.ge combined list
for i in range(len(a)):
    vacancy_list.append(a[i])

# first time needs to be active to write vacancies!!!
# with open('vacancy_links.json', 'r+', encoding='utf-8') as vac:
#     json.dump(vacancy_list, vac, ensure_ascii=False)

with open('vacancy_links.json', 'r+', encoding='utf-8') as vac:
    data = json.load(vac)
    for item in vacancy_list:
        # print(item)
        if item in data:
            print("old vacancy>>>", item)
        else:
            json.dump(item, vac, ensure_ascii=False)
            print("new vacancy", item)


