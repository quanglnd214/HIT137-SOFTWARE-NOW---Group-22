from __future__ import annotations


class HistoryStats:
    undo_count: int
    redo_count: int


class HistoryManager:
    """Undo/redo manager using two stacks.

    Policy:
    - keeping track of past image states
    - putting states back in place when you undo or redo actions
    """
    pass
