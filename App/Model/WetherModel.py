class WetherModel:
    def __init__(self = None, title = None, checkTime = None, temperature = None, state = None, 
    description = None, feelsLike = None, highLow = None, humidity = None, pressure = None, 
    wind = None, visibility = None, moonPhase = None, todayValues = [], dailyValues = [], hourlyValues = []):

        self.Title = title
        self.CheckTime = checkTime
        self.Temperature = temperature
        self.State = state
        self.Description = description
        self.FeelsLike = feelsLike
        self.HighLow = highLow
        self.Humidity = humidity
        self.Pressure = pressure
        self.Wind = wind
        self.Visibility = visibility
        self.MoonPhase = moonPhase
        self.TodayValues = todayValues
        self.DailyValues = dailyValues
        self.HourlyValues = hourlyValues