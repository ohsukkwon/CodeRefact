# -*- coding: utf-8 -*-
from utils.GlobalVars import g_str_token_split

class ScoredItem:
    def __init__(self, rawString):
        self.__setInitValue__()

        trimedStr = rawString.strip()
        if len(trimedStr) < 1:
            print(r'# Error len(trimedStr) is 0.')
        else:
            self.mRawStr = trimedStr
            arr_split_trimed_str = [_str.strip() for _str in trimedStr.split(g_str_token_split)]

            if len(arr_split_trimed_str) < 1:
                print(r'# Error len(arr_split_trimed_str) is 0.')
            else:
                for i in range(0,len(arr_split_trimed_str)):
                    if i == 0:
                        self.mScore = arr_split_trimed_str[0]
                    elif i == 1:
                        self.mReason = arr_split_trimed_str[1]
                    elif i == 2:
                        self.mOrgInput = arr_split_trimed_str[2]
                    elif i == 3:
                        self.mOrgOutput = arr_split_trimed_str[3]
                    elif i == 4:
                        self.mRecomand = arr_split_trimed_str[4]
                    else:
                        self.__setInitValue__()

    def __setInitValue__(self):
        self.mRawStr = ''
        self.mScore = -1
        self.mReason = ''
        self.mOrgInput = ''
        self.mOrgOutput = ''
        self.mRecommand = ''

    def getRawStr(self):
        return self.mRawStr
