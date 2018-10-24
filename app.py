import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from Classes.Forecast import Forecast
from Classes.SendMail import SendMail

sched = BlockingScheduler()
with open("token.txt") as f:
    token = f.readlines()
#######################################################################
def get_date():
    date = datetime.datetime.today().strftime('%Y%m%d')
    return date

def get_rain_forecast(hourly, current):
    date_now = ("http://api.wunderground.com/api/%s/history_%s/q/Poland/Wroclaw.json" % (token, get_date()))
    print(date_now,"\n",current,"\n",hourly)
    ###temp
    print(datetime.datetime.today().strftime('%Y%m%d-%H:%M'))
    rain_forecast = Forecast(hourly, current, date_now).get_rain_forecast()
    if int(rain_forecast) >= 2:
        Send("Warning!\n There is %s percent possibility that's going to rain within 1 hour.\n\n\nBest regards, Python" % (rain_forecast))

def get_today_weather(hourly, current):
    daily_forecast = Forecast(hourly, current, None).get_weather_forecast()
    actual = Forecast(hourly, current, None).get_actual_weather()
    Send("Current temperature: %s\nForecast for today: %s\n\n\nBest regards, Python" % (actual, daily_forecast))

def Send(body):
    SendMail("FROM WHO", "YOUR PASSWORD", "TO WHO", body).send()

def main():
    hourly = ("http://api.wunderground.com/api/%s/hourly/q/Poland/Wroclaw.json" %(token))
    current = ("http://api.wunderground.com/api/%s/conditions/forecast/q/Poland/Wroclaw.json" %(token))
    sched.add_job(get_rain_forecast, 'cron', [hourly, current], hour='7-20', minute='0,30')
    #sched.add_job(get_rain_forecast, 'interval', [hourly, current], minutes=2)

    sched.add_job(get_today_weather, 'cron', [hourly, current], hour=6, minute=45)
    sched.start()

if __name__ == "__main__":
    print("Starting", datetime.datetime.today().strftime('%Y%m%d-%H:%M'))
    main()
