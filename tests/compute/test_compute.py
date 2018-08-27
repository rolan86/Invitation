import json
import pytest

from invitation.compute import new_compute as nc


tdata = [
    json.dumps(
        {
            "latitude": "52.986375", "user_id": 12,
            "name": "Christina McArdle", "longitude": "-6.043701"
        }
    )
]

edata = [
    {
        'latitude': 52.986375, 'user_id': 12,
        'name': u'Christina McArdle', 'longitude': -6.043701
    }
]

tinvite = [
    {
        'latitude': 52.986375,
        'user_id': 12,
        'name': u'Christina McArdle',
        'longitude': -6.043701
    },
    {
        'latitude': 51.92893,
        'user_id': 1,
        'name': u'Alice Cahill',
        'longitude': -10.27699
    },
    {
        'latitude': 52.3191841,
        'user_id': 3,
        'name': u'Jack Enright',
        'longitude': -8.5072391
    }
]

einvite = [(12, u'Christina McArdle', 41.77)]


@pytest.mark.parametrize(
    'tdata, edata', [
        (tdata, edata)
    ]
)
def test_format_data(tdata, edata):
    """Test to check function for formatting of data"""
    obj = nc.Invite()
    assert obj.format_data(tdata) == edata


@pytest.mark.parametrize(
    'testdata, expected', [
        ([52.98637, -6.043701], 41.77)
    ]
)
def test_distance_calculation(testdata, expected):
    """Test to check function for radial distance calculation"""
    obj = nc.Invite()
    lat, lon = testdata
    assert obj.dist_calculation(lat, lon) == expected


@pytest.mark.parametrize(
    'testdata, expected', [
        (90, True),
        (101, False)
    ]
)
def test_radius_check(testdata, expected):
    """Test to check function for border test of radius"""
    obj = nc.Invite()
    assert obj.radius_check(testdata) == expected


@pytest.mark.parametrize(
    'tinvite, einvite', [
        (tinvite, einvite)
    ]
)
def test_get_invitees(tinvite, einvite):
    """Test to check the function for the invite list"""
    obj = nc.Invite()
    assert obj.get_invitees(tinvite) == einvite
