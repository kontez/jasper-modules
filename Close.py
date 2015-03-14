# -*- coding: utf-8-*-

import re
import os

WORDS = ["CLOSE"]

def handle(text, mic, profile):
    """
        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """

    mic.say("Goodbye, master.")
    exit(0)
    
def isValid(text):
    """
        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bclose\b', text, re.IGNORECASE))
