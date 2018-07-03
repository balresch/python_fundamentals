"""Model for aircraft flights"""



class Flight:

    def __init__(self, flight_nr):
        self._flight_nr = flight_nr

    def flight_number(self):
        return self._flight_nr


class Aircraft:
    pass


