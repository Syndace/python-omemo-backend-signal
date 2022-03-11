import doubleratchet

from .sendrecvchain import SendRecvChain

class SymmetricKeyRatchet(doubleratchet.ratchets.SymmetricKeyRatchet):
    def __init__(self):
        super().__init__(SendRecvChain, SendRecvChain)
