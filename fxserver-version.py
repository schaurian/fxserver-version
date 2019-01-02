import requests
from bs4 import BeautifulSoup
import cherrypy


def get_version():
    page = requests.get('https://runtime.fivem.net/artifacts/fivem/build_client/master/')

    soup = BeautifulSoup(page.text, 'lxml')

    rows = soup.find_all('a')


    highest_version_number = 0
    for row in rows:

        try:
            version_number = int(row.string.split('-')[0])
        except ValueError:
            version_number = 0

        if version_number > highest_version_number:
            highest_version_number = version_number
            highest_version = row.string

    return(highest_version)

cherrypy.config.update({'environment': 'production', 'server.socket_host': '0.0.0.0',})

class version(object):
    @cherrypy.expose
    def index(self):
        return(get_version())

cherrypy.quickstart(version())
