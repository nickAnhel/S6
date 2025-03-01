from containers import Container
from interface import Lab3App


def main() -> None:
    # Setup DI Container
    container = Container()
    container.wire(modules=["interface"])

    # Setup textual app
    app = Lab3App()
    app.run()


if __name__ == "__main__":
    main()
