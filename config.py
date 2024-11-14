#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7924605822:AAFc7To_ndjnk47DTPZKRu4apXTGYQiXwks")
    API_ID = int(os.environ.get("API_ID", "28187462"))
    API_HASH = os.environ.get("API_HASH", "0159fbade6b803a808fbc5e248d52b87")
    AUTH_USERS = "1291491834"

