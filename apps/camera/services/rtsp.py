from django.http import JsonResponse, StreamingHttpResponse
import cv2
import os

class StreamRTSP:

    @staticmethod
    def gen(user, password, ip, port):

        # class colors
        COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
        base_path = os.path.dirname(os.path.abspath(__file__))
        coco_names_path = os.path.join(base_path, "coco.names")
        weights_path = os.path.join(base_path, "yolov4-tiny.weights")
        config_path = os.path.join(base_path, "yolov4-tiny.cfg")

        class_names = []
        with open(coco_names_path, "r") as f:
            class_names = [cname.strip() for cname in f.readlines()]

        cap = cv2.VideoCapture(
            f"rtsp://{user}:{password}@{ip}:{port}/cam/realmonitor?channel=1&subtype=0"
        )

        # Load weights and config neural network
        net = cv2.dnn.readNet(weights_path, config_path)

        # Set params neural network
        model = cv2.dnn_DetectionModel(net)
        model.setInputParams(size=(416, 416), scale=1 / 255)

        if not cap.isOpened():
            cap.release()
            raise ValueError("Unable to connect to the RTSP stream. Please check the credentials or the stream URL.")
        
        while True:
            success, frame = cap.read()
            if not success:
                break
            else:
                classes, scores, boxes = model.detect(frame, 0.1, 0.3)

                for (classid, score, box) in zip(classes, scores, boxes):
                    color = COLORS[int(classid) % len(COLORS)]
                    label = "%s : %f" % (class_names[classid], score)
                    cv2.rectangle(frame, box, color, 2)
                    cv2.putText(
                        frame,
                        label,
                        (box[0], box[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        color,
                        2,
                    )

                ret, buffer = cv2.imencode(".jpg", frame)
                frame = buffer.tobytes()
                yield (
                    b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
                )

    @staticmethod
    def video_feed(user, password, ip, port):
        try:
            return StreamingHttpResponse(
                StreamRTSP.gen(user, password, ip, port),
                content_type="multipart/x-mixed-replace; boundary=frame",
            )
        except ValueError as ve:
            return JsonResponse({"error": str(ve)}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
