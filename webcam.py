import cv2 as cv
import os
import mediapipe as mp
import argparse 

def process_img(image, face_detection):

    H, W, _ = image.shape

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
    return image


args = argparse.ArgumentParser()

args.add_argument('--mode',default='webcam')
args.add_argument('--filePath', default=None)
args = args.parse_args()

output_dir = os.path.join('.','output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)



#detect face
mp_face_detection = mp.solutions.face_detection
with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
    
    if args.mode in ['image']:
        #read image
        image_path = args.filePath
        image = cv.imread(image_path)
        
        image = process_img(image, face_detection)
      
        #save image
        cv.imwrite(os.path.join(output_dir, 'output.jpg'), image)
        
    elif args.mode in ['video']:
       
        video = cv.VideoCapture(args.filePath)
        ret, frame = video.read()

        output_video_path = os.path.join(output_dir, 'output.mp4')
        output_video = cv.VideoWriter(output_video_path,
                                   cv.VideoWriter_fourcc(*'mp4v'),
                                     30,
                                       (frame.shape[1], frame.shape[0]))

        while ret:
            frame = process_img(frame, face_detection)
            output_video.write(frame)
            ret, frame = video.read()

        video.release()
        output_video.release()  
    
    elif args.mode in ['webcam']:
        
        video = cv.VideoCapture(0)
        address = "http://192.168.0.101:8080/video"
        video.open(address)
        ret, frame = video.read()

        while ret:
            frame = process_img(frame, face_detection)
            cv.imshow('frame', frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
            ret, frame = video.read()
        video.release()
        cv.destroyAllWindows()