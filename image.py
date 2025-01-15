import cv2 as cv
import os
import mediapipe as mp

output_dir = os.path.join('.','output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
#read image
image_path = os.path.join('.','face_anonymizer', 'sample.jpg')
image = cv.imread(image_path)

H, W, _ = image.shape
#detect face
mp_face_detection = mp.solutions.face_detection
with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
    results = face_detection.process(cv.cvtColor(image, cv.COLOR_BGR2RGB))

    if results.detections is not None:

        for detection in results.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box
            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height    
            
            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)
            #img = cv.rectangle(image, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)

            #blur faces
            image[y1:y1+h, x1:x1+w,:]= cv.blur(image[y1:y1+h, x1:x1+w,:], (50, 50))

    #save image
    cv.imwrite(os.path.join(output_dir, 'output.jpg'), image)