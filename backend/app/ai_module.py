import cv2

def detect_billboard(image_path):
    """
    Dummy detection: replace with YOLOv8/TensorFlow model for real demo
    """
    img = cv2.imread(image_path)
    height, width, _ = img.shape
    # Dummy rules for demo
    detected = True
    size_violation = width > 1000 or height > 500
    return {
        "detected": detected,
        "size_violation": size_violation,
        "violation_type": "Size" if size_violation else "Placement"
    }
