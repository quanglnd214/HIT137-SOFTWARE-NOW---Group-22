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

    def __init__(self, max_states: int = 30) -> None:
        self.undo_stack = []
        self.redo_stack = []
        self.max_states = max_states

    def clear(self) -> None:
        self.undo_stack.clear()
        self.redo_stack.clear()

    def push(self, state) -> None:
        """Save a copy of the current state for undo."""
        if state is None:
            return

        # store a copy so later changes don't affect history
        self.undo_stack.append(state.copy())
        self.redo_stack.clear()

        # keep history size under control
        if len(self.undo_stack) > self.max_states:
            self.undo_stack.pop(0)

    def undo(self, current_state):
        """Return the previous state, or None if not available."""
        if not self.undo_stack or current_state is None:
            return None

        self.redo_stack.append(current_state.copy())
        return self.undo_stack.pop()

    def redo(self, current_state):
        """Return the next state, or None if not available."""
        if not self.redo_stack or current_state is None:
            return None

        self.undo_stack.append(current_state.copy())
        return self.redo_stack.pop()