
# 🥬 Beetroot Detection with YOLOv7

This project uses the YOLOv7 object detection framework to train and run a model for detecting beetroots in images and webcam streams.

---

## 🚀 Getting Started

### 1. Clone the Repository (with Git LFS for model files)

This repository uses **Git Large File Storage (Git LFS)** to store large files like pretrained `.pt` weights.

> 🔧 **Install Git LFS (one-time setup):**

#### Windows:
Download from: https://git-lfs.github.com/

Or using Chocolatey:
```
choco install git-lfs
```

#### macOS:
```
brew install git-lfs
```

#### Linux (Ubuntu/Debian):
```
sudo apt install git-lfs
```

#### Then run this (once per system):
```
git lfs install
```

> ✅ Now clone the repo **with LFS support**:
```
git clone https://github.com/yourusername/Beetroot_yolo.git
cd Beetroot_yolo
```

> ❗ **Without Git LFS**, large files like model weights (`.pt`) will not be downloaded correctly.

---

## 🧰 Git LFS for Contributors

If you're contributing and want to **push new large files**, follow these steps:

1. Track the file type (e.g., `.pt`):
   ```
   git lfs track "*.pt"
   ```

2. Stage the `.gitattributes` and your files:
   ```
   git add .gitattributes
   git add path/to/your_model.pt
   ```

3. Commit and push:
   ```
   git commit -m "Add model with Git LFS"
   git push origin main
   ```

---

## 🐍 Set Up the Virtual Environment

Create and activate the virtual environment called `btenv`:

**Windows:**
```
python -m venv btenv
btenv\Scripts\activate
```

**macOS/Linux:**
```
python -m venv btenv
source btenv/bin/activate
```

*Your prompt should now show `(btenv)` at the start.*

---

## 📦 Install Dependencies

Install all required Python packages using the `requirements.txt` file:

```
pip install -r yolov7/requirements.txt
```

---

## 📁 Prepare Your Dataset

Make sure your dataset is structured as follows:

```
Beetroot/
├── dataset/
│   ├── images/
│   ├── labels/
│   └── data.yaml
```

*Edit `data.yaml` to point to your training and validation images and labels.*

---

## 🏋️ Train the Model

Train the YOLOv7 model for one epoch (adjust as needed):

```
python yolov7/train.py \
--workers 1 \
--device cpu \
--batch-size 1 \
--epochs 1 \
--data dataset/data.yaml \
--img 640 \
--cfg yolov7/cfg/training/yolov7.yaml \
--weights yolov7/yolov7.pt \
--name beetroot_detector \
--hyp yolov7/data/hyp.scratch.p5.yaml
```

*Trained model will be saved in `runs/train/beetroot_detector/weights/`.*

---

## 📷 Run Live Detection

Run detection using your webcam (device index `0`):

```
python yolov7/detect.py \
--weights runs/train/beetroot_detector/weights/best.pt \
--source 0
```

---

## 📂 Project Structure

```
Beetroot/
├── yolov7/               # YOLOv7 code
├── dataset/              # Dataset (images, labels, data.yaml)
├── scripts/              # (Optional) Custom scripts
├── requirements.txt      # Python dependencies
├── .gitattributes        # Git LFS tracking file
└── README.md             # This file
```

---

## 📝 Notes

- **Model Weights:** After training, best model is saved in `runs/train/beetroot_detector/weights/best.pt`.
- **Virtual Environment:** Always activate `btenv` before running commands.
- **Git LFS Reminder:** You must install Git LFS before cloning this repository to get the `.pt` model files.

