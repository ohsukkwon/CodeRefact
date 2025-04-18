# -*- coding: utf-8 -*-
import datetime
import os
import sys
from pathlib import Path

from GlobalUtil import get_date_file_name
from utils.GlobalVars import *


class MyLog:
    def __init__(self, deviceID='', log_dir_path=Path(os.path.dirname(__file__)), argFname=None, serious_mode=False, log_buf_max_length = 1000):
        self._make_log_dir(log_dir_path)
        self.m_log_dir_path = log_dir_path

        if argFname is None:
            fname_date = get_date_file_name()

            if serious_mode:
                self.m_log_file_name = f'serious_log_{deviceID}_{fname_date}.{FILE_EXTENSION_WITHOUT_DOT_LOG}'
            else:
                self.m_log_file_name = f'log_{deviceID}_{fname_date}.{FILE_EXTENSION_WITHOUT_DOT_LOG}'
        else:
            self.m_log_file_name = argFname

        self.m_log_file_fullpath = f'{os.path.join(self.m_log_dir_path, self.m_log_file_name)}'

        self.mLogBufMaxLength = log_buf_max_length
        self.mLogBufferList = []

    def _make_log_dir(self, argDirPath):
        try:
            if not os.path.exists(argDirPath):
                os.makedirs(argDirPath)
        except OSError:
            print('Error: Creating directory. ' + str(argDirPath))

    def _add_log(self,msg=''):
        self.mLogBufferList.append(msg)
        self._check_buf()

    def _check_buf(self):
        if self.mLogBufMaxLength == LOG_BUFFER_SIZE_NO_FLUSH or len(self.mLogBufferList) < self.mLogBufMaxLength:
            return
        else:
            self._write_buffer()

    def _write_buffer(self):
        with open(self.m_log_file_fullpath, 'a', encoding='utf-8-sig') as log_file:
            for logItem in self.mLogBufferList:
                log_file.write(f'{str(logItem)}\n')
        self.mLogBufferList.clear()

    def flush_buffer(self):
        self._write_buffer()

    def close(self):
        self._write_buffer()

    def clear(self):
        self.mLogBufferList.clear()

    def get_my_path(self):
        return self.m_log_file_fullpath

    def append_to_my_path(self, argPath):
        self.m_log_dir_path = os.path.join(self.m_log_dir_path, argPath)
        self.m_log_file_fullpath = f'{os.path.join(self.m_log_dir_path, self.m_log_file_name)}'

        self._make_log_dir(self.m_log_dir_path)
        print(f'[__CheckSTEP__]append_to_my_path. => {self.m_log_file_fullpath}')

    def update_my_path(self, argPath):
        self.m_log_dir_path = argPath
        self.m_log_file_fullpath = f'{os.path.join(self.m_log_dir_path, self.m_log_file_name)}'

        self._make_log_dir(self.m_log_dir_path)
        print(f'update_my_path. => {self.m_log_file_fullpath}')

    def i(self, msg='', bShowTimeStamp=False):
        if bShowTimeStamp:
            now = datetime.datetime.now()
            timestamp = now.strftime('%Y-%m-%d %X(%f)')
            msg = f'[{timestamp}] [INFO] : {msg}\n'

        print(msg)
        self._add_log(msg)

    def d(self, msg='', bShowTimeStamp=False):
        if bShowTimeStamp:
            now = datetime.datetime.now()
            timestamp = now.strftime('%Y-%m-%d %X(%f)')
            msg = f'[{timestamp}] [DEBUG] : {msg}\n'

        print(msg)
        self._add_log(msg)

    def e(self, msg='', bShowTimeStamp=False, argGoExit=False):
        if bShowTimeStamp:
            now = datetime.datetime.now()
            timestamp = now.strftime('%Y-%m-%d %X(%f)')
            msg = f'[{timestamp}] [ERROR] : {msg}\n'

        print(msg)
        self._add_log(msg)
        if argGoExit:
            sys.exit(msg)

    def inner(self, idx=-1, msg=''):
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%d %X(%f)')
        log_msg = f'[{timestamp}] [INNER] : ===>>> [{idx}] : {msg}'

        print(log_msg)
        self._add_log(log_msg)

    def __str__(self):
        retstr = ""

        if hasattr(self, "m_log_file_fullpath") and len(self.m_log_file_fullpath) > 0:
            retstr = f'[__CheckSTEP__]■ MyLog : m_log_file_fullpath -> {self.m_log_file_fullpath}'
        else:
            retstr = "None."

        return retstr
