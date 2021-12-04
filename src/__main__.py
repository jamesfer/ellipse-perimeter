import numpy
import math
from typing import Sequence, Iterator

from .learn import fit_model, build_relu_model, build_tanh_model, build_big_relu_model, build_sigmoid_model, \
    build_exponential_model
from .dataset import make_ellipse_dataset
from .plot import plot
from .formulae import approximate_perimeter, approximate_perimeter_ramanujan, perimeter_by_series, \
    approximate_perimeter_ramanujan_2


def calculate_error_percentage(accurate_values: Iterator[float], estimate_values: Iterator[float]) -> Iterator[float]:
    return [math.fabs(accurate - estimate) / accurate * 100 for (accurate, estimate) in zip(accurate_values, estimate_values)]


def normalize(dataset):
    stats = dataset.describe().transpose()
    return (dataset - stats['mean']) / stats['std']


if __name__ == '__main__':
    training_ellipses, training_labels, test_ellipses, test_labels = make_ellipse_dataset(5, 10000)
    norm_training_ellipses = normalize(training_ellipses)
    norm_test_ellipses = normalize(test_ellipses)
    norm_training_labels = normalize(training_labels)
    norm_test_labels = normalize(test_labels)

    ramanujan_2_predictions = [approximate_perimeter_ramanujan_2(a, 1) for a in test_ellipses['a']]

    relu_model = build_relu_model()
    big_relu_model = build_big_relu_model()
    tanh_model = build_tanh_model()
    sigmoid_model = build_sigmoid_model()
    exponential_model = build_exponential_model()

    relu_model, big_relu_mode, tanh_model, sigmoid_model, exponential_model = list(map(
        lambda m: fit_model(m, norm_training_ellipses, training_labels),
        [relu_model, big_relu_model, tanh_model, sigmoid_model, exponential_model]
    ))

    # model.evaluate(test_ellipses, test_labels, verbose=2)

    plot(test_ellipses, [
        # list(calculate_error_percentage(actual, [approximate_perimeter(a, b) for (a, b) in ellipses])),
        # list(calculate_error_percentage(test_labels, [approximate_perimeter_ramanujan(a, 1) for a in test_ellipses['a']])),
        # ('ramanujan_2', list(calculate_error_percentage(test_labels, ramanujan_2_predictions))),
        ('relu', list(calculate_error_percentage(test_labels, relu_model.predict(norm_test_ellipses).flatten()))),
        ('big_relu', list(calculate_error_percentage(test_labels, big_relu_model.predict(norm_test_ellipses).flatten()))),
        ('tanh', list(calculate_error_percentage(test_labels, tanh_model.predict(norm_test_ellipses).flatten()))),
        ('sigmoid', list(calculate_error_percentage(test_labels, sigmoid_model.predict(norm_test_ellipses).flatten()))),
        ('exponential', list(calculate_error_percentage(test_labels, exponential_model.predict(norm_test_ellipses).flatten()))),
    ])
