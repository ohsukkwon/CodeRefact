# -*- coding: utf-8 -*-
from prompts.GenPromptASRConversation import GenPromptASRConversation
from prompts.GenPromptASRListen import GenPromptASRListen
from prompts.ScorePromptCorrection import ScorePromptCorrection
from prompts.ScorePromptEmoji import ScorePromptEmoji
from prompts.ScorePromptEvalImg import ScorePromptEvalImg
from prompts.ScorePromptToneCasual import ScorePromptToneCasual
from prompts.ScorePromptTonePolite import ScorePromptTonePolite
from prompts.ScorePromptToneProfessional import ScorePromptToneProfessional
from prompts.ScorePromptToneSocial import ScorePromptToneSocial
from prompts.ScorePromptTranslation import ScorePromptTranslation
from utils.GlobalVars import *

class ScorePromptFactory:
    def __init__(self):
        self.mMyAllPrompts = {}

    def getTargetPrompt(self, targetPromptName, argArgs):
        # if targetPromptName in self.mMyAllPrompts:
        #     return self.mMyAllPrompts[targetPromptName]
        # else:
        if targetPromptName == PROMPT_KEY_NAME_TRANS:
            self.mMyAllPrompts[PROMPT_KEY_NAME_TRANS] = ScorePromptTranslation(argArgs)
            return self.mMyAllPrompts[PROMPT_KEY_NAME_TRANS]
        elif targetPromptName == PROMPT_KEY_NAME_CORRECT:
            self.mMyAllPrompts[PROMPT_KEY_NAME_CORRECT] = ScorePromptCorrection(argArgs)
            return self.mMyAllPrompts[PROMPT_KEY_NAME_CORRECT]
        elif targetPromptName == PROMPT_KEY_NAME_EMOJI:
            self.mMyAllPrompts[PROMPT_KEY_NAME_EMOJI] = ScorePromptEmoji(argArgs)
            return self.mMyAllPrompts[PROMPT_KEY_NAME_EMOJI]
        elif targetPromptName == PROMPT_KEY_NAME_TONESOCIAL:
            self.mMyAllPrompts[PROMPT_KEY_NAME_TONESOCIAL] = ScorePromptToneSocial(argArgs)
            return self.mMyAllPrompts[PROMPT_KEY_NAME_TONESOCIAL]
        elif targetPromptName == PROMPT_KEY_NAME_TONEPOLITE:
            self.mMyAllPrompts[PROMPT_KEY_NAME_TONEPOLITE] = ScorePromptTonePolite(argArgs)
            return self.mMyAllPrompts[PROMPT_KEY_NAME_TONEPOLITE]
        elif targetPromptName == PROMPT_KEY_NAME_TONEPROFESSIONAL:
            self.mMyAllPrompts[PROMPT_KEY_NAME_TONEPROFESSIONAL] = ScorePromptToneProfessional(argArgs)
            return self.mMyAllPrompts[PROMPT_KEY_NAME_TONEPROFESSIONAL]
        elif targetPromptName == PROMPT_KEY_NAME_TONECASUAL:
            self.mMyAllPrompts[PROMPT_KEY_NAME_TONECASUAL] = ScorePromptToneCasual(argArgs)
            return self.mMyAllPrompts[PROMPT_KEY_NAME_TONECASUAL]
        elif targetPromptName == CONFIG_NAME_VALUE_LISTEN:
            self.mMyAllPrompts[CONFIG_NAME_VALUE_LISTEN] = GenPromptASRListen(argArgs)
            return self.mMyAllPrompts[CONFIG_NAME_VALUE_LISTEN]
        elif targetPromptName == CONFIG_NAME_VALUE_CONVERSATION:
            self.mMyAllPrompts[CONFIG_NAME_VALUE_CONVERSATION] = GenPromptASRConversation(argArgs)
            return self.mMyAllPrompts[CONFIG_NAME_VALUE_CONVERSATION]
        elif targetPromptName == CONFIG_NAME_VALUE_EVALIMG:
            self.mMyAllPrompts[CONFIG_NAME_VALUE_EVALIMG] = ScorePromptEvalImg(argArgs)
            return self.mMyAllPrompts[CONFIG_NAME_VALUE_EVALIMG]
        elif targetPromptName == CONFIG_NAME_VALUE_EVALCAPTION:
            self.mMyAllPrompts[CONFIG_NAME_VALUE_EVALCAPTION] = ScorePromptEvalImg(argArgs)
            return self.mMyAllPrompts[CONFIG_NAME_VALUE_EVALCAPTION]
        elif targetPromptName == CONFIG_NAME_VALUE_EVALDUMMY:
            self.mMyAllPrompts[CONFIG_NAME_VALUE_EVALDUMMY] = ScorePromptEvalImg(argArgs)
            return self.mMyAllPrompts[CONFIG_NAME_VALUE_EVALDUMMY]
        else:
            print(f"CRITICAL: Invalid args{argArgs}")
            return None
