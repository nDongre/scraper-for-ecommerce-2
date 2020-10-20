import requests
import json

import pandas as pd

google_search_codes = pd.read_csv('greendeck.csv')
codes = google_search_codes['Google Search Code']
urls = []

#These if conditions don't do much. I had to use these because free version of serpstack only grants 100 requests per month.
for i in range(0,129):

    if i<100:
        params = {
            'access_key': '3e6a22eb2109f94f07030dba0f1cc8e5',
            'query': codes[i]
        }

    else:
        params = {
            'access_key': '7a1d5651cd1cc0e3244270ee43f9f237',
            'query': codes[i]
        }

    

    api_result = requests.get('http://api.serpstack.com/search', params)

    api_response = api_result.json()

    print("Total results: ", api_response['search_information']['total_results'], " ", i)

#appending the scraped urls in an array.
    for number, result in enumerate(api_response['organic_results'], start=1):
        if number == 1:
            urls.append(result['url'])
            print(urls)
            break


#print(urls)

