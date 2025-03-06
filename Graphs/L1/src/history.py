import sys
import readline


class HistoryNavigator:
    def __init__(self) -> None:
        self._history: list[str] = []
        self._current_index = 0

    def add_to_history(self, command: str) -> None:
        if command.strip() and (not self._history or command != self._history[-1]):
            self._history.append(command)
        self._current_index = len(self._history)

    def get_prev(self) -> str:
        if self._history:
            self._current_index: int = max(0, self._current_index - 1)
            return self._history[self._current_index]
        return ""

    def get_next(self) -> str:
        if self._history:
            self._current_index = min(len(self._history), self._current_index + 1)
            if self._current_index < len(self._history):
                return self._history[self._current_index]
        return ""


def input_with_history(prompt: str = ">>> ") -> str:
    navigator = HistoryNavigator()

    def hook() -> None:
        key = readline.get_line_buffer()

        if key == "\x1b[A":
            command = navigator.get_prev()
            sys.stdout.write("\r" + " " * (len(prompt) + len(readline.get_line_buffer())))
            sys.stdout.write("\r" + prompt + command)
            sys.stdout.flush()

        elif key == "\x1b[B":
            command = navigator.get_next()
            sys.stdout.write("\r" + " " * (len(prompt) + len(readline.get_line_buffer())))
            sys.stdout.write("\r" + prompt + command)
            sys.stdout.flush()

    readline.set_pre_input_hook(hook)

    command = input(prompt)
    navigator.add_to_history(command)
    return command
