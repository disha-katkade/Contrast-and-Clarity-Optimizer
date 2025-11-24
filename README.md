
# **Contrast and Clarity Optimizer👁️👁️ **

Contrast and Clarity Optimizer is a beginner-friendly computer vision project that enhances real-time webcam video using fundamental OpenCV techniques. The system improves visibility by applying grayscale conversion, histogram equalization, and Canny edge detection. It also allows users to save enhanced frames as images and automatically records the entire enhanced video session.

---

**Features💡**

1. Real-time webcam video processing
2. Grayscale conversion
3. Contrast enhancement using histogram equalization
4. Canny edge detection
5. Enhanced frame generation using weighted overlay
6. Option to save individual enhanced frames
7. Automatic saving of enhanced output video

---

**Concepts Used📚**

This project demonstrates the application of basic computer vision operations:
- Image preprocessing
- Color space conversion (BGR to Grayscale)
- Histogram equalization for contrast enhancement
- Canny edge detection
- Frame overlay using weighted addition
- Video capture and video writing using OpenCV

---

**Technology Stack💻**

| Python 3.x  | OpenCV | NumPy |Laptop webcam |
| :------- | :------: | :-------: | :--------:|

---

**Project Structure📂**

- Contrast-and-clarity-optimizer/main/
  - `src/`
    - `algorithm.py`
  - `Enhanced-Output/`
    - ` saved_frames/ `
    - ` saved_recordings/ `
  - `README.md`
  - `requirements.txt`
  - `License`

---

**How to Run▶️**

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Start the application:
```
python src/algorithm.py
```
3. Controls:
Press 's' to save the current enhanced frame as an image
Press 'q' to quit the program

The enhanced video is automatically saved as a file.

---

**Testing Recommendations**

The project works well with objects that have visible structure and contrast variations, such as:
- Printed newspaper or textbook pages
- Labels on bottles or packages
- QR codes
- Drawings or shapes on paper
- Everyday objects with clear edges

---

**Applications**

This project can serve as a foundation for:
- Visibility enhancement tools
- Educational demonstrations of image preprocessing
- Preprocessing modules for larger computer vision systems
- Low-light or low-contrast video enhancement
- Assistive visual aids


---

License

This project is released under the MIT License.

