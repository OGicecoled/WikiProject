import wikipedia
import pymysql
from sshtunnel import SSHTunnelForwarder

# TODO: Find way to pull out x number of longest records in DB and insert into variable

# Connect to local CentOS server running MariaDB
server = SSHTunnelForwarder(
    '192.168.86.153',
    ssh_username='ceverett',
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

cursor = cnx.cursor()

# Get title of a random article on Wikipedia. Pulls out first word of the title
def getTitle():
    title = wikipedia.random(pages=1)
    fullTitle = str.split(title)
    title = fullTitle[0]
    return title

# Get first sentence of a summary of the article in the getTitle function. I may try to incorporate this at some point.
def getSummary(title):
    summary = wikipedia.summary(title, sentences=1)
    return summary

# Insert the first word of the title into the database.
def queryTitle(title):
    query = "INSERT INTO SiteContent(PageText) VALUES (%s)"
    cursor.execute(query, (title))
    cnx.commit()

# Sort table by string length of the title and pulls out the largest record
def sortTest():
    query = "SELECT PageText FROM SiteContent ORDER BY CHAR_LENGTH(PageText) DESC;"
    cursor.execute(query)
    cnx.commit()
    record = cursor.fetchone()
    print(record)

# Closes DB and SSH connections
def closeConnection():
    cursor.close()
    cnx.close()
    server.close()

i = 1
for i in range (1,5):
    title = getTitle()
    print(title)
    queryTitle(title)

sortTest()
closeConnection()