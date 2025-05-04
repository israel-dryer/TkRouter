from typing import Any, List, Optional, Callable
from .exceptions import HistoryNavigationError


class History:
    """
    Manages a stack-based history mechanism with a navigable index.

    This class provides a forward/backward navigation model similar to browser history.
    It is used internally by the Router to manage path transitions and enable features
    like 'back', 'forward', and 'go(delta)' navigation.

    Attributes:
        _stack (List[Any]): Internal list storing the navigation history.
        _index (int): Index pointing to the current location in the stack.
    """

    def __init__(self) -> None:
        """
        Initializes an empty history stack and sets the index to -1 (no entries yet).
        """
        self._stack: List[Any] = []
        self._index: int = -1

    def push(self, path: Any) -> Any:
        """
        Adds a new path to the top of the history stack.

        If the current index is not at the top of the stack, the stack is truncated
        before the new path is pushed. Updates the current index to point to the new path.

        Args:
            path (Any): The new path to push onto the history stack.

        Returns:
            Any: The path that was added.

        Raises:
            ValueError: If the path is None or an empty value.
        """
        if not path:
            raise ValueError("Path cannot be None or an empty value.")
        self._stack = self._stack[:self._index + 1]
        self._stack.append(path)
        self._index += 1
        return path

    def replace(self, path: Any) -> None:
        """
        Replaces the current path in the history stack with a new value.

        Args:
            path (Any): The new path to replace the current entry.

        Raises:
            ValueError: If the path is None or an empty value.
            HistoryNavigationError: If there is no valid item to replace.
        """
        if not path:
            raise ValueError("Path cannot be None or an empty value.")
        if self._index < 0 or self._index >= len(self._stack):
            raise HistoryNavigationError("Cannot replace path in an invalid history state.")
        self._stack[self._index] = path

    def back(self) -> Optional[Any]:
        """
        Moves one step backward in the history stack.

        Returns:
            Optional[Any]: The new current path after moving backward.

        Raises:
            HistoryNavigationError: If already at the beginning of the stack.
        """
        if not self.can_go_back:
            raise HistoryNavigationError("Cannot go back. Already at the beginning of the stack.")
        self._index -= 1
        return self._stack[self._index]

    def forward(self) -> Optional[Any]:
        """
        Moves one step forward in the history stack.

        Returns:
            Optional[Any]: The new current path after moving forward.

        Raises:
            HistoryNavigationError: If already at the end of the stack.
        """
        if not self.can_go_forward:
            raise HistoryNavigationError("Cannot go forward. Already at the end of the stack.")
        self._index += 1
        return self._stack[self._index]

    def go(self, delta: int) -> Optional[Any]:
        """
        Jumps forward or backward in the stack by a relative offset.

        Args:
            delta (int): Number of steps to move. Negative = backward, positive = forward.

        Returns:
            Optional[Any]: The path at the new index, or None if the jump is out of bounds.
        """
        target_index = self._index + delta
        if 0 <= target_index < len(self._stack):
            self._index = target_index
            return self._stack[self._index]
        return None

    def current(self) -> Optional[Any]:
        """
        Retrieves the current path in the history stack.

        Returns:
            Optional[Any]: The current path, or None if history is empty.
        """
        return self._stack[self._index] if self._index >= 0 else None

    def clear(self, callback: Optional[Callable[[], None]] = None) -> None:
        """
        Clears the entire history stack and resets the index.

        Args:
            callback (Optional[Callable[[], None]]): Optional function to call after clearing.
        """
        self._stack = []
        self._index = -1
        if callback:
            callback()

    @property
    def size(self) -> int:
        """
        Returns:
            int: The number of items currently in the stack.
        """
        return len(self._stack)

    @property
    def can_go_back(self) -> bool:
        """
        Returns:
            bool: True if you can go backward in history.
        """
        return self._index > 0

    @property
    def can_go_forward(self) -> bool:
        """
        Returns:
            bool: True if you can go forward in history.
        """
        return self._index + 1 < len(self._stack)

    def __repr__(self) -> str:
        """
        Returns:
            str: Debug string representation of the history stack and current index.
        """
        return f"History(stack={self._stack}, index={self._index})"
