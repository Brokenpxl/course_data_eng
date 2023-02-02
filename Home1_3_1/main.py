#import requests as req
from bs4 import BeautifulSoup
import json
import tqdm
import json

data = {
    "data":[]
}


from requests_tor import RequestsTor
req = RequestsTor()



for page in range(0, 40):
    url = f"https://hh.ru/search/vacancy?text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post&area=113&customDomain=1&page={page}&hhtmFrom=vacancy_search_list"
    resp = req.get(url)

    soup = BeautifulSoup(resp.text, "lxml")
    tags = soup.find_all(attrs={"data-qa":"serp-item__title"})
    for iter in tqdm.tqdm(tags):
        
        url_object = iter.attrs["href"]
        resp_object = req.get(url_object)

        soup_object = BeautifulSoup(resp_object.text, "lxml")
        tag_exp = soup_object.find(attrs={"class":"vacancy-description-list-item"}).find(attrs={"data-qa":"vacancy-experience"}).text
        tag_price = soup_object.find(attrs={"data-qa":"vacancy-salary"}).find(attrs={"class":"bloko-header-section-2 bloko-header-section-2_lite"}).text

        tag_region = soup_object.find(attrs={"data-qa":"vacancy-serp__vacancy-address"}).text
        
        data["data"].append({
            "Title":iter.text,
            "work experience":tag_exp,
            "salary":tag_price,
            "region":tag_region
            })

        #print(iter.text,tag_exp,tag_price,tag_region)
        with open("data.json","w") as file:
            json.dump(data, file, ensure_ascii=False) 

    #soup = BeautifulSoup(html_target_page.text, 'lxml')
     #   for link in soup.find_all('div', class_='vacancy-serp-item-body'):
      #      title = link.find("a", {"data-qa": "serp-item__title"}).text
       #     salary = clean_html(link.find("span", {"data-qa": "vacancy-serp__vacancy-compensation"}))
        #    region = clean_html(link.find("div", {"data-qa": "vacancy-serp__vacancy-address"}))
         #   dict_to_write['data'].append({
          #      'title': title,
           #     'work experience': experiences_for_dict[n],
            #    'salary': salary,
             #   'region': region
            #})
            #with open(f'{n}_data_{experience}.json', 'w', encoding='utf-8') as file:
             #   json.dump(dict_to_write, file, ensure_ascii=False)
    #time.sleep(30)
    #print(len(dict_to_write['data']))
    #dict_to_write = {'data': []}