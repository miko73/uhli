import time
import os


def show_zone_info():
    print(f'''\
    TZ    : {os.environ.get('TZ', '(not set)')}
    tzname: {time.tzname}
    Zone  : {time.timezone} ({time.timezone / 3600})
    DST   : {time.daylight}
    Time  : {time.ctime()}
    ''')


if __name__ == '__main__':
    print('Default: ')
    show_zone_info()

    ZONES = [
        'GMT',
        'Europe/Amsterdam'
    ]

    for zone in ZONES:
        os.environ['TZ'] = zone
        # time.tzset()      # Only available on Unix
        print(zone, ':')
        show_zone_info()