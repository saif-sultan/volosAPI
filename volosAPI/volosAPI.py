from __future__ import absolute_import
from __future__ import division
from __future__ import print_function



# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""

*********************
Volos Options Data API
*********************
Documentation at: https://volosdataapi.docs.apiary.io/#

"""

__author__ = 'Saif Sultan'
__copyright__ = '2019 Volos Portfolio Solutions, LLC.. All rights reserved'
__version__ = '1.0'
__interpreter__ = 'Anaconda - Python 2.7.10 64 bit'
__maintainer__ = 'Saif Sultan'
__email__ = 'saif.sultan@volossoftware.com'
__status__ = 'In Progress'

import json
import requests
import pandas as pd
import io


class volosAPI(object):

    API_KEY  = None
    API_STAGE = 'prod'
    API_ENDPOINT = 'https://api-data.volossoftware.com/'

    def __init__(self, api_key):
        self.API_KEY = api_key

    def set_api_key(self, api_key):
        self.API_KEY = api_key

    def switch_stage_prod(self):
        self.API_STAGE = 'prod'

    def switch_stage_ci(self):
        self.API_STAGE = 'ci'

    def switch_stage_ir(self):
        self.API_STAGE = 'ir'

    def get_headers(self):
        if self.API_KEY is None:
            raise Exception("Please set API Key")
        return {'x-api-key': self.API_KEY}

    def get_url(self, uri):
        return self.API_ENDPOINT + self.API_STAGE + uri

    def get_strategy_total_returns(self, strategy_id, output_format='csv', start_date='1990-01-01', end_date='2050-01-01'):
        uri = '/time-series/totalreturns'
        payload = {'strategy_id': strategy_id, 'output_format': output_format, 'start_date':start_date, 'end_date':end_date}

        res = requests.get(self.get_url(uri), params=payload, headers=self.get_headers())
        if output_format=='json':
            return json.loads(res.content)
        elif output_format=='csv':
            return pd.read_csv(io.StringIO(res.content.decode('utf-8')))
        else:
            raise NotImplementedError("Incorrect output format")


    def get_strategy_list_total_returns(self, strategy_id_list, start_date='1990-01-01', end_date='2050-01-01'):
        uri = '/time-series/total-returns-multi'
        payload = {'strategy_id_list': strategy_id_list, 'start_date': start_date, 'end_date': end_date}
        res = requests.post(self.get_url(uri), data=json.dumps(payload), headers=self.get_headers())
        return pd.read_csv(io.StringIO(res.content.decode('utf-8')))


    def get_strategy_metrics(self, strategy_id, start_date='1990-01-01', end_date='2050-01-01'):
        uri = '/time-series/metrics'
        payload = {'strategy_id': strategy_id, 'start_date': start_date, 'end_date': end_date}
        res = requests.post(self.get_url(uri), data=json.dumps(payload), headers=self.get_headers())
        return pd.read_csv(io.StringIO(res.content.decode('utf-8')))


    def get_strategy_trade_logs(self, strategy_id, start_date='1990-01-01', end_date='2050-01-01'):
        uri = '/strategy/tradelogs'
        payload = {'strategy_id': strategy_id, 'start_date': start_date, 'end_date': end_date}
        res = requests.post(self.get_url(uri), data=json.dumps(payload), headers=self.get_headers())
        return pd.read_csv(io.StringIO(res.content.decode('utf-8')))


    def get_strategy_list_meta_data(self, strategy_id_list):
        uri = '/strategy/meta-data'
        payload = {'strategy_id_list': strategy_id_list}
        res = requests.post(self.get_url(uri), data=json.dumps(payload), headers=self.get_headers())
        return json.loads(res.content.decode('utf-8'))

    def get_strategy_list_tags(self, strategy_id_list):
        uri = '/strategy/tags'
        payload = {'strategy_id_list': strategy_id_list}
        res = requests.post(self.get_url(uri), data=json.dumps(payload), headers=self.get_headers())
        return json.loads(res.content.decode('utf-8'))

    def get_strategy_excel_sheet(self, strategy_id):
        uri = '/strategy/excel-sheet'

        payload = {'strategy_id': strategy_id}
        res = requests.get(self.get_url(uri), params=payload, headers=self.get_headers())
        return res.url
        # return pd.read_excel(io.StringIO(res.content))


    def search_by_ticker(self, ticker):
        uri = '/search/ticker'
        payload = {'ticker': ticker}
        res = requests.post(self.get_url(uri), data=json.dumps(payload), headers=self.get_headers())
        return pd.read_csv(io.StringIO(res.content.decode('utf-8')))


    def search_by_tags(self, tag_value_pairs):
        uri = '/search/tags'
        payload = {'tag_value_pairs': tag_value_pairs, 'match_all':1}
        res = requests.post(self.get_url(uri), data=json.dumps(payload), headers=self.get_headers())
        return pd.read_csv(io.StringIO(res.content.decode('utf-8')))


    def get_all_tags(self):
        uri = '/misc/all-tags'

        res = requests.get(self.get_url(uri), headers=self.get_headers())
        return json.loads(res.content)


    def get_tag_values(self, tag_name_list):
        uri = '/misc/tag-values'
        payload = {'tag_name_list': tag_name_list}
        res = requests.post(self.get_url(uri), data=json.dumps(payload), headers=self.get_headers())
        return pd.read_csv(io.StringIO(res.content.decode('utf-8')))