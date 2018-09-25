#http://wdi.worldbank.org/table/2.7
import html
from html.entities import html5
from urllib.request import urlopen
import html5lib

from bs4 import BeautifulSoup


def rankingStudentsForTeachers():

    url = 'http://wdi.worldbank.org/table/2.7'

    html_parse = urlopen(url)

    soup = BeautifulSoup(html_parse, 'html.parser')

    tabela = soup.findAll('table',{'class':'indicators-table'})[1]

    linhas = tabela.findAll('tr')

    object = {}

    for linha in linhas:
        pais = linha.find('td', {'class': 'country'}).text

        object[pais] = {}

        investiment = linha.findAll('td')[7].text

        object[pais]['investimento'] = investiment

        aluno_por_professor = linha.findAll('td')[11].text
        object[pais]['alunos_por_professor'] = aluno_por_professor

    print('Brasil', object['Brazil']['investimento'], object['Brazil']['alunos_por_professor'])
    print('Suíca', object['Switzerland']['investimento'], object['Switzerland']['alunos_por_professor'])
    print('Alemanha', object['Germany']['investimento'], object['Germany']['alunos_por_professor'])
    print('Japão', object['Japan']['investimento'], object['Japan']['alunos_por_professor'])
    print('Áustria', object['Austria']['investimento'], object['Austria']['alunos_por_professor'])

def rankingCountrys():

    url = 'http://wdi.worldbank.org/table/2.7'

    html_parse = urlopen(url)

    soup = BeautifulSoup(html_parse, 'html.parser')

    tabela = soup.findAll('table',{'class':'indicators-table'})[1]

    linhas = tabela.findAll('tr')

    object = {}

    for linha in linhas:

        pais = linha.find('td',{'class':'country'}).text

        object[pais] = {}

        investiment = linha.findAll('td')[7].text

        object[pais]['investimento'] = investiment

    print('Brasil', object['Brazil']['investimento'])
    print('Suíca', object['Switzerland']['investimento'])
    print('Alemanha', object['Germany']['investimento'])
    print('Japão', object['Japan']['investimento'])
    print('Áustria', object['Austria']['investimento'])

#rankingCountrys()

#rankingStudentsForTeachers()


#films
def films_firs_name():
    url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

    html_parse = urlopen(url)

    html_soup = BeautifulSoup(html_parse, 'html.parser')

    #type(html_soup)
    movie_containers = html_soup.findAll('div',class_ = 'lister-item mode-advanced')

    first_film = movie_containers[0]
    first_name_film = first_film.h3.a.text
    print(first_name_film)

def year_movie():
    url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

    html_parse = urlopen(url)

    html_soup = BeautifulSoup(html_parse, 'html.parser')

    # type(html_soup)
    movie_containers = html_soup.findAll('div', class_='lister-item mode-advanced')

    first_film = movie_containers[0]
    first_year_movie  = first_film.h3.find('span',class_ = 'lister-item-year text-muted unbold')
    first_year_movie_text = first_year_movie.text
    print(first_year_movie_text)

def avaliation_imdb():
    url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

    html_parse = urlopen(url)

    html_soup = BeautifulSoup(html_parse, 'html.parser')

    # type(html_soup)
    movie_containers = html_soup.findAll('div', class_='lister-item mode-advanced')

    first_film = movie_containers[0]
    first_film_imdb = first_film.strong
    parse_float_first_film_imdb = float(first_film_imdb.text)
    print(parse_float_first_film_imdb)

# films_firs_name()
#year_movie()
#avaliation_imdb()

def clima_tempo():
    url = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.W6qDohRv_Qp'
    html_parse = urlopen(url)
    html_soup = BeautifulSoup(html_parse, 'html.parser')

    days = html_soup.find(id="seven-day-forecast")

    items = days.find_all(class_="tombstone-container")

    const =  items[0]

    # print(const.prettify())
    period = const.find(class_="period-name").text
    description =  const.find(class_="short-desc").text
    temperatura = const.find(class_="temp").text

    print(period)
    print(description)
    print(temperatura)

clima_tempo()