# -*- coding: utf-8 -*-
import re

from GlobalVars import *

class QueryOneTableEvalImg:
    def _set_title(self):
        self.mHeader = '''| no | prompt | style | outimg | inimg | score | reason | caption |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
'''

    def __init__(self, argGlobalArgs):
        self.mArgs = argGlobalArgs
        self._set_title()
        self.mResultRecords = []

    def add_fake_record(self, arg_idx = 0):
        self.add_record('{:04d}'.format(arg_idx), 'FAKE', 'FAKE', 'FAKE', 'FAKE', 'FAKE', 'FAKE', 'FAKE')

    def add_record(self, argNo, argPrompt, argStyle, argOutImg, argInImg, argScore, argReason, argCaption):
        argScore = argScore.strip().split('/')[0]
        argScore = re.sub(r'[^0-9]', '', argScore)

        self.mResultRecords.append(QueryItemEvalImg(argNo, argPrompt, argStyle, argOutImg, argInImg, argScore, argReason, argCaption))

        return len(self.mResultRecords)

    def set_record(self, argIdx, argNo, argPrompt, argStyle, argOutImg, argInImg, argScore, argReason, argCaption):
        recordItem = self.mResultRecords[argIdx]
        recordItem.setNo(argNo)
        recordItem.setScore(argPrompt)
        recordItem.setStyle(argStyle)
        recordItem.setOutImg(argOutImg)
        recordItem.setInImg(argInImg)
        recordItem.setScore(argScore)
        recordItem.setReason(argReason)
        recordItem.setCaption(argCaption)

    def get_record_count(self):
        return len(self.mResultRecords)

    def __str__(self):
        retStr = f"■ QueryOneTable : \n"

        for _idx, item in enumerate(self.mResultRecords):
            retStr = f'{retStr}{item.getString()}'
            if _idx < len(self.mResultRecords)-1:
                retStr = f'{retStr}\n'

        return retStr


class QueryItemEvalImg:
    def __init__(self, argNo, argPrompt, argStyle, argOutImg, argInImg, argScore, argReason, argCaption):
        self.mNo = argNo.strip()
        self.mPrompt = argPrompt.strip()
        self.mStyle = argStyle.strip()

        self.mOutImg = argOutImg.strip()
        self.mInImg = argInImg.strip()

        self.mScore = argScore.strip()
        self.mReason = argReason.strip()
        self.mCaption = argCaption.strip()

    def setNo(self, argNo):
        self.mNo = argNo.strip()

    def getNo(self):
        return self.mNo

    def setPrompt(self, argPrompt):
        self.mPrompt = argPrompt.strip()

    def getPrompt(self):
        return self.mPrompt

    def setStyle(self, argStyle):
        self.mStyle = argStyle.strip()

    def setOutImg(self, argOutImg):
        self.mOutImg = argOutImg.strip()

    def getOutImg(self):
        return self.mOutImg

    def setInImg(self, argInImg):
        self.mInImg = argInImg.strip()

    def getInImg(self):
        return self.mInImg

    def setScore(self, argScore):
        self.mScore = argScore.strip()

    def getScore(self):
        return self.mScore

    def setReason(self, argReason):
        self.mReason = argReason.strip()

    def getReason(self):
        return self.mReason

    def setCaption(self, argCaption):
        self.mCaption = argCaption.strip()

    def getCaption(self):
        return self.mCaption

    def to_dict(self):

        result_dict = {
            'no': self.mNo,
            'prompt': self.mPrompt,
            'style': self.mStyle,
            'outImg': self.mOutImg,
            'inImg': self.mInImg,
            'score': self.mScore,
            'reason': self.mReason,
            'caption': self.mCaption,
        }

        return result_dict

    def getString(self):
        return f'| {self.mNo} | {self.mPrompt} | {self.mStyle} | {self.mOutImg} | {self.mInImg} | {self.mScore} | {self.mReason} | {self.mCaption} |'

    def __str__(self):
        return f'■ QueryItem: | {self.mNo} | {self.mPrompt} | {self.mStyle} | {self.mOutImg} | {self.mInImg} | {self.mScore} | {self.mReason} | {self.mCaption} |\n'


