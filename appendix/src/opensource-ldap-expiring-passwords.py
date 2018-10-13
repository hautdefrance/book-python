# !/usr/bin/env python3

import datetime
import time
from pprint import pprint
from ldap3 import Server, Connection, SEARCH_SCOPE_WHOLE_SUBTREE

USER = "myusername"
PASS = "mypassword"
BASEDN = "OU=Users,DC=local"
SERVER = Server("127.0.0.1", port=389)
ATTRIBUTES = ['mail', 'pwdLastSet']


def construct_filter(wintimestamp):
    return """(&
       (objectCategory=Person)
       (objectCategory=User)
       (userAccountControl=512)
       (pwdLastSet<={wintimestamp})
       (mail=*)
    )""".format(wintimestamp=wintimestamp)


def search(filter):
    with Connection(SERVER, user=USER, password=PASS) as c:
        c.search(BASEDN, filter, SEARCH_SCOPE_WHOLE_SUBTREE,
                 attributes=ATTRIBUTES)
        return [record['attributes'] for record in c.response]


def datetime_to_mstimestamp(date):
    """
    Active Direcotry has different approach to create timestamp than Unix.
    Here's a function to convert the Unix timestamp to the AD one.

    >>> datetime_to_mstimestamp(datetime.datetime(2000, 1, 1, 0, 0))
    125911548000000000
    """
    timestamp = int(time.mktime(date.timetuple()))
    magic_number = 116444736000000000
    return timestamp * 10000000 + magic_number


def mstimestamp_to_datetime(mstimestamp):
    """
    Active Direcotry has different approach to create timestamp than Unix.
    Here's a function to convert AD timestamp to the Unix one.

    >>> mstimestamp_to_datetime(130567328471235643)
    datetime.datetime(2014, 10, 2, 16, 14, 7, 123563)
    """
    magic_number = 11644473600
    return datetime.datetime.fromtimestamp(
        mstimestamp / 10000000 - magic_number)


def month_ago(date):
    """
    >>> month_ago(datetime.datetime(2000, 1, 31, 0, 0))
    datetime.datetime(2000, 1, 1, 0, 0)
    """
    return date - datetime.timedelta(days=30)


def print_users_with_expiring_password():
    now = datetime.datetime.now()
    expiration_date = month_ago(now)
    wintimestamp = datetime_to_mstimestamp(expiration_date)
    older_than_month_ago = construct_filter(wintimestamp)

    for user in search(older_than_month_ago):
        user['pwdLastSet'] = mstimestamp_to_datetime(
            int(user['pwdLastSet'][0]))
        pprint(user)


if __name__ == "__main__":
    print_users_with_expiring_password()
