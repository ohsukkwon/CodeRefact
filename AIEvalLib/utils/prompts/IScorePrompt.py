# -*- coding: utf-8 -*-
from abc import *

from utils.GlobalVars import *


class IScorePrompt(metaclass=ABCMeta):

    @abstractmethod
    def get_my_keyname(self):
        pass

    @abstractmethod
    def get_my_csvname(self):
        pass

    def update_arg_to(self, argkey, argval):
        if hasattr(self, 'mArgs'):
            self.mArgs.setValInnerArg(argkey, argval)

    def get_value(self, argkey, argDefInNone=None):
        return self.mArgs.getValInnerArg(argkey, argDefInNone)

    @abstractmethod
    def get_noti_role_prompt(self):
        pass

    @abstractmethod
    def get_do_score_prompt(self):
        pass

    @abstractmethod
    def get_again_form_prompt(self):
        pass

    def get_sentence_gensentences_prompt(self):
        pass

    def get_sentence_template_prompt(self):
        pass

    def get_again_form_trans_prompt(self):
        return '''내가 원하는 답변 형식이 아니야. 다시 한번 답변해줘.'''

    def get_prompt(self, pmtType):

        if pmtType == PROMPT_COMMAND_KEY_NAME_NOTIROLE:
            print(PROMPT_COMMAND_KEY_NAME_NOTIROLE)
            return self.get_noti_role_prompt()

        elif pmtType == PROMPT_COMMAND_KEY_NAME_DOSCORE:
            print(PROMPT_COMMAND_KEY_NAME_DOSCORE)
            return self.get_do_score_prompt()

        elif pmtType == PROMPT_COMMAND_KEY_NAME_AGAINFORM:
            print(PROMPT_COMMAND_KEY_NAME_AGAINFORM)
            return self.get_again_form_prompt()

        elif pmtType == PROMPT_COMMAND_KEY_NAME_AGAINFORM_TRANS:
            print(PROMPT_COMMAND_KEY_NAME_AGAINFORM_TRANS)
            return self.get_again_form_trans_prompt()

        elif pmtType == PROMPT_COMMAND_KEY_NAME_TEMPLATE:
            print(PROMPT_COMMAND_KEY_NAME_TEMPLATE)
            return self.get_sentence_template_prompt()

        elif pmtType == PROMPT_COMMAND_KEY_NAME_GENSENTS:
            print(PROMPT_COMMAND_KEY_NAME_GENSENTS)
            return self.get_sentence_gensentences_prompt()

        else:
            print('Unknown pmyType' + pmtType)
            return None