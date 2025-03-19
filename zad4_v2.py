import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# a) Wybór modelu pre-trained (MobileNetV2), wczytujemy model bez górnych warstw (include_top=False)
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False

# b) Dodawanie dodatkowych warstw
x = base_model.output
x = Flatten()(x)  # Spłaszczamy dane wyjściowe z modelu bazowego
x = Dense(128, activation='relu')(x)
x = Dropout(0.5)(x)  # Dropout, aby zapobiec przeuczeniu
output_layer = Dense(1, activation='sigmoid')(x)  # Warstwa wyjściowa (1 neuron, klasyfikacja binarna)

model = Model(inputs=base_model.input, outputs=output_layer)

# c)Kompilacja modelu
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.summary()

train_datagen = ImageDataGenerator(
    rescale=1.0/255.0,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest",
    validation_split=0.2  # 20% danych na walidację
)

# Ścieżka do folderu z danymi
data_dir = r"C:\Users\Kasia\workspace\lab_6\dataset_dogs_vs_cats"


train_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='training'
)

validation_generator = train_datagen.flow_from_directory(
    data_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

history = model.fit(
    train_generator,
    epochs=5,
    validation_data=validation_generator,
    steps_per_epoch=len(train_generator),
    validation_steps=len(validation_generator),
    verbose=1
)

# d) Ocena modelu i porównanie wyników, wyświetlenie wykresów strat i dokładności
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Strata treningowa')
plt.plot(history.history['val_loss'], label='Strata walidacyjna')
plt.title('Strata')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Dokładność treningowa')
plt.plot(history.history['val_accuracy'], label='Dokładność walidacyjna')
plt.title('Dokładność')
plt.legend()

plt.tight_layout()
plt.show()

model.save('fine_tuned_dogs_vs_cats_model.h5')

# Testowanie modelu na nowych obrazach (opcjonalne)
def predict_image(image_path):
    from tensorflow.keras.preprocessing.image import load_img, img_to_array

    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img) / 255.0
    img_array = img_array.reshape((1, 224, 224, 3))

    prediction = model.predict(img_array)
    class_label = 'Dog' if prediction > 0.5 else 'Cat'
    print(f"Predykcja: {class_label}, Prawdopodobieństwo: {prediction[0][0]:.2f}")

predict_image("path_to_test_image.jpg")
