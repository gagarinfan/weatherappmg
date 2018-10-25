# WeatherApp
This repo has been moved from my private Bitbucket repository.

## About app

Hi! This is my first simple python app that connects to [weaterunderground](https://www.wunderground.com/) API and checks for the weather. I decided to create this simple app because as DevOps engineer I wanted to know not only how to deploy applications on Docker but how to create dockerized apps, as well. So this repo also includes Dockerfile and Jenkinsfile.


## Usage

### Files
- [app.py](app.py) - main file for executing app
- [Forecast.py](Class/Forecast.py) - class for checking weather
- [SendMail.py](Class/SendMail.py) - class for sending mail via gmail
- [token.txt](token.txt) - place where token to API is stored
- [Jsons](Jsons) - catalog where I store API response example
- [Dockerfile](Dockerfile) and [Jenkinsfile](Jenkinsfile) - files I need to create container from my app and automate deployment 

### Concept 
- Need to have token to connect wunderground's API
- Application send mail every day at 6:45 AM with weather forecast:
```python
sched.add_job(get_today_weather, 'cron', [hourly, current], hour=6, minute=45)
```
- Every 30 minutes app get forecast for next hour between 7AM and 8PM:
```python
sched.add_job(get_rain_forecast, 'cron', [hourly, current], hour='7-20', minute='0,30')
```
- If possibility of rain is more than 60% and it's not currently raining app send mail with alert:
```python
        if int(rain_forecast) >= 60 and previous == 0:
            print("Rain forecast", rain_forecast, "so I'm sending mail", previous)
            return rain_forecast
        elif int(rain_forecast) >= 60 and previous == 1:
            print("Rain forecast", rain_forecast, "but it has already been raining", previous)
            return 1
        else:
            print("Rain forecast", rain_forecast, "doesn't rain", previous)
            return 0
```