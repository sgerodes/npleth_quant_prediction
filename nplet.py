class Nplet():
    rising_key = 1
    falling_key = 0

    def __init__(self, key):
        self.key = key
        self.forecast_count = {Nplet.rising_key: 0.0, Nplet.falling_key: 0.0}

    def inc_rising_count(self):
        self.forecast_count[Nplet.rising_key] += 1

    def inc_falling_count(self):
        self.forecast_count[Nplet.falling_key] += 1

    def get_rising_count(self):
        return self.forecast_count[Nplet.rising_key]

    def get_falling_count(self):
        return self.forecast_count[Nplet.falling_key]

    def get_rising_falling_ratio(self):
        if self.get_falling_count() == 0:
            if self.get_rising_count() != 0:
                return 9223372036854775807
            else:
                return 1
        return self.get_rising_count() / self.get_falling_count()

    def get_total_count(self):
        return self.get_rising_count() + self.get_falling_count()

    def get_rising_probability(self):
        return self.get_rising_count() / self.get_total_count()

    def get_falling_probability(self):
        return self.get_falling_count() / self.get_total_count()

    def get_key(self):
        return self.key

    def __repr__(self):
        return 'Nplet(key={}; forecast_count={})'.format(self.get_key(), self.forecast_count)
