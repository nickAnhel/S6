import typing as tp
from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Button, DataTable, Header, Footer, Collapsible
from textual.containers import VerticalScroll

from dependency_injector.wiring import Provide, inject

from containers import Container



BASE_DIR = Path(__file__).parent


class QueryRowTable(Collapsible):
    def __init__(
        self,
        fetch_data_func: tp.Callable[[], tp.Awaitable[list[dict[str, tp.Any]]]],
        *args,
        **kwargs,
    ) -> None:
        super().__init__(
            Button("▶", id="play", classes="button"),
            DataTable(id="customer-table", classes="table"),
            *args,
            **kwargs,
        )
        self.fetch_data = fetch_data_func

    async def on_button_pressed(
        self,
        event: Button.Pressed,
    ) -> None:
        if event.button.id == "play":
            data = await self.fetch_data()

            table = self.query_one("#customer-table", DataTable)
            table.clear()

            if data:
                if not table.columns:
                    table.add_columns(*data[0].keys())

                for row in data:
                    table.add_row(*row.values())


class Lab3App(App):
    CSS_PATH = BASE_DIR / "tcss" / "styles.tcss"

    @inject
    def compose(
        self,

    ) -> ComposeResult:
        yield Header()
        yield Footer()

        yield VerticalScroll()
