import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from keras._tf_keras.keras.datasets import mnist


def get_dataset() -> np.ndarray:
    (x, _), _ = mnist.load_data()

    x = x[:100]
    x = tf.image.resize(tf.convert_to_tensor(x[..., np.newaxis]), (10, 10)).numpy().squeeze()
    x = (x > 127).astype(np.int8)
    x[x == 0] = -1
    x = x.reshape(-1, 100)

    return x


def get_train_subset(dataset: np.ndarray) -> np.ndarray:
    train_indices = np.random.choice(len(dataset), size=5, replace=False)
    return dataset[train_indices]


def get_noisy_image(image: np.ndarray, noise_level: float = 0.1) -> np.ndarray:
    noisy = image.copy()
    indices = np.random.rand(len(image)) < noise_level
    noisy[indices] *= -1
    return noisy


def draw_images(
    title: str,
    subplot_titles: list[str],
    *images: np.ndarray,
) -> None:
    fig, ax = plt.subplots(1, len(images), figsize=(10, 3.5))
    fig.suptitle(title, fontsize=15)

    for i, image in enumerate(images):
        ax[i].matshow(image.reshape(10, 10), cmap="gray")
        ax[i].set_title(subplot_titles[i])
        ax[i].set_xticks([])
        ax[i].set_yticks([])

    plt.show()
