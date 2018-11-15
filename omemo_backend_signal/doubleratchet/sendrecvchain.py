from __future__ import absolute_import

import doubleratchet

class SendRecvChain(doubleratchet.kdfchains.ConstKDFChain):
    def __init__(self, key = None):
        """
        Note: The key parameter MUST NOT be None.
        """
        super(SendRecvChain, self).__init__(
            doubleratchet.recommended.ChainKeyKDF("SHA-256"),
            None,
            key
        )

    def serialize(self):
        return {
            "super": super(SendRecvChain, self).serialize()
        }

    @classmethod
    def fromSerialized(cls, serialized, *args, **kwargs):
        return super(SendRecvChain, cls).fromSerialized(
            serialized["super"],
            *args,
            **kwargs
        )
