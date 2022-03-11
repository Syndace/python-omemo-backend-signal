import doubleratchet

class SendRecvChain(doubleratchet.kdfchains.ConstKDFChain):
    def __init__(self, key):
        super().__init__(
            None,
            doubleratchet.recommended.ChainKeyKDF("SHA-256"),
            key
        )
