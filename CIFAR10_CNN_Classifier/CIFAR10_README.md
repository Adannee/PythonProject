# CIFAR-10 Image Classification with CNNs

A custom Convolutional Neural Network (CNN) built with TensorFlow/Keras to classify 60,000 images across 10 categories. Trained from scratch on 50,000 images and evaluated on a 10,000-image test set.

---

## Results

| Metric | Value |
|--------|-------|
| **Best Validation Accuracy** | **70.91%** (Epoch 18) |
| Final Training Accuracy | 71.93% |
| Final Validation Accuracy | 69.78% |
| Epochs Trained | 20 |
| Training Time (per epoch) | ~10–12 seconds |

> **Note:** A slight overfitting pattern emerges after epoch 14, where training accuracy begins to pull ahead of validation accuracy. Future improvements could include data augmentation or additional regularisation to close this gap.

---

## Dataset

- **CIFAR-10**: 60,000 colour images (32×32 pixels) across 10 classes
- **Train / Test split**: 50,000 / 10,000
- **Source**: Built-in via `tensorflow.keras.datasets`
- **Preprocessing**: Pixel values normalised to [0, 1] range

**Classes:** airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck

---

## Model Architecture

A sequential CNN with two convolutional blocks followed by a dense classifier:

```
Input (32×32×3)
    → Conv2D (32 filters, 3×3, ReLU)       # 896 params
    → MaxPooling2D (2×2)
    → Conv2D (64 filters, 3×3, ReLU)       # 18,496 params
    → MaxPooling2D (2×2)
    → Flatten
    → Dense (64 units, ReLU)               # 147,520 params
    → Dropout (0.5)
    → Dense (10 units, Softmax)            # 650 params

Total trainable parameters: 167,562
```

**Design choices:**
- Two convolutional blocks to capture low- and mid-level features progressively
- MaxPooling for spatial downsampling and translation invariance
- 0.5 Dropout rate to reduce overfitting in the dense layer
- Softmax output for multi-class probability distribution
- Adam optimiser with sparse categorical cross-entropy loss

---

## Training

```python
model.fit(
    X_train, y_train,
    epochs=20,
    validation_data=(X_test, y_test),
    batch_size=64
)
```

**Training progression:**

| Epoch | Train Acc | Val Acc |
|-------|-----------|---------|
| 1     | 63.5%     | 68.5%   |
| 5     | 66.3%     | 68.7%   |
| 10    | 68.9%     | 69.9%   |
| 15    | 70.6%     | 69.7%   |
| 18    | 71.9%     | **70.9%** |
| 20    | 71.9%     | 69.8%   |

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| TensorFlow / Keras | Model building & training |
| NumPy | Array manipulation |
| Matplotlib | Visualisation |

---

## File Structure

```
CIFAR10_CNN_Classifier/
├── cifar10_classifier.py      # Full training script
├── cifar10_cnn_model.h5       # Saved trained model
├── requirements.txt
└── README.md
```

---

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Train the model
python cifar10_classifier.py

# Load saved model for inference
from tensorflow.keras.models import load_model
model = load_model('cifar10_cnn_model.h5')
```

---

## What I Learned

- How convolutional layers progressively learn spatial features from low-level edges to higher-level patterns
- The trade-off between model capacity and overfitting — the current architecture begins to overfit slightly after epoch 14
- How batch normalisation and data augmentation (not yet implemented) could improve generalisation beyond ~70% accuracy

---

## Future Improvements

- [ ] Add data augmentation (random flips, rotations, crops) to improve generalisation
- [ ] Experiment with batch normalisation layers
- [ ] Try a deeper architecture or transfer learning with a pre-trained model (e.g. MobileNetV2)
- [ ] Add confusion matrix to visualise per-class performance
