# -*- coding: utf-8 -*-
from GlobalVars import *

class ASRGenResult:

    def __init__(self, argTestId):
        self.mTestId = argTestId
        self.mStartTime = None
        self.mEndTime = None
        self.mDuration = None
        self.mTargetPath = None
        self.mAsrGenCfgInfo = self.ASRGenCfgInfo()
        self.mAsrGptScenarioResult = None
        self.mAsrRAIvoiceResult = None

    def add_asr_info(self, argStartTime, argEndTimd, argDuration, argTargetPath):
        self.mStartTime = argStartTime
        self.mEndTime = argEndTimd
        self.mDuration = argDuration
        self.mTargetPath = argTargetPath

    def add_cfg_summary(self, argPath, argMode, argSubject, argWordsCountOf1Line, argTotalCountOfSentences, argCfgMotherLanguage):
        self.mAsrGenCfgInfo.add_summary(argPath, argMode, argSubject, argWordsCountOf1Line, argTotalCountOfSentences, argCfgMotherLanguage)

    def add_cfg_person(self, argPersonId, argName):
        self.mAsrGenCfgInfo.add_person(argPersonId, argName)

    def add_cfg_person_info(self, argPersonId, argVoiceEngine, argVoiceId, argMyLang):
        self.mAsrGenCfgInfo.add_person_info(argPersonId, argVoiceEngine, argVoiceId, argMyLang)

    def add_gpt_scenario_result(self, argRetryCount, argTotalTokens, argStartTime, argEndTime, argDuration, argResult, argTargetPath):
        self.mAsrGptScenarioResult = self.ASRGptScenarioResult(argRetryCount, argTotalTokens, argStartTime, argEndTime, argDuration, argResult, argTargetPath)

    def add_ai_voice_result(self, argStartTime, argEndTime, argDuration, argResult, argTargetPath):
        self.mAsrRAIvoiceResult = self.ASRAIvoiceResult(argStartTime, argEndTime, argDuration, argResult, argTargetPath)

    def __str__(self):
        return (f'[ASRGenResult:{self.mTestId}] StartTime:{self.mStartTime} EndTime:{self.mEndTime} Duration:{self.mDuration} TargetPath:{self.mTargetPath}\n'
                f'{self.mAsrGenCfgInfo}\n{self.mAsrGptScenarioResult}\n{self.mAsrRAIvoiceResult}')

    class ASRGenCfgInfo:
        def __init__(self):
            self.mSummary = None
            self.mPerson = []

        def add_summary(self, argPath, argMode, argSubject, argWordsCountOf1Line, argTotalCountOfSentences, argCfgMotherLanguage):
            self.mSummary = self.ASRGenCfgSummary(argPath, argMode, argSubject, argWordsCountOf1Line, argTotalCountOfSentences, argCfgMotherLanguage)

        def add_person(self, argPersonId, argName):
            self.mPerson.append(self.ASRGenCfgPerson(argPersonId, argName))

        def add_person_info(self, argPersonId, argVoiceEngine, argVoiceId, argMyLang):
            self.mPerson[argPersonId].add_person_info(argVoiceEngine, argVoiceId, argMyLang)

        def __str__(self):
            return (f'[ASRGenCfgInfo] {self.mSummary}\n{self.mPerson[IDX_ASR_GEN_RESULT_CFG_PERSONA1]}\n'
                    f'{self.mPerson[IDX_ASR_GEN_RESULT_CFG_PERSONA2] if len(self.mPerson) == 2 else ""}')

        class ASRGenCfgSummary:
            def __init__(self, argPath, argMode, argSubject, argWordsCountOf1Line, argTotalCountOfSentences, argCfgMotherLanguage):
                self.mPath = argPath
                self.mMode = argMode
                self.mSubject = argSubject
                self.mWordsCountOf1Line = argWordsCountOf1Line
                self.mTotalCountOfSentences = argTotalCountOfSentences
                self.mCfgMotherLanguage = argCfgMotherLanguage

            def __str__(self):
                return f'{self.mPath}\n[ASRGenCfgSummary] Mode:{self.mMode} Subject:{self.mSubject} WordsCountOf1Line:{self.mWordsCountOf1Line} TotalCountOfSentences:{self.mTotalCountOfSentences} CfgMotherLanguage:{self.mCfgMotherLanguage}'

        class ASRGenCfgPerson:
            def __init__(self, argPersonId, argName):
                self.mPersonId = argPersonId
                self.mName = argName
                self.mVoiceEngine = None
                self.mVoiceId = None
                self.mMyLang = None

            def add_person_info(self, argVoiceEngine, argVoiceId, argMyLang):
                self.mVoiceEngine = argVoiceEngine
                self.mVoiceId = argVoiceId
                self.mMyLang = argMyLang

            def __str__(self):
                if self.mPersonId == IDX_ASR_GEN_RESULT_CFG_PERSONA2:
                    return f'[ASRGenCfgPerson2] VoiceEngine:{self.mVoiceEngine} VoiceId:{self.mVoiceId} Name:{self.mName} MyLang:{self.mMyLang}'
                return f'[ASRGenCfgPerson] VoiceEngine:{self.mVoiceEngine} VoiceId:{self.mVoiceId} Name:{self.mName} MyLang:{self.mMyLang}'

    class ASRGptScenarioResult:
        def __init__(self, argRetryCount, argTotalTokens, argStartTime, argEndTime, argDuration, argResult, argTargetPath):
            self.mRetryCount = argRetryCount
            self.mTotalTokens = argTotalTokens
            self.mStartTime = argStartTime
            self.mEndTime = argEndTime
            self.mDuration = argDuration
            self.mResult = argResult
            self.mTargetPath = argTargetPath

        def __str__(self):
            return f'[ASRGptScenarioResult] RetryCount:{self.mRetryCount} TotalTokens:{self.mTotalTokens} StartTime:{self.mStartTime} EndTime:{self.mEndTime} Duration:{self.mDuration} Result:{self.mResult} TargetPath:{self.mTargetPath}'

    class ASRAIvoiceResult:
        def __init__(self, argStartTime, argEndTime, argDuration, argResult, argTargetPath):
            self.mStartTime = argStartTime
            self.mEndTime = argEndTime
            self.mDuration = argDuration
            self.mResult = argResult
            self.mTargetPath = argTargetPath

        def __str__(self):
            return f'[ASRAIvoiceResult] StartTime:{self.mStartTime} EndTime:{self.mEndTime} Duration:{self.mDuration} Result:{self.mResult} TargetPath:{self.mTargetPath}'
