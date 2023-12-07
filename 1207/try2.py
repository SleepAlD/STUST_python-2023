class sports :
    def __init__(self, name) :
        self.name = name

    @property
    def sport_name(self):
        return self.name

    @sport_name.setter
    def sport_name(self, value) :
        self.name = value

class on_land(sports) :
    def __init__(self,name,field):
        super().__init__(name)
        self.field = field

    @property
    def on_load_field(self) :
        return self.field

class in_water(sports) :
    def __init__(self,name,activity):
        super().__init__(name)
        self.activity = activity

    @property
    def in_water_field(self) :
        return self.activity

if __name__ == "__main__" :
    baseball = on_land("baseball","baseball field")
    print(baseball.sport_name)
    print(baseball.on_load_field)

    #print('\n')

    water_biking = in_water("water bike","sea")
    print(water_biking.sport_name)
    print(water_biking.in_water_field)