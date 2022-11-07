from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as web:
    content = web.read()

soup = BeautifulSoup(content, "html.parser")
# print(soup.title.string)

all_anchor = soup.find_all(name="a")
# print(all_anchor)
for tag in all_anchor:
    print(tag.getText())
    print(tag.get("href"))

company_url =  soup.select(selector="p a")
print(company_url)


