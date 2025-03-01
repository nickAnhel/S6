import typing as tp

import config
from utils import draw_history_plots, get_generators, get_model, print_metrics


BATCH_SIZE: tp.Final[int] = 32
EPOCHS: tp.Final[int] = 10


def main() -> None:
    # Create generators
    train_gen, validation_gen, test_gen = get_generators(batch_size=BATCH_SIZE)
    print()

    # Get FNN model
    model, history = get_model(
        epochs=EPOCHS,
        train_gen=train_gen,
        validation_gen=validation_gen,
    )

    # Print model metrics
    print_metrics(model, test_gen)

    # Draw accuracy and loss plots
    draw_history_plots(EPOCHS, history)


if __name__ == "__main__":
    main()
