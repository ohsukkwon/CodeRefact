# -*- coding: utf-8 -*-

class TokenRecord:

    def __init__(self, argTiktokenQuery, argTiktokenResponse, argSystemQuery, argSystemQueryCached, argSystemResponse):
        self.mTiktokenQuery = argTiktokenQuery
        self.mTiktokenResponse = argTiktokenResponse
        self.mSystemQuery = argSystemQuery
        self.mSystemQueryCached = argSystemQueryCached
        self.mSystemResponse = argSystemResponse

    def add_record(self, argTokenRecord):
        if argTokenRecord:
            self.mTiktokenQuery += argTokenRecord.mTiktokenQuery
            self.mTiktokenResponse += argTokenRecord.mTiktokenResponse
            self.mSystemQuery += argTokenRecord.mSystemQuery
            self.mSystemQueryCached += argTokenRecord.mSystemQueryCached
            self.mSystemResponse += argTokenRecord.mSystemResponse

    def calc_money(self, money_query_per_1token, money_query_cached_per_1token, monkey_response_per_1token):
        moneyTiktoken = self.mTiktokenQuery * money_query_per_1token + \
                        self.mTiktokenResponse * monkey_response_per_1token
        moneySystemToken = self.mSystemQuery * money_query_per_1token + \
                           self.mSystemQueryCached * money_query_cached_per_1token + \
                           self.mSystemResponse * monkey_response_per_1token

        return '{:.8f}'.format(moneyTiktoken), '{:.8f}'.format(moneySystemToken)

    def get_tiktoken_count(self):
        return self.mTiktokenQuery, self.mTiktokenResponse

    def get_systemtoken_count(self):
        return self.mSystemQuery, self.mSystemQueryCached, self.mSystemResponse

    def get_total_token_count(self):
        return self.mSystemQuery+self.mSystemQueryCached+self.mSystemResponse

    def __str__(self):
        return f'[total:{self.mTiktokenQuery + self.mTiktokenResponse}] TikTokenQuery:{self.mTiktokenQuery}, TiktokenResponse:{self.mTiktokenResponse}\n' \
               f'[total:{self.mSystemQuery + self.mSystemQueryCached + self.mSystemResponse}] SystemQuery:{self.mSystemQuery}, SystemQueryCached:{self.mSystemQueryCached}, SystemResponse:{self.mSystemResponse}'
