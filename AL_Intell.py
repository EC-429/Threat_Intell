# import packages
import argparse
import operator
import re


# WHITELIST: Add IP Addresses to the list below to be ignored if found in the access.log
whitelist = ["127.0.0.1", "192.168.1.1"]
reg_ip = "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"                      # IP address regex


def ip_top_offenders(n):
    ips_dict = {}                                                   # Dictionary

    with open('logs/access_collector.log') as log:                  # open access.log
        for line in log:                                            # loop through each line
            ips = re.search(reg_ip, line)                           # search line for regex
            if ips: ip = ips.group(0)                               # if successful, assign result to var.
            else: pass                                              # else, pass

            if ip in whitelist:                                     # Check if IP is in whitelist
                pass                                                # if so, pass
            else:
                if ip in ips_dict:                                  # check if IP is already in dict
                    ips_dict[ip] = ips_dict.get(ip) + 1             # if it is, increment value
                else:
                    ips_dict[ip] = 1                                # if not, create key and initial value

    # sort dictionary
    sorted_ips_dict = sorted(ips_dict.items(), key=operator.itemgetter(1), reverse=True)
    # create top accessing IPs tuple list using user input
    top_ip_offenders = sorted_ips_dict[0:n]

    # print results
    for items in top_ip_offenders:
        data = str(items[0]) + ":" + str(items[1])
        print(data)


def request_types(n):
    type_dict = {}                                                  # dictionary
    reg_types = "GET|POST|HEAD|OPTIONS|PUT|DELETE|CONNECT|TRACE"    # request type regex

    with open('logs/access_collector.log') as log:                  # open access.log
        for line in log:                                            # loop through each line
            ips = re.search(reg_ip, line)                           # search line for regex
            if ips: ip = ips.group(0)                               # if successful, assign result to var.
            else: pass                                              # else, pass

            types = re.search(reg_types, line)                      # search line for regex
            if types: req_type = types.group(0)                     # if successful, assign result to var.
            else: pass                                              # else pass

            if ip in whitelist:                                         # Check if IP is in whitelist
                pass                                                    # if so, pass
            else:
                if req_type in type_dict:                               # check if type in dictionary
                    type_dict[req_type] = type_dict.get(req_type) + 1   # if it is, increment by 1
                else:
                    type_dict[req_type] = 1                             # if not, create new key/value

    # sort dictionary
    sorted_type_dict = sorted(type_dict.items(), key=operator.itemgetter(1), reverse=True)
    # create top requested type tuple list using user input
    top_req_type = sorted_type_dict[0:n]

    # print results
    for items in top_req_type:
        data = str(items[0]) + ":" + str(items[1])
        print(data)


def req_directory(n):
    req_dict = {}                                                           # dictionary
    reg_req = '\s{1}(/|/[a-zA-Z0-9\/\.\_\?\=\%\:\-\&\[\]\!\+\\\]+)\s{1}'    # request directory regex

    with open('logs/access_collector.log') as log:                          # open access.log
        for line in log:                                                    # loop through each line
            ips = re.search(reg_ip, line)                                   # search line for regex
            if ips: ip = ips.group(0)                                       # if successful, assign result to var.
            else: pass                                                      # else, pass

            reqs = re.search(reg_req, line)                                 # search line for regex
            if reqs: req_url = reqs.group(0).strip()                        # if successful, assign result to var.
            else: pass

            if ip in whitelist:                                             # Check if IP is in whitelist
                pass                                                        # if so, pass
            else:
                if req_url in req_dict:                                     # check if directory in dictionary
                    req_dict[req_url] = req_dict.get(req_url) + 1           # if it is, increment by one
                else:
                    req_dict[req_url] = 1                                   # if not, create new key/value

    # sort dictionary
    sorted_req_dict = sorted(req_dict.items(), key=operator.itemgetter(1), reverse=True)
    # create top requested directory tuple list using user input
    top_dir_req = sorted_req_dict[0:n]

    # print results
    for items in top_dir_req:
        data = str(items[0]) + ":" + str(items[1])
        print(data)


def req_response(n):
    resp_dict = {}
    reg_codes = " 200 | 201 | 204 | 301 | 302 | 304 | 400 | 401 | 403 | 404 | 409 | 500 "  # response code regex

    with open('logs/access_collector.log') as log:
        for line in log:
            ips = re.search(reg_ip, line)                           # search line for regex
            if ips: ip = ips.group(0)                               # if successful, assign result to var.
            else: pass                                              # else, pass

            codes = re.search(reg_codes, line)                      # search line for regex
            if codes: resp_code = codes.group(0).strip()            # if successful, assign result to var.
            else: pass                                              # else pass

            if ip in whitelist:                                             # Check if IP is in whitelist
                pass                                                        # if so, pass
            else:
                if resp_code in resp_dict:
                    resp_dict[resp_code] = resp_dict.get(resp_code) + 1     # check if response is in dictionary
                else:                                                       # if it is, increment by one
                    resp_dict[resp_code] = 1                                # if not, create new hey/value

    # sorted dictionary
    sorted_resp_dict = sorted(resp_dict.items(), key=operator.itemgetter(1), reverse=True)
    # create top request response tuple list using user input
    top_resp_req = sorted_resp_dict[0:n]

    for items in top_resp_req:
        data = str(items[0] + ":" + str(items[1]))
        print(data)


def req_traffic(n):

    dict_200 = {}                                               # Good traffic Dictionary
    dict_404 = {}                                               # Bad traffic Dictionary
    reg_200 = " 200 "                                           # Regex string to search for
    reg_404 = " 404 "                                           # "                         "
    reg_date = "\d{2}/\w{3}/\d{4}"                              # "                         "

    with open('logs/access_collector.log') as log:
        for line in log:                                        # loop through log file
            ips = re.search(reg_ip, line)                           # search line for regex
            if ips: ip = ips.group(0)                               # if successful, assign result to var.
            else: pass                                              # else, pass

            if ip in whitelist:                                             # Check if IP is in whitelist
                pass                                                        # if so, pass
            else:
                ok = re.search(reg_200, line)                       # search for regex
                pnf = re.search(reg_404, line)                      # "               "

                if ok:                                              # If 200 regex is found
                    dts = re.search(reg_date, line)                 # search for date regex
                    dtm = dts.group(0)

                    if dtm in dict_200:                             # If found date regex is in good traffic dictionary
                        dict_200[dtm] = dict_200[dtm] + 1           # increment value integer
                    else:
                        dict_200[dtm] = 1                           # else, add the key and assign initial value of 1

                if pnf:                                             # same as above
                    pnfs = re.search(reg_date, line)
                    pnfm = pnfs.group(0)

                    if pnfm in dict_404:
                        dict_404[pnfm] = dict_404[pnfm] + 1
                    else:
                        dict_404[pnfm] = 1

    for x in list(dict_200)[0:n]:
        print(f'200:{x}:{dict_200[x]}')

    for y in list(dict_404)[0:n]:
        print(f'404:{y}:{dict_404[y]}')


def main():
    # argpase
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--offenders", type=int, help="Display top n requesting IPs (Ex: -o 5)")
    parser.add_argument("-r", "--requests", type=int, help="Display top n request types (Ex: -r 3)")
    parser.add_argument("-d", "--directories", type=int, help="Display top n requested directories (Ex: -d 7)")
    parser.add_argument("-c", "--codes", type=int, help="Display top n response codes (Ex: -o 3)")
    parser.add_argument("-t", "--traffic", type=int, help="Display most current traffic (Ex: -t 6)")
    # arg placeholder

    args = parser.parse_args()                                      # parser args
    offenders = str(args.offenders)                                 # store arguments as variables
    requests = str(args.requests)
    directories = str(args.directories)
    codes = str(args.codes)
    traffic = str(args.traffic)

    if offenders != "None":                                         # check if arguments have been passed
        ip_top_offenders(int(offenders))                            # if so, run the corresponding function
    elif requests != "None":
        request_types(int(requests))
    elif directories != "None":
        req_directory(int(directories))
    elif codes != "None":
        req_response(int(codes))
    elif traffic != "None":
        req_traffic(int(traffic))
    else:
        "Opps! Try again. Must be smarter than the menu."


# Run main function
main()
