import keras
import numpy as np
import pandas as pd
from keras.losses import binary_crossentropy

from dtsc330_26.classifiers import reusable_classifier
from dtsc330_26.readers import har

data = har.HAR(
    "data/motion-and-heart-rate-from-a-wrist-worn-wearable-and-labeled-sleep-from-polysomnography-1.0.0",
    10,
)
full_df = data.df
full_df.index = pd.to_timedelta(full_df["timestamp"], unit="s")


def create_model():
    # 10 minutes at 30 Hz
    inputs = keras.layers.Input(shape=(5, 10 * 60 * 30))  # 28,800
    x = keras.layers.Conv1D(16, (5, 5))(inputs)  # 28,798
    x = keras.layers.MaxPool1D(2)(x)  # 14,399
    x = keras.layers.Conv1D(16, (5, 5))(x)  # 14,397
    x = keras.layers.MaxPool1D(2)(x)  # 7198
    x = keras.layers.Conv1D(16, (5, 5))(x)  # 7196
    x = keras.layers.MaxPool1D(2)(x)  # 3598
    x = keras.layers.Conv1D(16, (5, 5))(x)
    x = keras.layers.MaxPool1D(2)(x)  # 1800
    x = keras.layers.Conv1D(16, (5, 5))(x)
    x = keras.layers.MaxPool1D(2)(x)  # 800
    x = keras.layers.Conv1D(16, (5, 5))(x)
    x = keras.layers.MaxPool1D(2)(x)  # 400
    x = keras.layers.Flatten()(x)

    x = keras.layers.Dense(1000, activation="relu")(x)
    x = keras.layers.Dense(400, activation="relu")(x)
    x = keras.layers.Dense(100, activation="relu")(x)
    x = keras.layers.Dense(20, activation="relu")(x)
    x = keras.layers.Dense(5, activation="relu")(x)
    x = keras.layers.Dense(1, activation="sigmoid")(x)

    model = keras.models.Model(inputs=inputs, outputs=x)
    return model


model = create_model()
model.compile(
    loss=binary_crossentropy, optimizer="adam"
)  # binary_crossentropy because it's a classifier, not a regressor
model.fit(features.values, features.values, epochs=50, batch_size=32, shuffle=True)

# We need to loop through peopel so that we don't average across them
people = pd.unique(full_df["person"])
features, labels, test_features, test_labels = [], [], [], []
for person in people:
    print(f"Computing person {person+1}")
    df = full_df.loc[full_df["person"] == person]
