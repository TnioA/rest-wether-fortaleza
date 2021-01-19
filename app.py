# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import requests
import json
import os
import collections

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/api/wether', methods=['GET'])
def Wether():
    html_doc = requests.get("https://weather.com/weather/today/l/-3.73,-38.52?par=google&temp=c")
    soup = BeautifulSoup(html_doc.text, "html.parser")

    contentList = soup.find_all("section")

    title = contentList[2].find("h1").text.strip()
    checkTime = contentList[2].find("div").find("div", class_="CurrentConditions--timestamp--1SWy5").text.strip()
    temperature = contentList[2].find("div", class_="CurrentConditions--primary--3xWnK").find("span").text.strip()
    state = contentList[2].find("div", class_="CurrentConditions--primary--3xWnK").find("div").text.strip()
    description = contentList[2].find("div", class_="CurrentConditions--primary--3xWnK").find("div").text.strip()
    feelsLike = contentList[5].find("span", class_="TodayDetailsCard--feelsLikeTempValue--2aogo").text.strip()
    
    auxBox = contentList[5].find_all("div", class_="WeatherDetailsListItem--wxData--23DP5")
    highLow = auxBox[0].text.strip()
    wind = auxBox[1].find('span').text.strip()
    humidity = auxBox[2].find('span').text.strip()
    pressure = auxBox[4].find('span').text.strip()
    visibility = auxBox[6].text.strip()
    moonPhase = auxBox[7].text.strip()
    
    auxBox = contentList[3].find("ul")
    dailyValues = []
    for item in auxBox.find_all("li"):
        dailyValues.append({
            'Period': item.find("h3").find("span").text.strip(),
            'Temperature': item.find("div", class_="Column--temp--2v_go").find("span").text.strip(),
            'RainChance': item.find("div", class_="Column--precip--2H5Iw").find("span").text.strip().replace("Chance of Rain", ""),
        })

    auxBox = contentList[6].find("ul")
    hourlyValues = []
    for item in auxBox.find_all("li"):
        hourlyValues.append({
            'Period': item.find("h3").find("span").text.strip(),
            'Temperature': item.find("div", class_="Column--temp--2v_go").find("span").text.strip(),
            'RainChance': item.find("div", class_="Column--precip--2H5Iw").find("span").text.strip().replace("Chance of Rain", ""),
        })

    auxBox = contentList[7].find("ul")
    todayValues = []
    for item in auxBox.find_all("li"):
        todayValues.append({
            'Period': item.find("h3").find("span").text.strip(),
            'Temperature': item.find("div", class_="Column--temp--2v_go").find("span").text.strip(),
            'RainChance': item.find("div", class_="Column--precip--2H5Iw").find("span").text.strip().replace("Chance of Rain", ""),
        })

    return jsonify({ 
        'Title': title,
        'CheckTime': checkTime,
        'Temperature': temperature,
        'State': state,
        'Description': description,
        'FeelsLike': feelsLike,
        'HighLow': highLow,
        'Humidity': humidity,
        'Pressure': pressure,
        'Wind': wind,
        'Visibility': visibility,
        'MoonPhase': moonPhase,
        'TodayValues': todayValues,
        'DailyValues': dailyValues,
        'HourlyValues': hourlyValues
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)
