import typing as tp
from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Button, DataTable, Header, Footer, Collapsible
from textual.containers import VerticalScroll

from dependency_injector.wiring import Provide, inject

from containers import Container
from services import CustomersService, PartsService, SalesService


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


class QueryRowPlot(Collapsible):
    def __init__(
        self,
        draw_plot_func: tp.Callable[[], tp.Awaitable[None]],
        *args,
        **kwargs,
    ) -> None:
        super().__init__(
            Button("▶", id="play", classes="button"),
            *args,
            **kwargs,
        )
        self.draw_plot = draw_plot_func

    async def on_button_pressed(
        self,
        event: Button.Pressed,
    ) -> None:
        if event.button.id == "play":
            await self.draw_plot()


class Lab1App(App):
    CSS_PATH = BASE_DIR / "tcss" / "styles.tcss"

    @inject
    def compose(
        self,
        customers_service: CustomersService = Provide[Container.customers_service],
        parts_service: PartsService = Provide[Container.parts_service],
        sales_service: SalesService = Provide[Container.sales_service],
    ) -> ComposeResult:
        yield Header()
        yield Footer()

        yield VerticalScroll(
            QueryRowTable(
                customers_service.get_all_customers,
                title="Get all customers",
            ),
            QueryRowTable(
                parts_service.get_top5_parts_by_sales,
                title="Get top 5 parts by sales (table)",
            ),
            QueryRowPlot(
                parts_service.draw_top5_parts_by_sales,
                title="Get top 5 parts by sales (plot)",
            ),
            QueryRowTable(
                parts_service.get_parts_retail_selling_price_difference,
                title="Get average difference between selling and retail price for each part (table)",
            ),
            QueryRowPlot(
                parts_service.draw_parts_retail_selling_price_difference,
                title="Get average difference between selling and retail price for each part (plot)",
            ),
            QueryRowTable(
                sales_service.get_monthly_revenue,
                title="Get monthly revenue (table)",
            ),
            QueryRowPlot(
                sales_service.draw_monthly_revenue,
                title="Get monthly revenue (plot)",
            ),
        )
