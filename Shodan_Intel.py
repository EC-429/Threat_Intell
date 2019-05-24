# Imports
import argparse
import requests
import shodan

API_KEY = "INSERT API KEY HERE"


def pop_tags(n):
    url = f'https://api.shodan.io/shodan/query/tags?key={API_KEY}&size={n}'
    data = requests.get(url).json()

    for obj in data['matches']:
        count, value = (obj['count'], obj['value'])
        print(f'{value}:{count}')


def pop_queries():
    url = f'https://api.shodan.io/shodan/query?key={API_KEY}&sort=votes&order=desc'
    data = requests.get(url).json()

    for obj in data['matches']:
        votes, title = (obj['votes'], obj['title'])
        # query, desc = (obj['query'], obj['description'])
        print(f'{title}:{votes}')


def ports_crawled():
    url = f'https://api.shodan.io/shodan/ports?key={API_KEY}&'
    data = requests.get(url).json()

    for index,obj in enumerate(data):
        print(f'{index}:{obj}')


def facet_query(x):
    api = shodan.Shodan(API_KEY)                            # setup the API
    # The list of facets we want summary information for
    FACETS = [
        ('org',     3),
        ('domain',  3),
        ('country', 3),
        ('port',    3)
    ]
    result = api.count(f'{x}', facets=FACETS)   # api query

    for obj in result['facets']:                            # loop through returned json facets
        facet = obj                                         # define returned facet objects as variables
        #print(f'\nFACET: {facet}')
        for items in result['facets'][facet]:                   # loop through each facet obj
            facet, value, count = (facet.upper(),
                                   items['value'],
                                   items['count'])

            print(f'{facet}:{value}:{count}')


if __name__ == '__main__':
    # argpase
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--tags", type=int, help="Display top n popular Shodan tags (Ex: -t 5)")
    parser.add_argument("-f", "--facets", type=str, help="Display Shodan facet info. (Ex: -f category:malware)")
    parser.add_argument("--reports",
                        choices=['PopularQueries', 'CrawledPorts'],
                        type=str, help="Display Shodan report information (EX: --reports PopularQueries)")
    # arg placeholder

    args = parser.parse_args()                                      # parser args
    tags = str(args.tags)                                           # store arguments as variables
    facets = str(args.facets)
    arg_report = str(args.reports)

    if tags != "None":                                         # check if arguments have been passed
        pop_tags(int(tags))                            # if so, run the corresponding function
    elif facets != "None":
        facet_query(str(facets))
    elif arg_report == "PopularQueries":
        pop_queries()
    elif arg_report == "CrawledPorts":
        ports_crawled()
    else:
        "Opps! Try again. Must be smarter than the menu."
