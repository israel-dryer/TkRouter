from typing import Protocol, Callable, TypeAlias, Optional

RouteParams: TypeAlias = dict[str, str]

class CommandWidget(Protocol):
    def configure(self, command: Callable) -> None: ...
