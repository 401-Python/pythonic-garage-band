

class Band():
    members = []

    def __init__(self, name, band):
        self.band = band
        self.name = name
        self.__class__.members.append(self)

    @staticmethod
    def making_da_band():
        return "It's time to make the band"

    def __repr__(self):
        return f'{self.name}'

    @classmethod
    def play_solos(cls):
        for member in cls.members:
            print(f'Super {member.instrument} solo from {member}')

    @classmethod
    def create_from_data(cls, data):
        for musician in data:
          if musician['instrument'] == 'Guitar':
              cls.members.append(
                  Guitarist(musician['name'], musician['instrument']))
              continue

          elif musician['instrument'] == 'Bass':
              cls.members.append(Bassist(musician['name'], musician['instrument']))
              continue

          elif musician['instrument'] == 'Drums':
              cls.members.append(Drummer(musician['name'], musician['instrument']))
              continue

    @classmethod
    def to_list(cls):
        print(cls.members)
        return cls.members


class Musician(Band):
    musician_list = []

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_members(cls):
        return cls.musician_list


class Guitarist(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return '*loud guitar noises*'

    def get_instrument(self):
        return 'guitar'


class Bassist(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return 'basssssssssss'

    def get_instrument(self):
        return 'Bass'


class Drummer(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument
        super().__init__(name)

    def play_solo(self):
        return 'badum badum ch badum ch'

    def get_instrument(self):
        return 'Drums'


data = [
    {'name': 'Jimmy',
     'instrument': 'Guitar'
     },

    {'name': 'Michael',
        'instrument': 'Bass'
     },
    {'name': 'Lisa',
        'instrument': 'Drums'
     }
]


Band.create_from_data(data)
# Band.play_solos()
Band.to_list()
