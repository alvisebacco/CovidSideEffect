import hashlib


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
