class Cipher:
    def __init__(self, secret, props=None):
        if props is None:
            props = {
                'alpha': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                'toUpper': True,
                'stripCharacters': True,
                'addSpaces': True,
                'stripSpaces': True
            }

        self.props = props
        self.alpha = props['alpha']
        self.trans = []
        self.key = self._parse(secret)
        self.key = ''.join(sorted(set(self.key)))
        self.cipher = sorted(self.key)
        self.width = len(self.cipher)
        self.height = len(self.alpha) // len(self.cipher) + 1
        kAlpha = self.key + self.alpha
        kAlpha = ''.join(sorted(set(kAlpha)))
        padding = " " * abs(self.width * self.height - len(kAlpha))
        self.kAlpha = kAlpha + padding
        self.trans = [0] * len(self.cipher)

        for i, _ in enumerate(self.cipher):
            letter = self.kAlpha[i]
            if letter in self.cipher:
                cipherIndex = self.cipher.index(letter)
                self.trans[cipherIndex] = cipherIndex - i

        self.encryptedAlpha = self._parse(''.join(
            self.kAlpha[self._max(self._flatIndex(i) - self.trans[self._flatIndex(i) % self.width], len(self.kAlpha))] for i, _ in enumerate(self.kAlpha)
        ))

    def _distinct(self, val):
        return ''.join(sorted(set(val)))

    def _max(self, i, max_val):
        return min(i, max_val)

    def _flatIndex(self, i):
        return i // self.height + ((i % self.height) * self.width)

    def _addSpaces(self, s):
        return ' '.join(s[i:i+5] for i in range(0, len(s), 5)) if self.props['addSpaces'] else s

    def _crypt(self, s, alphaA, alphaB):
        return self._addSpaces(''.join(alphaA[alphaB.index(lttr)] for lttr in s if lttr in alphaB))

    def _convertCase(self, s):
        return s.upper() if self.props['toUpper'] else s

    def _stripCharacters(self, s):
        return ''.join(c for c in s if c.isalpha()) if self.props['stripCharacters'] else s

    def _stripSpaces(self, s):
        return s.replace(' ', '') if self.props['stripSpaces'] else s

    def _parse(self, s):
        return self._stripCharacters(self._stripSpaces(self._convertCase(s)))

    def encrypt(self, s):
        return self._crypt(self._parse(s), self.encryptedAlpha, self.alpha)

    def decrypt(self, s):
        return self._crypt(s, self.alpha, self.encryptedAlpha)
