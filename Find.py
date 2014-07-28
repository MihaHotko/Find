#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class Search():
    def find_email(self,string="",patt='@',file_name=None):
        """
            Returns a list of emails in a file or string
        """
        f_string=""
        if file_name == None and string != "":
            search = re.findall(r'[a-z0-9(\.a-z0-9|a-z0-9)\.a-z0-9]+%s[a-z0-9]+\.[\w]+'%patt,string, re.IGNORECASE)
            return search
        else:
            with open(file_name,'r') as f:
                f_read = f.read()
                f_string += f_read
                search = re.findall(r'[\w\.-]+%s[\w\.-]+'%patt,f_string)
                return search
                f.close()

    def find_string(self):
        """
            Returns a list of a certain string in file or string
        """
        pass
