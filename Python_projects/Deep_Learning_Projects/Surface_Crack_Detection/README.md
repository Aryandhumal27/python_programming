# Surface Crack Detection using CNN

This project demonstrates an "end-to-end Deep Learning pipeline" for detecting "surface cracks" using a "Convolutional Neural Network (CNN)".

The project follows industrial best practices by:

* Automating dataset preprocessing and organization
* Splitting data into Training, Validation and Testing sets
* Applying Image Data Augmentation
* Building a Deep CNN architecture with Batch Normalization
* Preventing overfitting using Dropout Layers
* Using Early Stopping and Learning Rate Scheduling
* Saving the best trained model for future predictions
* Performing Single Image Crack Detection

---

# Dependencies

Install the required Python packages before running the project:

```bash
pip install tensorflow numpy matplotlib scikit-learn
```

---

# Dataset Information

## Dataset Structure

```
CrackDataset/
│
├── Positive/
│      image1.jpg
│      image2.jpg
│      ...
│
└── Negative/
       image1.jpg
       image2.jpg
       ...
```

* Positive → Images containing surface cracks
* Negative → Images without cracks

During execution, the project automatically creates:

```
Processed_CrackDataset/

├── train/
│      ├── Crack/
│      └── NoCrack/
│
├── validation/
│      ├── Crack/
│      └── NoCrack/
│
└── test/
       ├── Crack/
       └── NoCrack/
```

---

# Workflow

## Dataset Verification

* Verify Positive and Negative folders exist
* Check image availability
* Read supported image formats

---

## Dataset Preparation

* Shuffle images randomly
* Split dataset into:

  * 70% Training
  * 15% Validation
  * 15% Testing
* Copy images into processed dataset folders

---

## Image Preprocessing

* Resize images to 128 × 128
* Normalize pixel values
* Apply Data Augmentation:

  * Rotation
  * Zoom
  * Width Shift
  * Height Shift
  * Horizontal Flip

---

## CNN Architecture

The implemented CNN consists of:

### Convolution Block 1

* Conv2D (32 Filters)
* Batch Normalization
* MaxPooling2D

### Convolution Block 2

* Conv2D (64 Filters)
* Batch Normalization
* MaxPooling2D

### Convolution Block 3

* Conv2D (128 Filters)
* Batch Normalization
* MaxPooling2D

### Convolution Block 4

* Conv2D (256 Filters)
* Batch Normalization
* MaxPooling2D

### Fully Connected Layers

* Flatten
* Dense (256)
* Dropout (0.5)
* Dense (128)
* Dropout (0.3)
* Dense (1) with Sigmoid Activation

---

# Model Compilation

The CNN model uses:

* Optimizer: Adam
* Loss Function: Binary Crossentropy
* Evaluation Metric: Accuracy

---

# Training Strategy

The project uses industrial callbacks:

## EarlyStopping

* Monitor: Validation Loss
* Patience: 4 epochs

## ModelCheckpoint

* Save only the best performing model

Output file:

```
Best_Crack_Detection_Model.keras
```

## ReduceLROnPlateau

* Automatically reduce learning rate
* Improves convergence

---

# Model Training & Evaluation

The trained model is evaluated using:

* Test Accuracy
* Test Loss
* Confusion Matrix
* Classification Report

---

# Running the Project

Execute the project:

```bash
python CNN_Crack_Detection.py
```

During execution the project will:

* Verify dataset
* Create processed dataset
* Split data
* Perform augmentation
* Build CNN model
* Train model
* Plot Accuracy Graph
* Plot Loss Graph
* Evaluate model
* Save trained model
* Predict sample image

---

# Visualizations

The project generates:

* Sample Training Images
* Training Accuracy Graph
* Validation Accuracy Graph
* Training Loss Graph
* Validation Loss Graph

---

# Model Storage

The trained CNN model is automatically saved as:

```
Final_Marvellous_Crack_Detection_Model.keras
```

The best validation model is stored as:

```
Best_Crack_Detection_Model.keras
```

These models can be loaded later without retraining.

---

# Single Image Prediction

The project supports prediction on an individual image.

Example:

```python
sample_test_image = os.path.join(
    PROCESSED_CrackDataset,
    "test",
    "Crack"
)

predict_single_image(image_path)
```

Possible outputs:

```
Crack Detected
```

or

```
No Crack
```

---

# Expected Output

```
Original Positive Images : xxxx

Original Negative Images : xxxx

Found xxxx images belonging to 2 classes.

Training Started...

Epoch 1/15
...

Testing Model on Unseen Test Data

Test Loss : 0.0xxx

Test Accuracy : xx.xx %

Confusion Matrix

Classification Report

Final model saved successfully.

Single Image Prediction

Final Result : Crack Detected
```

---

# Future Scope

* Deploy using Flask or FastAPI
* Real-time webcam crack detection
* Mobile application integration
* Transfer Learning using ResNet50 or EfficientNet
* Industrial quality inspection automation

---

# Author

Aryan Pandharinath Dhumal
Date: 21/05/26

