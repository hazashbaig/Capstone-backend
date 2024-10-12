import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

# Load your YOLO model
model = YOLO("C:\\Users\\hazas\\VIT\\Capstone\\backend\\NutritionAPI\\src\\main\\java\\com\\capstone\\controller\\best.pt")

def detect_food_items_from_frame(frame, confidence_threshold=0.25):
    """
    Detects food items in the given video frame using the YOLO model and returns a dictionary
    with food item names and their respective quantities.

    Args:
        frame (numpy.ndarray): The frame captured from the camera.
        confidence_threshold (float): The minimum confidence score to consider a detection valid.

    Returns:
        dict: A dictionary with food item names as keys and their counts as values.
    """
    results = model(frame)  # Perform detection on the frame
    detected_items = {}

    for result in results:
        for box in result.boxes:
            if box.conf.item() >= confidence_threshold:  # Apply confidence threshold
                class_id = box.cls.item()
                class_name = result.names[class_id]
                
                if class_name in detected_items:
                    detected_items[class_name] += 1
                else:
                    detected_items[class_name] = 1

    return detected_items, results[0].plot()  # Returning the detected items and the frame with bounding boxes

def run_camera_detection():
    """
    Captures video from the camera and performs real-time food detection.
    """
    cap = cv2.VideoCapture(0)  # Open the default camera (0 = primary camera)
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()  # Capture frame-by-frame
        if not ret:
            print("Failed to grab frame")
            break

        # Detect food items in the frame with confidence threshold of 0.25
        food_items, annotated_frame = detect_food_items_from_frame(frame, confidence_threshold=0.25)

        # Display the annotated frame with bounding boxes
        cv2.imshow('Food Detection', annotated_frame)

        # Print detected food items on the console
        print(f"Detected food items: {food_items}")

        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close any open windows
    cap.release()
    cv2.destroyAllWindows()

# Run the camera detection
run_camera_detection()
