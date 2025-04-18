# -*- coding: utf-8 -*-

class ResultTotalTestInfo:

    def __init__(self, argTestId):
        self.mTestId = argTestId
        self.mStartTime = None
        self.mEndTime = None
        self.mDuration = None
        self.mTargetPath = None

    def __str__(self):
        return f'[ResultTotalTestInfo:{self.mTestId}] StartTime:{self.mStartTime} EndTime:{self.mEndTime} Duration:{self.mDuration} TargetPath:{self.mTargetPath}\n'
