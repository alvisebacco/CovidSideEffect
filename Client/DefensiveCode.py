import hashlib
from datetime import datetime


class Defender:

    @staticmethod
    def name_surname(word: str) -> bool:
        if len(word) > 0:
            if word.isalpha():
                return True
            return False
        return False

    @staticmethod
    def password(word: str) -> bool:
        if len(word) >= 4:
            if ' ' not in word:
                return True
            return False
        return False

    @staticmethod
    def fiscal_code(word: str) -> bool:
        if len(word) == 11 or len(word) == 16:
            if ' ' not in word:
                return True
            return False
        return False

    @staticmethod
    def password_is_re_password(passwd: str, re_passwd: str) -> bool:
        if passwd == re_passwd:
            return True
        return False

    @staticmethod
    def year_is_only_year(yyyy: int) -> bool:
        this_year = datetime.today().year
        this_year = int(this_year)
        if yyyy-100 <= yyyy <= this_year:
            return True
        return False
