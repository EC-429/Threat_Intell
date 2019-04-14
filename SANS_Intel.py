# Imports
import argparse
import json
import requests
import datetime


def summary():
    today = datetime.date.today()                       # date variable
    # request data, decode json, save to variable
    data = requests.get(f'https://isc.sans.edu/api/dailysummary/{today}/{today}?json').json()

    date = data[0]["date"]                              # Variables: key/value pairs from json data
    records = data[0]["records"]
    targets = data[0]["targets"]
    sources = data[0]["sources"]

    print(f'Date:{date}')
    print(f'Records:{records}')
    print(f'Targets:{targets}')
    print(f'Sources:{sources}')


def targetports():
    today = datetime.date.today()                       # date variable
    # request data, decode json, save to variable
    data = requests.get(f'https://isc.sans.edu/api/topports/records/10/{today}?json').json()

    limit = int(data.get('limit'))                      # search dict. for numbers of arrays key

    for i in range(limit):                              # loop through arrays
        targetport = data[str(i)]['targetport']         # assign port variable while looping
        records = data[str(i)]['records']               # assign record variable while looping

        print(f'{targetport}:{records}')


def topips():
    today = datetime.date.today()                       # date variable
    # request data, decode json, save to variable
    data = requests.get(f'https://isc.sans.edu/api/topips/records/10/{today}?json').json()

    cnt = len(data)                                     # determine length of dictionary
    limit = cnt-1                                       # assign limit variable

    for i in range(limit):                              # loop through dictionary objects
        source = data[i]['source']                      # assign source IP variable while looping
        reports = data[i]['reports']                    # assign reports variable while looping

        print(f'{source}:{reports}')

def portdata():
    today = datetime.date.today()
    lweek = datetime.date.today() + datetime.timedelta(-7)
    lmonth = datetime.date.today() + datetime.timedelta(-30)

    td22 = requests.get(f'https://isc.sans.edu/api/portdate/22/{today}?json').json()
    td25 = requests.get(f'https://isc.sans.edu/api/portdate/25/{today}?json').json()
    td80 = requests.get(f'https://isc.sans.edu/api/portdate/80/{today}?json').json()
    td445 = requests.get(f'https://isc.sans.edu/api/portdate/445/{today}?json').json()
    td2323 = requests.get(f'https://isc.sans.edu/api/portdate/2323/{today}?json').json()
    lw22 = requests.get(f'https://isc.sans.edu/api/portdate/22/{lweek}?json').json()
    lw25 = requests.get(f'https://isc.sans.edu/api/portdate/25/{lweek}?json').json()
    lw80 = requests.get(f'https://isc.sans.edu/api/portdate/80/{lweek}?json').json()
    lw445 = requests.get(f'https://isc.sans.edu/api/portdate/445/{lweek}?json').json()
    lw2323 = requests.get(f'https://isc.sans.edu/api/portdate/2323/{lweek}?json').json()
    lm22 = requests.get(f'https://isc.sans.edu/api/portdate/22/{lmonth}?json').json()
    lm25 = requests.get(f'https://isc.sans.edu/api/portdate/25/{lmonth}?json').json()
    lm80 = requests.get(f'https://isc.sans.edu/api/portdate/80/{lmonth}?json').json()
    lm445 = requests.get(f'https://isc.sans.edu/api/portdate/445/{lmonth}?json').json()
    lm2323 = requests.get(f'https://isc.sans.edu/api/portdate/2323/{lmonth}?json').json()

    print(f'{td22["number"]}:{td22["data"]["records"]}')
    print(f'{td25["number"]}:{td25["data"]["records"]}')
    print(f'{td80["number"]}:{td80["data"]["records"]}')
    print(f'{td445["number"]}:{td445["data"]["records"]}')
    print(f'{td2323["number"]}:{td2323["data"]["records"]}')
    print(f'{lw22["number"]}:{lw22["data"]["records"]}')
    print(f'{lw25["number"]}:{lw25["data"]["records"]}')
    print(f'{lw80["number"]}:{lw80["data"]["records"]}')
    print(f'{lw445["number"]}:{lw445["data"]["records"]}')
    print(f'{lw2323["number"]}:{lw2323["data"]["records"]}')
    print(f'{lm22["number"]}:{lm22["data"]["records"]}')
    print(f'{lm25["number"]}:{lm25["data"]["records"]}')
    print(f'{lm80["number"]}:{lm80["data"]["records"]}')
    print(f'{lm445["number"]}:{lm445["data"]["records"]}')
    print(f'{lm2323["number"]}:{lm2323["data"]["records"]}')


def suspicious():
    # request data, decode json, save to variable
    data = requests.get('https://isc.sans.edu/feeds/suspiciousdomains_High.txt')
    line = data.text.split("\n")                            # split text by new lines
    sus_ips = []                                            # create empty list

    for i in line:                                          # for each line
        if ("#" in i) or "Site" in i:                       # parse
            pass
        else:
            sus_ips.append(i)                               # add ip to list

    for ip in sus_ips:                                      # parse and print list
        if ip != "":
            print(f'{ip}')


if __name__ == '__main__':
    # 3.1. Argparse help menu: display help menu
    parser = argparse.ArgumentParser(description='Parse and display SANS ISC DShield data by selecting a report below:')
    # 3.2. define flags
    parser.add_argument("--report",
                        choices=['Summary', 'TargetPorts', 'TopIPs', 'PortData', 'Suspicious'],
                        type=str)
    args = parser.parse_args()                  # 3.3. save input
    arg = str(args.report).lower()              # 3.4. assign input to var.

    if arg == 'summary':                        # function decision tree, based on input
        summary()
    elif arg == 'targetports':
        targetports()
    elif arg == 'topips':
        topips()
    elif arg == 'portdata':
        portdata()
    elif arg == 'suspicious':
        suspicious()
    else:
        print('Ooops! Must be smarter than the options menu. Try the -h flag.')

