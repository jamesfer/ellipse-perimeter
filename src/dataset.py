import pandas
import numpy

from .formulae import perimeter_by_series


def make_ellipse_dataset(max_ratio: float, count: int):
    major_axis_values = numpy.arange(1, max_ratio, (max_ratio - 1) / count)
    perimeters = map(lambda a: perimeter_by_series(a, 1), major_axis_values)

    dataset = pandas.DataFrame({'a': major_axis_values, 'perimeter': perimeters})

    training_ellipses = dataset.sample(frac=0.8, random_state=0)
    test_ellipses = dataset.drop(training_ellipses.index)

    training_labels = training_ellipses.pop('perimeter')
    test_labels = test_ellipses.pop('perimeter')

    return [training_ellipses, training_labels, test_ellipses, test_labels]

