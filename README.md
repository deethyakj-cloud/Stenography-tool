INTERN ID : CITS8522
# Steganography Tool

## 📌 Project Overview

The Steganography Tool is a Python-based cybersecurity application that demonstrates how text messages can be hidden inside digital images.

The tool uses image pixel data and Least Significant Bit (LSB) steganography to hide a text message inside a PNG image. The hidden message can later be extracted from the generated stego image.

This project provides a simple educational demonstration of image-based data hiding.

## 🎯 Objectives

- Hide text messages inside images
- Extract hidden messages from images
- Demonstrate LSB-based steganography
- Work with image pixel data using Python
- Provide a simple command-line interface
- Demonstrate basic information-hiding techniques

## 🚀 Features

- Hide text inside PNG images
- Extract hidden text from PNG images
- LSB-based steganography
- Automatic output image generation
- Simple command-line interface
- Message validation
- Uses Pillow for image processing

## 🛠️ Technologies Used

- Python
- Pillow
- LSB (Least Significant Bit) Steganography
- Image Processing

## 📁 Project Structure

```text
Steganography-Tool/
│
├── images/
│   └── test.png
│
├── output/
│   └── stego_image.png
│
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── venv/
```

> Note: The `venv/` folder is used only for local development and should not be uploaded to GitHub.

## 📄 File Description

| File/Folder | Description |
|---|---|
| `main.py` | Main steganography application |
| `images/` | Contains the original image used for testing |
| `output/` | Stores the generated stego image |
| `stego_image.png` | Image containing the hidden message |
| `.gitignore` | Prevents unnecessary files from being uploaded |
| `requirements.txt` | Contains the Pillow dependency |
| `README.md` | Project documentation |

## ⚙️ Installation

### 1. Install Python

Make sure Python is installed.

Check the Python version:

```bash
python --version
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

The project requires:

```text
Pillow
```

## ▶️ How to Run

Run the program using:

```bash
python main.py
```

The program displays:

```text
============================================================
             STEGANOGRAPHY TOOL
============================================================

1. Hide message
2. Extract message
3. Exit

Enter your choice:
```

## 🔐 Hide a Message

Select:

```text
1
```

The program asks:

```text
Enter the message to hide:
```

Enter a message such as:

```text
This is a cybersecurity steganography test.
```

The program creates:

```text
output/stego_image.png
```

The generated image contains the hidden message.

## 🔎 Extract a Message

Select:

```text
2
```

The program reads:

```text
output/stego_image.png
```

and extracts the hidden message.

Example output:

```text
============================================================
          EXTRACTED MESSAGE
============================================================

Hidden message:
This is a cybersecurity steganography test.
```

## 🧠 How LSB Steganography Works

The tool uses the Least Significant Bit (LSB) technique.

Digital images contain pixels with color values. Each pixel contains RGB channel values.

For example:

```text
Red   Green   Blue
120    200     75
```

The least significant bit of these values can be modified to store binary message data.

A simplified example:

```text
Original pixel:
120 → binary value

Modified pixel:
121 → binary value
```

The visual difference is extremely small, while the changed bits can represent hidden message data.

The process is:

```text
Text Message
      ↓
Convert to Binary
      ↓
Store bits in image pixels
      ↓
Generate Stego Image
      ↓
Read pixel bits
      ↓
Convert Binary to Text
      ↓
Extract Message
```

## 🧪 Security Testing

The project was tested using the following scenarios.

### Test 1 — Hide Message

Input:

```text
This is a cybersecurity steganography test.
```

Expected result:

```text
Message successfully hidden!
Output image: output\stego_image.png
```

Result:

```text
PASS ✅
```

### Test 2 — Extract Message

The generated `stego_image.png` was scanned using the extraction option.

Expected result:

```text
Hidden message:
This is a cybersecurity steganography test.
```

Result:

```text
PASS ✅
```

### Test 3 — Output Image

The program successfully generated:

```text
output/stego_image.png
```

Result:

```text
PASS ✅
```

## 🛡️ Security Applications

Steganography can be studied in cybersecurity for:

- Information hiding
- Digital forensics
- Security research
- Covert communication analysis
- Malware investigation
- Detection of hidden information

This project is an educational implementation intended to demonstrate the basic principles of image steganography.

## 📚 Learning Outcomes

This project demonstrates:

- Python programming
- Image processing
- Binary data conversion
- Pixel manipulation
- LSB steganography
- File handling
- Command-line application development
- Basic cybersecurity concepts

## 📊 Project Status

**Status: Completed ✅**

The project successfully demonstrates:

- Message hiding
- Message extraction
- LSB-based image steganography
- PNG image processing
- Output image generation

## 🔗 GitHub Repository

Add your GitHub repository link here after uploading the project.

## 👩‍💻 Project Category

**Cybersecurity / Steganography**

**Programming Language:** Python
