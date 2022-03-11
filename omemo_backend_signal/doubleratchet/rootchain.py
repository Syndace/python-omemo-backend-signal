import doubleratchet

class RootChain(doubleratchet.kdfchains.KDFChain):
    def __init__(self, key = None):
        super().__init__(
            doubleratchet.recommended.RootKeyKDF(
                "SHA-256",
                "WhisperRatchet".encode("US-ASCII")
            ),
            key
        )
