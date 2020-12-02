# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import json
import os
import collections

app = Flask(__name__)
CORS(app)

@app.route('/api/wether', methods=['GET'])
def Wether():
    html_doc = requests.get("https://weather.com/weather/today/l/-3.73,-38.52?par=google&temp=c")
    soup = BeautifulSoup(html_doc.text, "html.parser")

    # titles = soup.find("class", "CurrentConditions--header--3-4zi")
    # for dataBox in soup.find_all("tr", class_="rstable_td"):
    #     itens = dataBox.find_all("td")
    #     date = itens[0].text.strip()
    #     info = itens[1].text.strip().split("\t\t\t\t\t\t")
    #     concurse = info[0].replace("\n", "").strip()
    #     winners = info[1].replace("Ganhadores:", "").strip()
    #     value = info[2].replace("Prêmio:", "").strip()
    #     numbers = [item.text for item in itens[2].find_all("div")]

    return jsonify({ 
        'title': '',
        'checkTime': '',
        'temperature': '',
        'description': '',
        'feelsLike': '',
        'high/low': '',
        'humidity': '',
        'pressure': '',
        'wind': '',
        'moonPhase': '',
        'dailyValues': [],
        'hourlyValues': []
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
