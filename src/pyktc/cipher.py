class Cipher:
    def __init__(self, secret):
        self.alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key = ''.join(sorted(set(ch for ch in secret.upper() if ch in self.alpha), key=secret.upper().index))
        self.new_alpha = self.key + ''.join(ch for ch in self.alpha if ch not in self.key)

    def encrypt(self, message):
        return ''.join(self.new_alpha[self.alpha.index(ch)] if ch in self.alpha else ch for ch in message.upper())

    def decrypt(self, message):
        return ''.join(self.alpha[self.new_alpha.index(ch)] if ch in self.new_alpha else ch for ch in message.upper())