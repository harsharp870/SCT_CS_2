# SCT_CS_2
Image Cipher Tool

Description
This project implements a simple image encryption and decryption tool using pixel manipulation techniques. It transforms the RGB values of each pixel using a secret key to secure the image.

Features
Encrypts an image using a numeric key
Decrypts the image using the same key
Simple GUI interface for user interaction
Supports JPG, PNG, and JPEG formats

Technologies Used
Python
Pillow Library
Tkinter (for GUI)

How to Run
1. Install required library:
   pip install pillow

2. Run the program:
   python main.py

3. Select an image file
4. Enter a key (0–255)
5. Click Encrypt or Decrypt

Output
Encrypted image: cipher_output.png
Decrypted image: original_output.png

Concept
Each pixel’s RGB values are modified using a mathematical transformation with modulo operation to ensure values stay within valid range (0–255).
