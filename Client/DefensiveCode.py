class Defender:

    @staticmethod
    def password(word):
        if len(word) >= 4:
            if ' ' not in word:
                return True
            return False
        return False

    @staticmethod
    def fiscal_code(word):
        if len(word) == 11 or len(word) == 16:
            if ' ' not in word:
                return True
            return False
        return False

    @staticmethod
    def password_is_re_password(passwd, repasswd):
        if passwd == repasswd:
            return True
        return False

    @staticmethod
    def get_password_hash(password):
        return hash(password)
