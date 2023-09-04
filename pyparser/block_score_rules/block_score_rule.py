from __future__ import annotations
from abc import abstractmethod, ABCMeta

from ..blocks.block import Block


class BlockScoreRule(metaclass=ABCMeta):
    @abstractmethod
    def score(blocks: list[Block]) -> int:
        ...