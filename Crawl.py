import wikipedia
import pymysql
from sshtunnel import SSHTunnelForwarder

#Test commit from CLI
# Connect to local CentOS server running MariaDB
server = SSHTunnelForwarder(
    '192.168.86.153',
    ssh_username='x',
    ssh_password='x',
    remote_bind_address=('127.0.0.1', 3306)
)
server.start()

# Connect to MariaDB instance on server
cnx = pymysql.connect(
    host='127.0.0.1',
    port=server.local_bind_port,
    user='root',
    password='x',
    db='WebServer'
)

# Get title of a random article on Wikipedia
def getTitle():
    title = wikipedia.random(pages=1)
    return title

# Get first sentence of a summary of the article in the getTitle function
def getSummary(title):
    summary = wikipedia.summary(title, sentences=1)
    return summary

# TODO: Decide what to do with this data and plug it into my DB
i = 1
for i in range (1,5):
    title = getTitle()
    print(title)
    words = str.split(title)

    summary = getSummary(title)
    print(summary)
    sumWords = str.split(summary)

    print(words)
    print(sumWords)