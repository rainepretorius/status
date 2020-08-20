# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_quickstart]
import logging

from flask import Flask, render_template
import psycopg2
import socket
import urllib.request as request
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

authdbdb1 = None
authdbdb2 = None
blackjackdbdb1 = None
blackjackdbdb2 = None
covid19dbdb1 = None
covid19dbdb2 = None
helpdeskdbdb1 = None
helpdeskdbdb2 = None
liamdbdb1 = None
liamdbdb2 = None
lindendbdb1 = None
lindendbdb2 = None
sharesdbdb1 = None
sharesdbdb2 = None

errorlink = "/static/images/error.jpg"
workinglink = "/static/images/working.jpg"

http_error_dict = {100: ' 100 Continue', 101: ' 101 Switching Protocols', 102: '102 Processing', 103: '103 Early Hints',
                   200: '200 OK',
                   201: "201 Created", 202: "202 Accepted", 203: "203 Non-Authoritative Information",
                   204: "204 No Content", 205: "205 Reset Content", 206: "206 Partial Content", 207: "207 Multi-Status",
                   208: "208 Already Reported", 226: "226 IM Used", 400: "400 Bad Request", 401: "401 Unauthorized",
                   402: "402 Payment Required", 403: "403 Forbidden", 404: "404 Not Found",
                   405: "405 Method Not Allowed", 408: "408 Request Timeout", 500: "500 Internal Server Error",
                   501: "501 Not Implemented", 502: "502 Bad Gateway", 503: "503 Service Unavailable"}


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/all_services', methods=['get'])
def all_services():
    """
    DOCSTRING : Checks the status of all the services.
    :return: all_services1.html
    """
    """
    Database 1
    """

    try:
        server1 = psycopg2.connect(user='Python', password='VVd%MBK0i@8#86GJibThMi2sE&e*tb', host='db1.pretoriusse.net',
                                   port='5432', database='Linden')
        s1cursor = server1.cursor()
        s1cursor.execute("SELECT * FROM leerder_ouers")
        s1cursor.close()
        server1.close()
        db1 = "This database server is working."
        db1link = workinglink
    except psycopg2.Error as error:
        db1 = "This database server has the following error : \n\n" + str(error)
        db1link = errorlink
    except Exception as er:
        db1 = er
        db1link = errorlink

    """
    Database 2
    """

    try:
        server1 = psycopg2.connect(user='Python', password='VVd%MBK0i@8#86GJibThMi2sE&e*tb', host='db2.pretoriusse.net',
                                   port='5432', database='Blackjack')
        s1cursor = server1.cursor()
        s1cursor.execute("SELECT * FROM player_chips")
        s1cursor.close()
        server1.close()
        db2 = "This database server is working."
        db2link = workinglink
    except psycopg2.Error as error:
        db2 = "This database server has the following error : \n\n" + str(error)
        db2link = errorlink
    except Exception as er:
        db2 = er
        db2link = errorlink

    """
    Covid Vraelys
    """

    try:
        url = "https://covid.pretoriusse.net"
        status = request.urlopen(url=url, timeout=10)
        stcovid = status.getcode()
        covidstatus = http_error_dict[stcovid]
        if int(stcovid) == 200:
            covidlink = workinglink
        else:
            covidlink = errorlink
    except socket.timeout:
        covidstatus = "Could not connect to check status. Connection Timed Out."
        covidlink = errorlink
    except ConnectionRefusedError:
        covidstatus = "Could not connect to check status. Connection Refused."
        covidlink = errorlink
    except Exception as ex:
        covidlink = errorlink
        covidstatus = "Exception : " + str(ex)


    """
    Helpdesk
    """

    try:
        url = 'https://helpdesk.pretoriusse.net:80/'
        status = request.urlopen(url=url, timeout=10)
        sthelpdesk = status.getcode()
        helpdeskstatus = http_error_dict[sthelpdesk]
        if sthelpdesk == 200:
            helpdesklink = workinglink
        else:
            helpdesklink = errorlink
    except socket.timeout:
        helpdeskstatus = "Could not connect to check status. Connection Timed Out."
        helpdesklink = errorlink
    except ConnectionRefusedError:
        helpdeskstatus = "Could not connect to check status. Connection Refused."
        helpdesklink = errorlink
    except ssl.SSLError:
        helpdeskstatus = http_error_dict[200]
        helpdesklink = workinglink
    except Exception as ex1:
        helpdesklink = errorlink
        helpdeskstatus = "Exception : " + str(ex1)

    """
    Helpdesk Admin
    """

    try:
        url = 'https://helpdesk.pretoriusse.net:82/'
        status = request.urlopen(url=url, timeout=10)
        sthelpdeskadmin = status.getcode()
        helpdeskadminstatus = sthelpdeskadmin
        if sthelpdeskadmin == 200:
            helpdeskadminlink = workinglink
        else:
            helpdeskadminlink = errorlink
    except socket.timeout:
        helpdeskadminstatus = "Could not connect to check status. Connection Timed Out."
        helpdeskadminlink = errorlink
    except ConnectionRefusedError:
        helpdeskadminstatus = "Could not connect to check status. Connection Refused."
        helpdeskadminlink = errorlink
    except Exception as ex2:
        helpdeskadminlink = errorlink
        helpdeskadminstatus = "Exception : " + str(ex2)

    """
    Plex
    """

    try:
        url = 'https://plex.fsrl.pretoriusse.net:32400/web/index.html#'
        status = request.urlopen(url=url, timeout=10)
        stplex = status.getcode()
        plexstatus = http_error_dict[stplex]
        if stplex == 200:
            plexlink = workinglink
        else:
            plexlink = errorlink
    except socket.timeout:
        plexstatus = "Could not connect to check status. Connection Timed Out."
        plexlink = errorlink
    except ConnectionRefusedError:
        plexstatus = "Could not connect to check status. Connection Refused."
        plexlink = errorlink
    except Exception as ex3:
        plexlink = errorlink
        plexstatus = "Exception : " + str(ex3)

    """
    Pensioen Calculator"""

    try:
        url = 'http://dehothouse.pretoriusse.net/'
        status = request.urlopen(url=url, timeout=10)
        stpensioen = status.getcode()
        pensioenstatus = http_error_dict[stpensioen]
        if stpensioen == 200:
            pensioenlink = workinglink
        else:
            pensioenlink = errorlink
    except socket.timeout:
        pensioenstatus = "Could not connect to check status. Connection Timed Out."
        pensioenlink = errorlink
    except ConnectionRefusedError:
        pensioenstatus = "Could not connect to check status. Connection Refused."
        pensioenlink = errorlink
    except Exception as ex4:
        pensioenlink = errorlink
        pensioenstatus = "Exception : " + str(ex4)

    db1data = [(db1link, db1)]
    db2data = [(db2link, db2)]
    coviddata = [(covidlink, covidstatus)]
    helpdeskdata = [(helpdesklink, helpdeskstatus)]
    helpdeskdataadmin = [(helpdeskadminlink, helpdeskadminstatus)]
    plexdata = [(plexlink, plexstatus)]
    pensioendata = [(pensioenlink, pensioenstatus)]

    return render_template("all_services.html", db1data=db1data, db2data=db2data, coviddata=coviddata, helpdeskdata=helpdeskdata,
                           helpdeskadmindata=helpdeskdataadmin, plexdata=plexdata, pensioendata=pensioendata)

@app.route("/database_1")
def database1():
    """
    DOCSTRING : Checks what databases work on database server 1.
    :return: database1-Copy.html
    """
    """
    Linden Database
    """
    try:
        server1 = psycopg2.connect(user='Python', password='VVd%MBK0i@8#86GJibThMi2sE&e*tb', host='db1.pretoriusse.net',
                                   port='5432', database='Linden')
        s1cursor = server1.cursor()
        s1cursor.execute("SELECT * FROM leerder_ouers")
        s1cursor.close()
        server1.close()
        lindendbdb1 = "This database is working."
        lindendbdb1link = workinglink
    except psycopg2.Error as error:
        lindendbdb1 = "This database on database server 1 has the following error : \n\n" + str(error)
        lindendbdb1link = errorlink

    """
    Authentication Database
    """

    try:
        server1 = psycopg2.connect(user='Python', password='VVd%MBK0i@8#86GJibThMi2sE&e*tb', host='db1.pretoriusse.net',
                                   port='5432', database='Authentication')
        s1cursor = server1.cursor()
        s1cursor.execute("SELECT * FROM website")
        s1cursor.close()
        server1.close()
        authdbdb1 = "This database is working."
        authdbdb1link = workinglink
    except psycopg2.Error as error:
        authdbdb1 = "This database on database server 1 has the following error : \n\n" + str(error)
        authdbdb1link = errorlink

    """
    Blackjack Database
    """

    try:
        server1 = psycopg2.connect(user='Python', password='VVd%MBK0i@8#86GJibThMi2sE&e*tb', host='db1.pretoriusse.net',
                                   port='5432', database='Blackjack')
        s1cursor = server1.cursor()
        s1cursor.execute("SELECT * FROM player_chips")
        s1cursor.close()
        server1.close()
        blackjackdbdb1 = "This database is working."
        blackjackdbdb1link = workinglink
    except psycopg2.Error as error:
        blackjackdbdb1 = "This database on database server 1 has the following error : \n\n" + str(error)
        blackjackdbdb1link = errorlink

    """
    Covid19 Database
    """

    try:
        server1 = psycopg2.connect(user='Python', password='VVd%MBK0i@8#86GJibThMi2sE&e*tb', host='db1.pretoriusse.net',
                                   port='5432', database='Covid19')
        s1cursor = server1.cursor()
        s1cursor.execute("SELECT * FROM leerder_oggend")
        s1cursor.close()
        server1.close()
        covid19dbdb1 = "This database is working."
        covid19dbdb1link = workinglink
    except psycopg2.Error as error:
        covid19dbdb1 = "This database on database server 1 has the following error : \n\n" + str(error)
        covid19dbdb1link = errorlink

    """
    Helpdesk Database
    """

    try:
        server1 = psycopg2.connect(user='Python', password='VVd%MBK0i@8#86GJibThMi2sE&e*tb', host='db1.pretoriusse.net',
                                   port='5432', database='Helpdesk')
        s1cursor = server1.cursor()
        s1cursor.execute("SELECT * FROM open")
        s1cursor.close()
        server1.close()
        helpdeskdbdb1 = "This database is working."
        helpdeskdbdb1link = workinglink
    except psycopg2.Error as error:
        helpdeskdbdb1 = "This database on database server 1 has the following error : \n\n" + str(error)
        helpdeskdbdb1link = errorlink

    """
    Shares Database
    """

    try:
        server1 = psycopg2.connect(user='Python', password='VVd%MBK0i@8#86GJibThMi2sE&e*tb', host='db1.pretoriusse.net',
                                   port='5432', database='Shares')
        s1cursor = server1.cursor()
        s1cursor.execute("SELECT * FROM altron")
        s1cursor.close()
        server1.close()
        sharesdbdb1 = "This database is working."
        sharesdbdb1link = workinglink
    except psycopg2.Error as error:
        sharesdbdb1 = "This database on database server 1 has the following error : \n\n" + str(error)
        sharesdbdb1link = errorlink

    db1data = [(authdbdb1link, "Authentication", authdbdb1), (blackjackdbdb1link, "Blackjack", blackjackdbdb1),
               (covid19dbdb1link, "Covid19", covid19dbdb1),
               (helpdeskdbdb1link, "Helpdesk", helpdeskdbdb1), (lindendbdb1link, "Linden", lindendbdb1),
               (sharesdbdb1link, "Shares", sharesdbdb1)]
    return render_template("database1.html", data=db1data)

@app.route("/database_2")
def database2():
    """
    DOCSTRING : Checks what databases work on database server 2.
    :return: database2.html
    """
    """
    Linden Database
    """
    try:
        server1 = psycopg2.connect(user='Python', password='VVd%MBK0i@8#86GJibThMi2sE&e*tb', host='db2.pretoriusse.net',
                                   port='5432', database='Linden')
        s1cursor = server1.cursor()
        s1cursor.execute("SELECT * FROM leerder_ouers")
        s1cursor.close()
        server1.close()
        lindendbdb2 = "This database is working."
        lindendbdb2link = workinglink
    except psycopg2.Error as error:
        lindendbdb2 = "This database on database server 2 has the following error : \n\n" + str(error)
        lindendbdb2link = errorlink

    """
    Authentication Database
    """

    try:
        server1 = psycopg2.connect(user='Python', password='VVd%MBK0i@8#86GJibThMi2sE&e*tb', host='db2.pretoriusse.net',
                                   port='5432', database='Authentication')
        s1cursor = server1.cursor()
        s1cursor.execute("SELECT * FROM website")
        s1cursor.close()
        server1.close()
        authdbdb2 = "This database is working."
        authdbdb2link = workinglink
    except psycopg2.Error as error:
        authdbdb2 = "This database on database server 2 has the following error : \n\n" + str(error)
        authdbdb2link = errorlink

    """
    Blackjack Database
    """

    try:
        server1 = psycopg2.connect(user='Python', password='VVd%MBK0i@8#86GJibThMi2sE&e*tb', host='db2.pretoriusse.net',
                                   port='5432', database='Blackjack')
        s1cursor = server1.cursor()
        s1cursor.execute("SELECT * FROM player_chips")
        s1cursor.close()
        server1.close()
        blackjackdbdb2 = "This database is working."
        blackjackdbdb2link = workinglink
    except psycopg2.Error as error:
        blackjackdbdb2 = "This database on database server 2 has the following error : \n\n" + str(error)
        blackjackdbdb2link = errorlink

    """
    Covid19 Database
    """

    try:
        server1 = psycopg2.connect(user='Python', password='VVd%MBK0i@8#86GJibThMi2sE&e*tb', host='db2.pretoriusse.net',
                                   port='5432', database='Covid19')
        s1cursor = server1.cursor()
        s1cursor.execute("SELECT * FROM leerder_oggend")
        s1cursor.close()
        server1.close()
        covid19dbdb2 = "This database is working."
        covid19dbdb2link = workinglink
    except psycopg2.Error as error:
        covid19dbdb2 = "This database on database server 2 has the following error : \n\n" + str(error)
        covid19dbdb2link = errorlink

    """
    Helpdesk Database
    """

    try:
        server1 = psycopg2.connect(user='Python', password='VVd%MBK0i@8#86GJibThMi2sE&e*tb', host='db2.pretoriusse.net',
                                   port='5432', database='Helpdesk')
        s1cursor = server1.cursor()
        s1cursor.execute("SELECT * FROM open")
        s1cursor.close()
        server1.close()
        helpdeskdbdb2 = "This database is working."
        helpdeskdbdb2link = workinglink
    except psycopg2.Error as error:
        helpdeskdbdb2 = "This database on database server 2 has the following error : \n\n" + str(error)
        helpdeskdbdb2link = errorlink

    """
    Shares Database
    """

    try:
        server1 = psycopg2.connect(user='Python', password='VVd%MBK0i@8#86GJibThMi2sE&e*tb', host='db2.pretoriusse.net',
                                   port='5432', database='Shares')
        s1cursor = server1.cursor()
        s1cursor.execute("SELECT * FROM altron")
        s1cursor.close()
        server1.close()
        sharesdbdb2 = "This database is working."
        sharesdbdb2link = workinglink
    except psycopg2.Error as error:
        sharesdbdb2 = "This database on database server 2 has the following error : \n\n" + str(error)
        sharesdbdb2link = errorlink

    db2data = [(authdbdb2link, "Authentication", authdbdb2), (blackjackdbdb2link, "Blackjack", blackjackdbdb2),
               (covid19dbdb2link, "Covid19", covid19dbdb2),
               (helpdeskdbdb2link, "Helpdesk", helpdeskdbdb2), (lindendbdb2link, "Linden", lindendbdb2),
               (sharesdbdb2link, "Shares", sharesdbdb2)]
    return render_template("database2.html", data=db2data)


@app.route("/web_apps")
def web_apps():
    """
    DOCSTRING : Checks the status of web apps.
    :return:
    """
    """
    Covid Vraelys
    """

    try:
        url = "https://covid.pretoriusse.net"
        status = request.urlopen(url=url, timeout=10)
        stcovid = status.getcode()
        covidstatus = http_error_dict[stcovid]
        if int(stcovid) == 200:
            covidlink = workinglink
        else:
            covidlink = errorlink
    except socket.timeout:
        covidstatus = "Could not connect to check status. Connection Timed Out."
        covidlink = errorlink
    except ConnectionRefusedError:
        covidstatus = "Could not connect to check status. Connection Refused."
        covidlink = errorlink
    except Exception as ex:
        covidlink = errorlink
        covidstatus = "Exception : " + str(ex)


    """
    Helpdesk
    """

    try:
        url = 'https://helpdesk.pretoriusse.net:80/'
        status = request.urlopen(url=url, timeout=10)
        sthelpdesk = status.getcode()
        helpdeskstatus = http_error_dict[sthelpdesk]
        if sthelpdesk == 200:
            helpdesklink = workinglink
        else:
            helpdesklink = errorlink
    except socket.timeout:
        helpdeskstatus = "Could not connect to check status. Connection Timed Out."
        helpdesklink = errorlink
    except ConnectionRefusedError:
        helpdeskstatus = "Could not connect to check status. Connection Refused."
        helpdesklink = errorlink
    except ssl.SSLError:
        helpdeskstatus = http_error_dict[200]
        helpdesklink = workinglink
    except Exception as ex1:
        helpdesklink = errorlink
        helpdeskstatus = "Exception : " + str(ex1)

    """
    Helpdesk Admin
    """

    try:
        url = 'https://helpdesk.pretoriusse.net:82/'
        status = request.urlopen(url=url, timeout=10)
        sthelpdeskadmin = status.getcode()
        helpdeskadminstatus = sthelpdeskadmin
        if sthelpdeskadmin == 200:
            helpdeskadminlink = workinglink
        else:
            helpdeskadminlink = errorlink
    except socket.timeout:
        helpdeskadminstatus = "Could not connect to check status. Connection Timed Out."
        helpdeskadminlink = errorlink
    except ConnectionRefusedError:
        helpdeskadminstatus = "Could not connect to check status. Connection Refused."
        helpdeskadminlink = errorlink
    except Exception as ex2:
        helpdeskadminlink = errorlink
        helpdeskadminstatus = "Exception : " + str(ex2)

    """
    Plex
    """

    try:
        url = 'https://plex.fsrl.pretoriusse.net:32400/web/index.html#'
        status = request.urlopen(url=url, timeout=10)
        stplex = status.getcode()
        plexstatus = http_error_dict[stplex]
        if stplex == 200:
            plexlink = workinglink
        else:
            plexlink = errorlink
    except socket.timeout:
        plexstatus = "Could not connect to check status. Connection Timed Out."
        plexlink = errorlink
    except ConnectionRefusedError:
        plexstatus = "Could not connect to check status. Connection Refused."
        plexlink = errorlink
    except Exception as ex3:
        plexlink = errorlink
        plexstatus = "Exception : " + str(ex3)

    """
    Pensioen Calculator"""

    try:
        url = 'http://dehothouse.pretoriusse.net/'
        status = request.urlopen(url=url, timeout=10)
        stpensioen = status.getcode()
        pensioenstatus = http_error_dict[stpensioen]
        if stpensioen == 200:
            pensioenlink = workinglink
        else:
            pensioenlink = errorlink
    except socket.timeout:
        pensioenstatus = "Could not connect to check status. Connection Timed Out."
        pensioenlink = errorlink
    except ConnectionRefusedError:
        pensioenstatus = "Could not connect to check status. Connection Refused."
        pensioenlink = errorlink
    except Exception as ex4:
        pensioenlink = errorlink
        pensioenstatus = "Exception : " + str(ex4)

    webappdata = [(covidlink, "Linden Covid Vraelys", covidstatus), (helpdesklink, "Pretorius Helpdesk", helpdeskstatus),
               (helpdeskadminlink, "Pretorius Helpdesk Admin Portal", helpdeskadminstatus),
               (plexlink, "Plex - FSrl", plexstatus), (pensioenlink, "Pensioen Calculator", pensioenstatus)]
    return render_template("webapps.html", data=webappdata)


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
