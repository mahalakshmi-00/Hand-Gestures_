# Hand Gesture Recognition 🤖✋  

A real-time **Hand Gesture Recognition** system using **OpenCV, MediaPipe, TensorFlow, and NumPy**. This project detects hand landmarks from a live webcam feed and recognizes gestures like **"Open Hand (Palm)"** and **"Pointing Up"**, overlaying corresponding text.

---

## 🔧 Setup Instructions  

### 1️⃣ Install Prerequisites  
Ensure you have **Python** installed. If not, download it from [Python.org](https://www.python.org/).

### 2️⃣ Clone the Repository  
```sh
git clone https://github.com/mahalakshmi-00/Hand-Gestures_.git
cd Hand-Gestures_
```

### 3️⃣ Create and Activate a Virtual Environment  
```sh
python -m venv venv  
```
#### Windows:  
```sh
.\venv\Scripts\activate  
```
#### macOS/Linux:  
```sh
source venv/bin/activate  
```

### 4️⃣ Install Required Dependencies  
```sh
pip install opencv-python mediapipe tensorflow numpy  
```

### 5️⃣ Run the Gesture Recognition Script  
```sh
python finger.py  
```

---

## 🎯 Features  

✅ **Real-time hand tracking** using MediaPipe  
✅ **Live webcam feed processing** using OpenCV  
✅ **Hand Gesture Recognition** for different hand positions  
✅ **Gesture-based text overlay** on video feed  

---

## 🖥️ How It Works  

1. The webcam captures live video.  
2. **MediaPipe** detects hand landmarks.  
3. Gestures are recognized based on hand landmark positions.  
4. Recognized gestures are **displayed as text on the screen**.  

**Currently Supported Gestures:**  
🖐️ **Open Hand (Palm)** → Displays `"Syntax Sarcasm"`  
☝️ **Pointing Up** → Displays `"Join the Workshop"`  

---

## 🛠️ Troubleshooting  

- **Issue: Virtual environment not activating?**  
  ✅ Use **correct activation command** based on your OS (Windows/macOS/Linux).  
- **Issue: Webcam not detected?**  
  ✅ Ensure your camera is connected and accessible.  
- **Issue: Libraries missing?**  
  ✅ Run `pip list` to check installed libraries and reinstall missing ones.  

---

## 🚀 Future Enhancements  

- 🎭 Add **more hand gestures** recognition.  
- 🎨 Implement **custom UI overlay** for better user experience.  
- 🤖 Train a **custom deep learning model** for gesture classification.  
  
---

## 💡 Credits  

Created by **Mahalakshmi-00** 👩‍💻  
Built with ❤️ using **Python, OpenCV, and MediaPipe**  

---

## 📜 License  

This project is licensed under the **MIT License**.  

---

