from __future__ import absolute_import

import doubleratchet

class RootChain(doubleratchet.kdfchains.KDFChain):
    def __init__(self, key):
        super(RootChain, self).__init__(
            doubleratchet.recommended.RootKeyKDF(
                "SHA-256",
                "WhisperRatchet".encode("US-ASCII")
            ),
            key
        )
