# import packages
import argparse
import operator


def ip_top_offenders(n):
    ips_dict = {}                                                   # Dictionary

    with open('logs/access_collector.log') as log:                  # open access.log
        for line in log:                                            # loop through each line
            ip = line.split(" ")[0]                                 # split and assign IP

            if ip in ips_dict:                                      # check if IP is already in dict
                ips_dict[ip] = ips_dict.get(ip) + 1                 # if it is, increment value
            else:
                ips_dict[ip] = 1                                    # if not, create key and initial value

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

    with open('logs/access_collector.log') as log:                  # open access.log
        for line in log:                                            # loop through each line
            req = line.split('"')[1]                                # split line for request
            req_type = req.split(" ")[0]                            # split request for type

            #if "200" not in line:                                  # check if request caused an error
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
    dir_dict = {}                                                   # dictionary

    with open('logs/access_collector.log') as log:                  # open access.log
        for line in log:                                            # loop through each line
            req = line.split(' ')[6]                                # split line for directory requested

            if req in dir_dict:                                     # check if directory in dictionary
                dir_dict[req] = dir_dict.get(req) + 1               # if it is, increment by one
            else:
                dir_dict[req] = 1                                   # if not, create new key/value

    # sort dictionary
    sorted_req_dict = sorted(dir_dict.items(), key=operator.itemgetter(1), reverse=True)
    # create top requested directory tuple list using user input
    top_dir_req = sorted_req_dict[0:n]

    # print results
    for items in top_dir_req:
        data = str(items[0]) + ":" + str(items[1])
        print(data)


def req_response(n):
    resp_dict = {}

    with open('logs/access_collector.log') as log:
        for line in log:
            resp = line.split('"')[2].strip()
            resp_type = resp.split(' ')[0]

            if resp_type in resp_dict:
                resp_dict[resp_type] = resp_dict.get(resp_type) + 1
            else:
                resp_dict[resp_type] = 1

    # sorted dictionary
    sorted_resp_dict = sorted(resp_dict.items(), key=operator.itemgetter(1), reverse=True)
    # create top request response tuple list using user input
    top_resp_req = sorted_resp_dict[0:n]

    for items in top_resp_req:
        data = str(items[0] + ":" + str(items[1]))
        print(data)


def main():
    # argpase
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--offenders", type=int, help="Display top n requesting IPs")
    parser.add_argument("-r", "--requests", type=int, help="Display top n request types")
    parser.add_argument("-d", "--directories", type=int, help="Display top n requested directories")
    parser.add_argument("-c", "--codes", type=int, help="Display top n response codes")
    # arg placeholder

    args = parser.parse_args()                                      # parser args
    offenders = str(args.offenders)                                 # store arguments as variables
    requests = str(args.requests)
    directories = str(args.directories)
    codes = str(args.codes)

    if offenders != "None":                                         # check if arguments have been passed
        ip_top_offenders(int(offenders))                            # if so, run the corresponding function
    elif requests != "None":
        request_types(int(requests))
    elif directories != "None":
        req_directory(int(directories))
    elif codes != "None":
        req_response(int(codes))
    else:
        "Opps! Try again. Must be smarter than the menu."


# Run main function
main()
