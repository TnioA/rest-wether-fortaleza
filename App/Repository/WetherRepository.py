from flask import Flask
from bs4 import BeautifulSoup
from App.Model.WetherModel import WetherModel
import requests
import json
import os
import collections

class WetherRepository:
    def __init__(self):
        self.html_doc = requests.get("https://weather.com/weather/today/l/-3.73,-38.52?par=google&temp=c")
        self.soup = BeautifulSoup(self.html_doc.text, "html.parser")
    
    def GetWether(self):
        responseModel = WetherModel()
    
        contentList = self.soup.find_all("section")

        responseModel.Title = contentList[2].find("h1").text.strip()
        responseModel.CheckTime = contentList[2].find("div").find("div", class_="CurrentConditions--timestamp--1SWy5").text.strip()
        responseModel.Temperature = contentList[2].find("div", class_="CurrentConditions--primary--3xWnK").find("span").text.strip()
        responseModel.State = contentList[2].find("div", class_="CurrentConditions--primary--3xWnK").find("div").text.strip()
        responseModel.Description = contentList[2].find("div", class_="CurrentConditions--primary--3xWnK").find("div").text.strip()
        responseModel.FeelsLike = contentList[5].find("span", class_="TodayDetailsCard--feelsLikeTempValue--2aogo").text.strip()
        
        auxBox = contentList[5].find_all("div", class_="WeatherDetailsListItem--wxData--23DP5")

        responseModel.HighLow = auxBox[0].text.strip()
        responseModel.Wind = auxBox[1].find('span').text.strip()
        responseModel.Humidity = auxBox[2].find('span').text.strip()
        responseModel.Pressure = auxBox[4].find('span').text.strip()
        responseModel.Visibility = auxBox[6].text.strip()
        responseModel.MoonPhase = auxBox[7].text.strip()
        
        auxBox = contentList[3].find("ul")
        responseModel.DailyValues = []
        for item in auxBox.find_all("li"):
            responseModel.DailyValues.append({
                'Period': item.find("h3").find("span").text.strip(),
                'Temperature': item.find("div", class_="Column--temp--2v_go").find("span").text.strip(),
                'RainChance': item.find("div", class_="Column--precip--2H5Iw").find("span").text.strip().replace("Chance of Rain", ""),
            })

        auxBox = contentList[6].find("ul")
        responseModel.HourlyValues = []
        for item in auxBox.find_all("li"):
            responseModel.HourlyValues.append({
                'Period': item.find("h3").find("span").text.strip(),
                'Temperature': item.find("div", class_="Column--temp--2v_go").find("span").text.strip(),
                'RainChance': item.find("div", class_="Column--precip--2H5Iw").find("span").text.strip().replace("Chance of Rain", ""),
            })

        auxBox = contentList[7].find("ul")
        responseModel.TodayValues = []
        for item in auxBox.find_all("li"):
            responseModel.TodayValues.append({
                'Period': item.find("h3").find("span").text.strip(),
                'Temperature': item.find("div", class_="Column--temp--2v_go").find("span").text.strip(),
                'RainChance': item.find("div", class_="Column--precip--2H5Iw").find("span").text.strip().replace("Chance of Rain", ""),
            })

        return responseModel
