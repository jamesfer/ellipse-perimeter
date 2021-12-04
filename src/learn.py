import tensorflow
from tensorflow.keras.layers import Dense


def compile_model(model):
    optimizer = tensorflow.keras.optimizers.RMSprop(0.001)

    model.compile(loss='mse',
                  optimizer=optimizer,
                  metrics=['mae', 'mse'])

    return model


def build_relu_model():
    return compile_model(tensorflow.keras.Sequential([
        Dense(128, activation='relu', input_shape=[1]),
        Dense(128, activation='relu'),
        Dense(1),
    ]))


def build_big_relu_model():
    return compile_model(tensorflow.keras.Sequential([
        Dense(256, activation='relu', input_shape=[1]),
        Dense(256, activation='relu'),
        Dense(256, activation='relu'),
        Dense(1),
    ]))


def build_tanh_model():
    return compile_model(tensorflow.keras.Sequential([
        Dense(256, activation='tanh', input_shape=[1]),
        Dense(256, activation='tanh'),
        Dense(256, activation='tanh'),
        Dense(1),
    ]))


def build_sigmoid_model():
    return compile_model(tensorflow.keras.Sequential([
        Dense(128, activation='sigmoid', input_shape=[1]),
        Dense(128, activation='sigmoid'),
        Dense(1),
    ]))


def build_exponential_model():
    return compile_model(tensorflow.keras.Sequential([
        Dense(128, activation='exponential', input_shape=[1]),
        Dense(128, activation='exponential'),
        Dense(1),
    ]))


def fit_model(model, train_data, train_labels):
    early_stop = tensorflow.keras.callbacks.EarlyStopping(monitor='val_loss', patience=50)

    model.fit(
        train_data,
        train_labels,
        epochs=1000,
        validation_split=0.2,
        # verbose=0,
        callbacks=[early_stop]
    )

    return model
