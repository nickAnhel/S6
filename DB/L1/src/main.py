from containers import Container
from interface import Lab1App


def main():
    # Setup DI
    container = Container()
    container.wire(modules=["interface"])

    # Run Textual app
    app = Lab1App()
    app.run()


if __name__ == "__main__":
    main()
