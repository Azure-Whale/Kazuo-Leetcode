#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    : Post Request.py
@Time    : 11/20/2020 12:27 PM
@Author  : Kazuo
@Email   : azurewhale1127@gmail.com
@Software: PyCharm
'''

"""
Call hatebase API to get access to the english hateful words
"""

import requests
import json
import pandas as pd

AUTH = {'api_key': 'KeFymhAyxRdCkTopYGcDUnCNFYcbAwnZ'}

def get_token(AUTH):
    """
    Get token using given API key from the hatebase
    """
    # Get token
    url_get_auth = "https://api.hatebase.org/4-4/authenticate"


    # get toekn from the server
    a = requests.post(url=url_get_auth, data=AUTH)
    auth = a.json()
    token = auth['result']['token']

    return token


def get_vocab(token):
    """
    Get raw vocab json from the hatebase using given secret key
    """
    # extracting data in json format
    url_get_vocab = "https://api.hatebase.org/4-4/get_vocabulary"
    query = {'token': token,'page':1,'language':'eng','format':'json'}
    overview = requests.post(url=url_get_vocab, data=query)
    overview_info = overview.json()
    # get the number of expected words
    number_of_results = overview_info['number_of_results']
    # get total pages that we need to query, each query for each page
    num_pages = overview_info['number_of_pages']
    # store all res
    res = []
    # iterate each query and collect words for each query
    print('Total page ',num_pages)
    for page in range(1,num_pages+1):
        print('Loading page ', page)
        # set the query
        query = {'token': token, 'page': page, 'language': 'eng', 'format': 'json'}
        # use the query to get the data for a single page
        data = requests.post(url=url_get_vocab, data=query)
        data = data.json()
        # get the result attribute of the data
        page_result = data['result']
        for word in page_result:
            id = word['vocabulary_id']
            term = word['term']
            hateful_meaning = word['hateful_meaning']
            nonhateful_meaning = word['nonhateful_meaning']
            average_offensiveness = word['average_offensiveness']
            entry = {
                "id":id,
                "term":term,
                "hateful_meaning":hateful_meaning,
                "nonhateful_meaning":nonhateful_meaning,
                "average_offensiveness":average_offensiveness
            }
            res.append(entry)
        print('Get words for ',len(data['result']),' at page ',page)
        # open the output file to storage the words from the hatebase
    print(f'Get totally {len(res)} words')
    print(len(res)==number_of_results)
    return res

def store_word_list(words):
    if words:
        with open('../requests/words_from_hatebase.txt', 'w') as f:
            json.dump(words, f)


token = get_token(AUTH)
words = get_vocab(token)
store_word_list(words)