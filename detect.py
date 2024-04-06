from ultralytics import YOLO
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise ValueError(f"{len(sys.argv) - 1} args passed need at least 2")

    model = YOLO('best.pt')
    results = model(sys.argv[1:], stream=True)

    for result in results:
        name = f"inference-{result.path}"

        boxes = result.boxes
        masks = result.masks
        keypoints = result.keypoints
        probs = result.probs
        result.save(filename=name)
