import time

import requests


############################################################################################
class Forecast(object):
    def __init__(self, link_hourly, link_conditions, link_history):
        self.link_hourly = link_hourly
        self.link_conditions = link_conditions
        self.link_history = link_history

    def get_json(self, link):
        response = requests.get(link)
        data = response.json()
        return data

    def get_previous(self):
        data = self.get_json(self.link_history)
        previous = data['history']['observations'][-2]['rain']
        return previous

    def get_weather_forecast(self):
        data = self.get_json(self.link_conditions)
        today_forecast = data["forecast"]["txt_forecast"]["forecastday"][0]["fcttext_metric"]
        return today_forecast

    def get_actual_weather(self):
        data = self.get_json(self.link_conditions)
        current = data["current_observation"]["temp_c"]
        return current

    def get_rain_forecast(self):
        previous = int(self.get_previous())
        try:
            data = self.get_json(self.link_hourly)
            rain_forecast = data["hourly_forecast"][0]["pop"]

        except IndexError:
            print("Index error. Will try again after a few seconds")
            time.sleep(120)
            rain_forecast = data["hourly_forecast"][0]["pop"]

        if int(rain_forecast) >= 60 and previous == 0:
            print("Rain forecast", rain_forecast, "so I'm sending mail", previous)
            return rain_forecast
        elif int(rain_forecast) >= 60 and previous == 1:
            print("Rain forecast", rain_forecast, "but it has already been raining", previous)
            return 1
        else:
            print("Rain forecast", rain_forecast, "doesn't rain", previous)
            return 0