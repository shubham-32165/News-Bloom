    @app.route('/add_weather')
    def add_weather():  
        from .Models.Weather import Weather, Forcast, Time
        from datetime import datetime
        weather = Weather(
            location="Karnataka",
            date = datetime.now(),
            forcast = [
                Forcast( time = Time(hrs = 0, min = 0), temp = 25,  condition='clear'),
                Forcast( time = Time(hrs = 1, min = 0), temp = 24,  condition='clear'),
                Forcast( time = Time(hrs = 2, min = 0), temp = 24,  condition='clear'),
                Forcast( time = Time(hrs = 3, min = 0), temp = 24,  condition='clear'),
                Forcast( time = Time(hrs = 4, min = 0), temp = 24,  condition='clear'),
                Forcast( time = Time(hrs = 5, min = 0), temp = 23,  condition='clear'),
                Forcast( time = Time(hrs = 6, min = 0), temp = 23,  condition='clear'),
                Forcast( time = Time(hrs = 7, min = 0), temp = 24,  condition='clear'),
                Forcast( time = Time(hrs = 8, min = 0), temp = 26,  condition='clear'),
                Forcast( time = Time(hrs = 9, min = 0), temp = 28,  condition='cloudy'),
                Forcast( time = Time(hrs = 10, min = 0), temp = 30,  condition='cloudy'),
                Forcast( time = Time(hrs = 11, min = 0), temp = 31,  condition='cloudy'),
                Forcast( time = Time(hrs = 12, min = 0), temp = 33,  condition='clear'),
                Forcast( time = Time(hrs = 13, min = 0), temp = 34,  condition='clear'),
                Forcast( time = Time(hrs = 14, min = 0), temp = 34,  condition='clear'),
                Forcast( time = Time(hrs = 15, min = 0), temp = 32,  condition='clear'),
                Forcast( time = Time(hrs = 16, min = 0), temp = 31,  condition='clear'),
                Forcast( time = Time(hrs = 17, min = 0), temp = 29,  condition='clear'),
                Forcast( time = Time(hrs = 18, min = 0), temp = 28,  condition='rain'),
                Forcast( time = Time(hrs = 19, min = 0), temp = 27,  condition='rain'),
                Forcast( time = Time(hrs = 20, min = 0), temp = 26,  condition='thunder'),
                Forcast( time = Time(hrs = 21, min = 0), temp = 26,  condition='thunder'),
                Forcast( time = Time(hrs = 22, min = 0), temp = 26,  condition='clear'),
                Forcast( time = Time(hrs = 23, min = 0), temp = 26,  condition='clear')
            ]
        )
        weather.save()
        return "Data added successfully!!"