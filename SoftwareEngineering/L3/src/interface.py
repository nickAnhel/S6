import typing as tp
from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import Button, DataTable, Header, Footer, Collapsible, Input
from textual.containers import VerticalScroll

from dependency_injector.wiring import Provide, inject

from containers import Container
from services import HotelsService, RoomsService, ServicesService, BookingsService, ClientsService


BASE_DIR = Path(__file__).parent


class QueryRowTable(Collapsible):
    def __init__(
        self,
        fetch_data_func: tp.Callable[[], list[dict[str, tp.Any]]],
        *args,
        **kwargs,
    ) -> None:
        super().__init__(
            Button("▶", id="play", classes="button"),
            DataTable(id="table", classes="table"),
            *args,
            **kwargs,
        )
        self.fetch_data = fetch_data_func

    def on_button_pressed(
        self,
        event: Button.Pressed,
    ) -> None:
        if event.button.id == "play":
            data = self.fetch_data()

            table = self.query_one("#table", DataTable)
            table.clear()

            if data:
                if not table.columns:
                    table.add_columns(*data[0].keys())

                for row in data:
                    table.add_row(*row.values())


class QueryRowTableWithInput(Collapsible):
    def __init__(
        self,
        fetch_data_func: tp.Callable[[tp.Any], list[dict[str, tp.Any]]],
        input_placeholder: str,
        *args,
        input_default: str = "",
        **kwargs,
    ) -> None:
        super().__init__(
            Input(input_default, placeholder=input_placeholder, classes="input-field"),
            Button("▶", id="play", classes="button"),
            DataTable(id="table", classes="table"),
            *args,
            **kwargs,
        )
        self.fetch_data = fetch_data_func

    def on_button_pressed(
        self,
        event: Button.Pressed,
    ) -> None:
        if event.button.id == "play":
            input_field = self.query_one(Input)

            if not input_field.value:
                self.query_one(Input).focus()
                return

            data = self.fetch_data(input_field.value)

            table = self.query_one("#table", DataTable)
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
        rooms_service: RoomsService = Provide[Container.rooms_service],
        services_service: ServicesService = Provide[Container.services_service],
        clients_service: ClientsService = Provide[Container.clients_service],
        hotels_service: HotelsService = Provide[Container.hotels_service],
        bookings_service: BookingsService = Provide[Container.bookings_service],
    ) -> ComposeResult:
        yield Header()
        yield Footer()

        yield VerticalScroll(
            QueryRowTable(
                rooms_service.get_all,
                title="Get all rooms",
            ),
            QueryRowTable(
                services_service.get_all_ordered_by_usage,
                title="Get all services orderes by usage",
            ),
            QueryRowTableWithInput(
                clients_service.get_client_bookings,
                title="Get client bookings by email",
                input_placeholder="Email",
                input_default="john.doe@example.com",
            ),
            QueryRowTable(
                hotels_service.get_hotel_serives,
                title="Get hotel services",
            ),
            QueryRowTableWithInput(
                bookings_service.get_bookings_with_service,
                title="Get bookings with service",
                input_placeholder="Service",
                input_default="Bar",
            ),
            QueryRowTableWithInput(
                rooms_service.get_available_double_rooms,
                title="Get double rooms available on date",
                input_placeholder="Date (YYYY-MM-DD)",
                input_default="2023-10-03",
            ),
            QueryRowTableWithInput(
                clients_service.get_clients_used_services,
                title="Get clients that used service",
                input_placeholder="Service",
                input_default="Bar",
            ),
            QueryRowTableWithInput(
                hotels_service.get_total_revenue,
                title="Get hotel total revenue",
                input_placeholder="Hotel name",
                input_default="Sunset Paradise",
            ),
        )
