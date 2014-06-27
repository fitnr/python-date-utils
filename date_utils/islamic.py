from utils import ceil, floor

EPOCH = 1948439.5
WEEKDAYS = ("al-'ahad", "al-'ithnayn",
            "ath-thalatha'", "al-'arb`a'",
            "al-khamis", "al-jum`a", "as-sabt")


def leap(year):
    '''LEAP_ISLAMIC  --  Is a given year a leap year in the Islamic calendar ?'''
    return (((year * 11) + 14) % 30) < 11


def to_jd(year, month, day):
    '''TO_JD  --  Determine Julian day from Islamic date'''
    return ((day + ceil(29.5 * (month - 1)) + (year - 1) * 354 + floor((3 + (11 * year)) / 30) + EPOCH) - 1)


def from_jd(jd):
    '''Calculate Islamic date from Julian day'''

    jd = floor(jd) + 0.5
    year = floor(((30 * (jd - EPOCH)) + 10646) / 10631)
    month = min(12, ceil((jd - (29 + to_jd(year, 1, 1))) / 29.5) + 1)
    day = int(jd - to_jd(year, month, 1)) + 1
    return (year, month, day)
