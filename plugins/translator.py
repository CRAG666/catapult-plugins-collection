import hashlib
import http.client
import json
import re
import urllib.parse
import urllib.request

# import requests
from catapult.api import (Plugin, SearchResult, copy_text_to_clipboard,
                          lookup_icon)
from catapult.i18n import _

cache = {}

PATTERN = re.compile(r"^tr\s([a-z]{2})\s([a-z]{2})\s(.*)\s")


class TranslatorPlugin(Plugin):
    save_history = False
    title = _("Translator")
    cache_key = ""

    def __init__(self):
        super().__init__()
        self.url = "/translate_a/single"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://translate.google.com/",
            "Origin": "https://translate.google.com",
        }
        self.conn = http.client.HTTPSConnection("translate.googleapis.com")

    def google_translate(self, text, source_language, target_language):
        self.cache_key = hashlib.md5(
            f"{text}{source_language}{target_language}".encode()
        ).hexdigest()
        if self.cache_key in cache:
            return cache[self.cache_key]

        params = {
            "client": "gtx",
            "sl": source_language,
            "tl": target_language,
            "dt": "t",
            "q": text,
        }

        data = urllib.parse.urlencode(params).encode("utf-8")

        self.conn.request("POST", self.url, data, self.headers)

        response = self.conn.getresponse()

        result_text = response.read().decode()

        # self.conn.close()

        try:
            result = json.loads(result_text)
            result_text = result[0][0][0]
        except (json.JSONDecodeError, IndexError):
            result_text = ""

        cache[self.cache_key] = result_text
        return result_text

    def launch(self, window, id):
        copy_text_to_clipboard(cache.get(self.cache_key, ""))

    def search(self, query):
        match = re.match(PATTERN, query)
        if not match:
            return

        src, dest, text = match.groups()
        result = self.google_translate(text, src, dest)
        if result:
            yield SearchResult(
                description=result,
                fuzzy=False,
                icon=lookup_icon(
                    "gnome-translate",
                    "deepin-translator",
                    "org.gnome.Translate",
                    "org.gnome.Translate",
                    "application-x-executable",
                ),
                id="0",
                offset=0,
                plugin=self,
                score=1,
                title="Traduccion",
            )
