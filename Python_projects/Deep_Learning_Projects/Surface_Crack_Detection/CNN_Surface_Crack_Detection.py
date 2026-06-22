########################################################
# Required Python Packages
########################################################

# Import operating system related functions
import os

# Import utility to copy and manage files
import shutil

# Import random module for dataset shuffling
import random

# Import NumPy for numerical operations
import numpy as np

# Import Matplotlib for data visualization
import matplotlib.pyplot as plt

# Import TensorFlow framework
import tensorflow as tf

# Import Sequential model and model loading functionality
from tensorflow.keras.models import Sequential, load_model

# Import CNN layers required for model creation
from tensorflow.keras.layers import (
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout,
    BatchNormalization
)

# Import image preprocessing utilities
from tensorflow.keras.preprocessing.image import (
    ImageDataGenerator,
    load_img,
    img_to_array
)

# Import callbacks used during model training
from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint,
    ReduceLROnPlateau
)

# Import evaluation metrics for classification model
from sklearn.metrics import (
    confusion_matrix,
    classification_report
)

# ------------------------------------------------------------
# Step 1: Basic Configuration
# ------------------------------------------------------------

# Display application title
print("=" * 70)
print("        Industrial Surface Crack Detection using CNN")
print("=" * 70)

########################################################
# Define Original Dataset Path
########################################################

# Specify the root directory containing the original dataset
ORIGINAL_DATASET = "CrackDataset"

# Define path for images containing cracks
POSITIVE_FOLDER = os.path.join(ORIGINAL_DATASET, "Positive")

# Define path for images containing no cracks
NEGATIVE_FOLDER = os.path.join(ORIGINAL_DATASET, "Negative")

########################################################
# Define Processed Dataset Path
########################################################

# Specify directory where processed dataset will be stored
PROCESSED_DATASET = "Processed_CrackDataset"

########################################################
# Define Hyperparameters
########################################################

# Define image size for CNN input
IMAGE_SIZE = 128

# Define batch size for model training
BATCH_SIZE = 32

# Define total number of training epochs
EPOCHS = 15

# Define random seed for reproducibility
RANDOM_SEED = 42

########################################################
# Initialize Random Seeds
########################################################

# Set random seed for Python random module
random.seed(RANDOM_SEED)

# Set random seed for NumPy operations
np.random.seed(RANDOM_SEED)

# Set random seed for TensorFlow operations
tf.random.set_seed(RANDOM_SEED)


# ------------------------------------------------------------
# Step 2: Check Original Dataset
# ------------------------------------------------------------

########################################################
# Function name : check_folder
# Description   : Check whether the specified folder exists
# Input         : Path of the folder
# Output        : Display error message and terminate program if
#                 folder is not available
# Author        : Aryan Pandharinath Dhumal
# Date          : 21/05/26
########################################################

def check_folder(folder_path):
    # Verify whether the folder exists
    if not os.path.exists(folder_path):
        print("ERROR: Folder not found:", folder_path)
        exit()


# Verify Crack and No Crack dataset folders
check_folder(POSITIVE_FOLDER)
check_folder(NEGATIVE_FOLDER)


########################################################
# Function name : get_image_files
# Description   : Retrieve all valid image files from the
#                 specified folder
# Input         : Folder path
# Output        : List containing image file names
# Author        : Aryan Pandharinath Dhumal
# Date          : 21/05/26
########################################################

def get_image_files(folder):

    # Supported image extensions
    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".webp")

    # Return only valid image files
    return [
        file for file in os.listdir(folder)
        if file.lower().endswith(valid_extensions)
    ]


########################################################
# Read Crack and No Crack Images
########################################################

# Retrieve all positive (Crack) images
positive_images = get_image_files(POSITIVE_FOLDER)

# Retrieve all negative (No Crack) images
negative_images = get_image_files(NEGATIVE_FOLDER)


########################################################
# Display Dataset Information
########################################################

# Print total number of Crack images
print("Original Positive Images:", len(positive_images))

# Print total number of No Crack images
print("Original Negative Images:", len(negative_images))


########################################################
# Validate Dataset
########################################################

# Stop execution if any class folder contains no images
if len(positive_images) == 0 or len(negative_images) == 0:
    print("ERROR: Positive or Negative folder contains no images.")
    exit()

# ------------------------------------------------------------
# Step 3: Create Industrial Folder Structure
# ------------------------------------------------------------

# List of directories required for training,
# validation and testing datasets
folders = [
    "train/Crack",
    "train/NoCrack",
    "validation/Crack",
    "validation/NoCrack",
    "test/Crack",
    "test/NoCrack"
]

########################################################
# Create Required Directory Structure
########################################################

# Create all required folders inside the processed
# dataset directory if they do not already exist
for folder in folders:
    os.makedirs(
        os.path.join(PROCESSED_DATASET, folder),
        exist_ok=True
    )

# ------------------------------------------------------------
# Step 4: Split Data into Train, Validation, Test
# ------------------------------------------------------------

########################################################
# Function name : split_and_copy_images
# Description   : Split the dataset into Training,
#                 Validation and Testing sets and copy
#                 the images into their respective folders
# Input         : Source folder, list of image files,
#                 class name
# Output        : Copies images into processed dataset folders
#                 and displays split information
# Author        : Aryan Pandharinath Dhumal
# Date          : 21/05/26
########################################################

def split_and_copy_images(source_folder, image_files, class_name):

    # Randomly shuffle image list to avoid bias
    random.shuffle(image_files)

    # Calculate total number of images
    total_images = len(image_files)

    # Calculate number of training images (70%)
    train_count = int(total_images * 0.70)

    # Calculate number of validation images (15%)
    validation_count = int(total_images * 0.15)

    # Select images for training dataset
    train_files = image_files[:train_count]

    # Select images for validation dataset
    validation_files = image_files[train_count:train_count + validation_count]

    # Remaining images are used for testing
    test_files = image_files[train_count + validation_count:]

    # Store split information in dictionary
    split_data = {
        "train": train_files,
        "validation": validation_files,
        "test": test_files
    }

    # Copy images to corresponding destination folders
    for split_name, files in split_data.items():

        # Create destination folder path
        destination_folder = os.path.join(
            PROCESSED_DATASET,
            split_name,
            class_name
        )

        # Copy each image to destination folder
        for file in files:

            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)

            # Copy image only if it does not already exist
            if not os.path.exists(destination_path):
                shutil.copy(source_path, destination_path)

    # Display dataset split information
    print(f"{class_name} Images Split:")
    print("Training Images   :", len(train_files))
    print("Validation Images :", len(validation_files))
    print("Testing Images    :", len(test_files))
    print("-" * 70)


########################################################
# Split Crack Images
########################################################

# Split positive images into Train, Validation and Test
split_and_copy_images(
    POSITIVE_FOLDER,
    positive_images,
    "Crack"
)

########################################################
# Split No Crack Images
########################################################

# Split negative images into Train, Validation and Test
split_and_copy_images(
    NEGATIVE_FOLDER,
    negative_images,
    "NoCrack"
)


# ------------------------------------------------------------
# Step 5: Define Train, Validation and Test Paths
# ------------------------------------------------------------

# Define the path of the training dataset directory
train_dir = os.path.join(PROCESSED_DATASET, "train")

# Define the path of the validation dataset directory
validation_dir = os.path.join(PROCESSED_DATASET, "validation")

# Define the path of the testing dataset directory
test_dir = os.path.join(PROCESSED_DATASET, "test")


# ------------------------------------------------------------
# Step 6: Image Preprocessing and Augmentation
# ------------------------------------------------------------

# Create ImageDataGenerator for training dataset
# with data augmentation techniques
train_datagen = ImageDataGenerator(

    # Normalize pixel values between 0 and 1
    rescale=1.0 / 255,

    # Randomly rotate images up to 15 degrees
    rotation_range=15,

    # Randomly zoom images up to 20%
    zoom_range=0.2,

    # Randomly shift images horizontally
    width_shift_range=0.1,

    # Randomly shift images vertically
    height_shift_range=0.1,

    # Randomly flip images horizontally
    horizontal_flip=True
)

########################################################
# Validation Data Preprocessing
########################################################

# Create ImageDataGenerator for validation dataset
# with only normalization
validation_datagen = ImageDataGenerator(

    # Normalize pixel values between 0 and 1
    rescale=1.0 / 255
)

########################################################
# Test Data Preprocessing
########################################################

# Create ImageDataGenerator for testing dataset
# with only normalization
test_datagen = ImageDataGenerator(

    # Normalize pixel values between 0 and 1
    rescale=1.0 / 255
)

########################################################
# Load Training Dataset
########################################################

# Load images from training directory
train_data = train_datagen.flow_from_directory(

    train_dir,

    # Resize images to predefined dimensions
    target_size=(IMAGE_SIZE, IMAGE_SIZE),

    # Number of images processed in one batch
    batch_size=BATCH_SIZE,

    # Binary classification mode
    class_mode="binary"
)

########################################################
# Load Validation Dataset
########################################################

# Load images from validation directory
validation_data = validation_datagen.flow_from_directory(

    validation_dir,

    # Resize images to predefined dimensions
    target_size=(IMAGE_SIZE, IMAGE_SIZE),

    # Number of images processed in one batch
    batch_size=BATCH_SIZE,

    # Binary classification mode
    class_mode="binary"
)

########################################################
# Load Testing Dataset
########################################################

# Load images from testing directory
test_data = test_datagen.flow_from_directory(

    test_dir,

    # Resize images to predefined dimensions
    target_size=(IMAGE_SIZE, IMAGE_SIZE),

    # Number of images processed in one batch
    batch_size=BATCH_SIZE,

    # Binary classification mode
    class_mode="binary",

    # Disable shuffling to preserve original order
    shuffle=False
)

########################################################
# Display Class Labels
########################################################

# Print mapping of class names to numerical labels
print("Class Indices:", train_data.class_indices)


# ------------------------------------------------------------
# Step 7: Display Sample Images
# ------------------------------------------------------------

# Retrieve one batch of images and corresponding labels
# from the training dataset
sample_images, sample_labels = next(train_data)

# Create a figure for displaying sample images
plt.figure(figsize=(10, 6))

########################################################
# Display First Six Sample Images
########################################################

# Iterate through the first six images
for i in range(6):

    # Create subplot in a 2x3 grid
    plt.subplot(2, 3, i + 1)

    # Display the current image
    plt.imshow(sample_images[i])

    # Check whether the image belongs to Crack class
    if sample_labels[i] == train_data.class_indices["Crack"]:

        # Set title as Crack
        plt.title("Crack")

    else:

        # Set title as No Crack
        plt.title("No Crack")

    # Hide axis for better visualization
    plt.axis("off")

########################################################
# Display Complete Figure
########################################################

# Set overall title for the displayed images
plt.suptitle("Marvellous CNN Sample Training Images")

# Show the sample training images
plt.show()

# ------------------------------------------------------------
# Step 8: Build Industrial CNN Model
# ------------------------------------------------------------

# Create a Sequential Convolutional Neural Network model
model = Sequential()

########################################################
# First Convolutional Block
########################################################

# Add first convolutional layer with 32 filters
model.add(
    Conv2D(
        32,
        (3, 3),
        activation="relu",
        input_shape=(IMAGE_SIZE, IMAGE_SIZE, 3)
    )
)

# Normalize feature maps for stable learning
model.add(BatchNormalization())

# Reduce spatial dimensions using Max Pooling
model.add(MaxPooling2D(pool_size=(2, 2)))

########################################################
# Second Convolutional Block
########################################################

# Add second convolutional layer with 64 filters
model.add(Conv2D(64, (3, 3), activation="relu"))

# Apply Batch Normalization
model.add(BatchNormalization())

# Perform Max Pooling operation
model.add(MaxPooling2D(pool_size=(2, 2)))

########################################################
# Third Convolutional Block
########################################################

# Add third convolutional layer with 128 filters
model.add(Conv2D(128, (3, 3), activation="relu"))

# Apply Batch Normalization
model.add(BatchNormalization())

# Perform Max Pooling operation
model.add(MaxPooling2D(pool_size=(2, 2)))

########################################################
# Fourth Convolutional Block
########################################################

# Add fourth convolutional layer with 256 filters
model.add(Conv2D(256, (3, 3), activation="relu"))

# Apply Batch Normalization
model.add(BatchNormalization())

# Perform Max Pooling operation
model.add(MaxPooling2D(pool_size=(2, 2)))

########################################################
# Flatten Feature Maps
########################################################

# Convert multi-dimensional feature maps into
# one-dimensional feature vector
model.add(Flatten())

########################################################
# Fully Connected Dense Layers
########################################################

# Add first dense layer with 256 neurons
model.add(Dense(256, activation="relu"))

# Apply Dropout to reduce overfitting
model.add(Dropout(0.5))

# Add second dense layer with 128 neurons
model.add(Dense(128, activation="relu"))

# Apply Dropout to improve generalization
model.add(Dropout(0.3))

########################################################
# Output Layer
########################################################

# Add output layer for binary classification
# using Sigmoid activation function
model.add(Dense(1, activation="sigmoid"))


# ------------------------------------------------------------
# Step 9: Compile Model
# ------------------------------------------------------------

# Configure the CNN model by specifying the
# optimizer, loss function and evaluation metric
model.compile(

    # Use Adam optimizer for weight optimization
    optimizer="adam",

    # Use Binary Cross Entropy loss function for
    # binary classification problem
    loss="binary_crossentropy",

    # Use Accuracy as the performance evaluation metric
    metrics=["accuracy"]
)

# Print the complete architecture of the CNN model
# including layers, output shapes and parameters
model.summary()


# ------------------------------------------------------------
# Step 10: Industrial Training Callbacks
# ------------------------------------------------------------

# Create EarlyStopping callback to stop training
# if validation loss does not improve
early_stop = EarlyStopping(

    # Monitor validation loss during training
    monitor="val_loss",

    # Wait for 4 epochs before stopping
    patience=4,

    # Restore the best model weights after stopping
    restore_best_weights=True
)

########################################################
# Configure Model Checkpoint
########################################################

# Save the best performing model during training
checkpoint = ModelCheckpoint(

    # File name for storing the best model
    "Best_Crack_Detection_Model.keras",

    # Monitor validation accuracy
    monitor="val_accuracy",

    # Save only the best model
    save_best_only=True,

    # Maximize validation accuracy
    mode="max",

    # Display messages during saving
    verbose=1
)

########################################################
# Configure Learning Rate Scheduler
########################################################

# Reduce learning rate automatically when
# validation loss stops improving
reduce_lr = ReduceLROnPlateau(

    # Monitor validation loss
    monitor="val_loss",

    # Reduce learning rate by multiplying with factor
    factor=0.2,

    # Wait for 2 epochs before reducing learning rate
    patience=2,

    # Set minimum learning rate value
    min_lr=0.00001,

    # Display update messages
    verbose=1
)

# ------------------------------------------------------------
# Step 11: Train CNN Model
# ------------------------------------------------------------

# Train the Convolutional Neural Network using the
# training dataset along with validation dataset
history = model.fit(

    # Training dataset
    train_data,

    # Specify total number of training epochs
    epochs=EPOCHS,

    # Validation dataset used to evaluate model
    # performance after each epoch
    validation_data=validation_data,

    # Apply training callbacks such as EarlyStopping,
    # ModelCheckpoint and ReduceLROnPlateau
    callbacks=[
        early_stop,
        checkpoint,
        reduce_lr
    ]
)


# ------------------------------------------------------------
# Step 12: Plot Accuracy Graph
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("Marvellous CNN Training vs Validation Accuracy")
plt.legend()
plt.show()


# ------------------------------------------------------------
# Step 13: Plot Loss Graph
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("Marvellous CNN Training vs Validation Loss")
plt.legend()
plt.show()


# ------------------------------------------------------------
# Step 14: Evaluate Model on Test Dataset
# ------------------------------------------------------------

print("=" * 70)
print("Testing Model on Unseen Test Data")
print("=" * 70)

test_loss, test_accuracy = model.evaluate(test_data)

print("Test Loss     :", test_loss)
print("Test Accuracy :", test_accuracy * 100)


# ------------------------------------------------------------
# Step 15: Confusion Matrix and Classification Report
# ------------------------------------------------------------

predictions = model.predict(test_data)
predicted_classes = (predictions > 0.5).astype(int).reshape(-1)

actual_classes = test_data.classes

print("Confusion Matrix:")
print(confusion_matrix(actual_classes, predicted_classes))

print("Classification Report:")
print(classification_report(
    actual_classes,
    predicted_classes,
    target_names=list(test_data.class_indices.keys())
))


# ------------------------------------------------------------
# Step 16: Save Final Model
# ------------------------------------------------------------

model.save("Final_Marvellous_Crack_Detection_Model.keras")

print("Final model saved successfully.")


# ------------------------------------------------------------
# Step 17: Single Image Prediction Function
# ------------------------------------------------------------

########################################################
# Function name     : predict_single_image
# Description       : Predict whether the given input image
#                     contains a crack or not using the
#                     trained CNN model
# Input             : Path of the input image
# Output            : Displays prediction result for the image
# Author            : Aryan Pandharinath Dhumal
# Date              : 21/05/26
########################################################

def predict_single_image(image_path):

    # Check whether the specified image exists
    if not os.path.exists(image_path):
        print("ERROR: Image not found:", image_path)
        return

    ########################################################
    # Load and Preprocess Input Image
    ########################################################

    # Load image and resize it to the required dimensions
    img = load_img(image_path, target_size=(IMAGE_SIZE, IMAGE_SIZE))

    # Convert image into NumPy array
    img_array = img_to_array(img)

    # Normalize pixel values between 0 and 1
    img_array = img_array / 255.0

    # Expand dimensions to create batch of one image
    img_array = np.expand_dims(img_array, axis=0)

    ########################################################
    # Predict Image Class
    ########################################################

    # Predict the class probability using trained model
    prediction = model.predict(img_array)

    # Extract prediction score
    prediction_value = prediction[0][0]

    ########################################################
    # Retrieve Crack Class Index
    ########################################################

    # Obtain numerical index assigned to Crack class
    crack_index = train_data.class_indices["Crack"]

    ########################################################
    # Determine Final Prediction Result
    ########################################################

    # Generate prediction result based on class index
    if crack_index == 1:
        final_result = (
            "Crack Detected"
            if prediction_value > 0.5
            else "No Crack"
        )
    else:
        final_result = (
            "No Crack"
            if prediction_value > 0.5
            else "Crack Detected"
        )

    print("=" * 70)
    print("Single Image Prediction")                     
    print("=" * 70)
    print("Image Path       :", image_path)
    print("Prediction Value :", prediction_value)
    print("Final Result     :", final_result)

    plt.imshow(load_img(image_path))
    plt.title(final_result)
    plt.axis("off")
    plt.show()


# ------------------------------------------------------------
# Step 18: Test Single Image
# ------------------------------------------------------------

# Change image name according to your actual image file
sample_test_image = os.path.join(PROCESSED_DATASET, "test", "Crack")

test_images = get_image_files(sample_test_image)

if len(test_images) > 0:
    predict_single_image(os.path.join(sample_test_image, test_images[0]))
else:
    print("No test image found for single image prediction.")