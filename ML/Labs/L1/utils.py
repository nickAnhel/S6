import typing as tp
from pathlib import Path

import matplotlib.pyplot as plt

from keras._tf_keras.keras.callbacks import History
from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import Flatten, Dense, Dropout
from keras._tf_keras.keras.preprocessing.image import DirectoryIterator, ImageDataGenerator

BASE_DIR: tp.Final[Path] = Path(__file__).parent
TRAIN_DIR: tp.Final[Path] = BASE_DIR / "dataset" / "train"
TEST_DIR: tp.Final[Path] = BASE_DIR / "dataset" / "test"


def get_generators(batch_size: int) -> tuple[DirectoryIterator, DirectoryIterator, DirectoryIterator]:
    """Get generators for train, validation and test selections."""

    # Create test and train data generators
    train_valid_datagen = ImageDataGenerator(rescale=1.0 / 255.0, validation_split=0.2)
    test_datagen = ImageDataGenerator(rescale=1.0 / 255.0)

    # Create and return generators for train, validation and test selections
    return (
        train_valid_datagen.flow_from_directory(
            TRAIN_DIR,
            target_size=(48, 48),
            batch_size=batch_size,
            color_mode="grayscale",
            class_mode="categorical",
            subset="training",
        ),
        train_valid_datagen.flow_from_directory(
            TRAIN_DIR,
            target_size=(48, 48),
            batch_size=batch_size,
            color_mode="grayscale",
            class_mode="categorical",
            subset="validation",
        ),
        test_datagen.flow_from_directory(
            TEST_DIR,
            target_size=(48, 48),
            batch_size=batch_size,
            color_mode="grayscale",
            class_mode="categorical",
        ),
    )


def get_model(
    *,
    epochs: int,
    train_gen: DirectoryIterator,
    validation_gen: DirectoryIterator,
) -> tuple[Sequential, History]:
    """Get FNN model."""

    # Create FNN model
    model = Sequential()

    # Add layers to model
    model.add(Flatten(input_shape=(48, 48, 1)))
    model.add(Dense(512, activation="relu"))
    model.add(Dense(256, activation="relu"))
    model.add(Dense(7, activation="softmax"))

    # Compile model
    model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

    # Print model summary
    model.summary()
    print()

    # Fit model
    history = model.fit(train_gen, validation_data=validation_gen, epochs=epochs)

    return model, history


def draw_history_plots(
    epochs: int,
    history: History,
) -> None:
    """Draw plots for model history."""

    _, axes = plt.subplots(1, 2, figsize=(10, 4))

    # Accuracy plot
    axes[0].plot(
        range(1, epochs + 1),
        history.history["accuracy"],
        history.history["val_accuracy"],
    )
    axes[0].legend(["Train Accuracy", "Validation Accuracy"])
    axes[0].set_title("Accuracy")
    axes[0].set_xlabel("Epochs")
    axes[0].set_ylabel("Accuracy")
    axes[0].grid(True)

    # Loss plot
    axes[1].plot(
        range(1, epochs + 1),
        history.history["loss"],
        history.history["val_loss"],
    )
    axes[1].set_title("Loss")
    axes[1].legend(["Train Loss", "Validation Loss"])
    axes[1].set_xlabel("Epochs")
    axes[1].set_ylabel("Loss")
    axes[1].grid(True)

    plt.show()


def print_metrics(
    model: Sequential,
    test_gen: DirectoryIterator,
) -> None:
    """Print metrics for FNN model."""

    test_loss, test_accuracy = model.evaluate(test_gen)

    print("\nMetrics")
    print(f"Test Loss:     {test_loss:.5f}")
    print(f"Test Accuracy: {test_accuracy:.5f}")
