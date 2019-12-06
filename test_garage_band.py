import pytest

from garage_band import Band, Musician, Guitarist, Bassist, Drummer


def test_making_da_band():
    assert "It's time to make the band" == Band.making_da_band()


def test_jimmy_is_instance_of_correct_class(jimmy):
    assert isinstance(jimmy, Guitarist)


def test_jimmy_is_instance_of_parent_class(jimmy):
    assert isinstance(jimmy, Musician)


def test_jimmy_name(jimmy):
    assert jimmy.name == 'Jimmy'


def test_jimmy_instrument(jimmy):
    assert jimmy.instrument == 'guitar'


def test_to_list():
    Jimmy = Guitarist('Jimmy', 'guitar')
    Michael = Bassist('Michael', 'bass')
    Lisa = Drummer('Lisa', 'drums')
    expected = [Jimmy, Michael, Lisa]
    actual = Band.to_list()
    assert actual == expected

def test_create_band_from_data(jimmy):
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

    assert Band.members[0] == jimmy


@pytest.fixture()
def jimmy():
    return Guitarist('Jimmy', 'guitar')


# @pytest.fixture()
# def da_band():
#     return Guitarist('Jimmy', 'guitar'), Bassist('Michael', 'bass'), Drummer('Lisa', 'drums')

@pytest.fixture(autouse=True)
def clean():
    Band.members = []
