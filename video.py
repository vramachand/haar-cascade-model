import cv2
import os

# Configuration
MODEL_PATH = "cascade/cascade.xml"  # Path to your cascade model
ANNOTATION_MODE = False  # Set to True to draw ground truth (requires active labels)

# Load classifier
stop_cascade = cv2.CascadeClassifier(MODEL_PATH)
if stop_cascade.empty():
    print("Error: Couldn't load model")
    exit()

# Initialize webcam
cap = cv2.VideoCapture(0)  # 0 = default camera
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

# For annotation mode (if needed)
if ANNOTATION_MODE:
    LABEL_DIR = "data/labels"
    current_label = None

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame")
        break

    # Detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detections = stop_cascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw detections (green)
    for (x, y, w, h) in detections:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Optional: Draw ground truth if in annotation mode
    if ANNOTATION_MODE:
        label_path = os.path.join(LABEL_DIR, "webcam_live.txt")
        if os.path.exists(label_path):
            with open(label_path) as f:
                for line in f:
                    if line.startswith("stop_sign"):
                        x1, y1, x2, y2 = map(int, line.strip().split()[1:5])
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Display
    cv2.imshow("Stop Sign Detection (Press Q to quit)", frame)

    # Key controls
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()