from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webdata = response.text
# print(webdata)


soup = BeautifulSoup(webdata, "html.parser")

film_names = []
films = soup.find_all(name="h3", class_="title")
for tag in films:
    tag_name = tag.getText()
    film_names.append(tag_name)

film_names.reverse()
print(film_names)

with open("100movies.txt", "a") as dat:
    for i in film_names:
        dat.write(f"{i} \n")






