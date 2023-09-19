from bs4 import BeautifulSoup as bs
import requests
import csv
author=[]
dict={}
for k in range(1,11,1):
    if k==1:
        response=requests.get('http://quotes.toscrape.com/')
    else:
        response= requests.get('http://quotes.toscrape.com/'+'/page/'+str(k)+'/')
    data= bs(response.text,'html.parser')

    lst=data.find_all(class_='author')
    for j in lst:
        author.append(j.string.strip())
        dict[j.string.strip()]=dict.get(j.string.strip(),0)+1
authors= sorted(set(author))
csv_file_path = "authors.csv"

# Write the data into the CSV file
with open(csv_file_path, mode="w", newline="",encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Authors Name"])  # Write header row
    writer.writerows([[movie] for movie in authors])

print("CSV file created successfully!")
