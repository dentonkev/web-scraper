from bs4 import BeautifulSoup

with open('../personal-portfolio/index.html', 'r') as file:
    html = BeautifulSoup(file, 'html.parser')
    section = html.section

    print(section['id'])
    print(section.attrs)