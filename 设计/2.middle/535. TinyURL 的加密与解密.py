# -*- coding: utf-8 -*-
# @Time    : 2021/3/29 14:14
# @File    : 535. TinyURL 的加密与解密.py

class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.code = {}
        self.code['http://tinyurl.com/' + str(len(self.code))] = longUrl
        return 'http://tinyurl.com/' + str(len(self.code) - 1)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.code[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
