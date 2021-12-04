import matplotlib.pyplot as plt
from typing import Sequence, Tuple, AnyStr

colors = ['tab:blue', 'tab:orange', 'tab:red', 'tab:green', 'tab:purple', 'tab:yellow']


def plot(x_values: Sequence[float], series: Sequence[Tuple[AnyStr, Sequence[float]]]):
    plt.rcdefaults()
    fig, ax = plt.subplots()

    for (label, y_values) in series:
        ax.plot(x_values, y_values, label=label)

    plt.legend(loc='upper right')
    plt.show()
