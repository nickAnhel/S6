import numpy as np
from tqdm import tqdm


class HopfieldNetwork:
    def __init__(self, size: int) -> None:
        self._size: int = size
        self._weights: np.ndarray = np.zeros((size, size))

    def train(self, patterns: np.ndarray) -> None:
        for pattern in tqdm(patterns):
            pattern = pattern.reshape((self._size, 1))
            self._weights += np.dot(pattern, pattern.T)

        np.fill_diagonal(self._weights, 0)
        self._weights /= len(patterns)

    def predict(self, pattern: np.ndarray) -> np.ndarray:
        output = np.dot(self._weights, pattern)
        return np.where(output >= 0, 1, -1)

    def test(self, original: np.ndarray, noisy: np.ndarray) -> tuple[float, np.ndarray]:
        recovered = self.predict(noisy)
        accuracy = np.mean(original == recovered) * 100
        return accuracy, recovered
