from django.http import StreamingHttpResponse
import cv2

class StreamRTSP:

    @staticmethod
    def gen(user, password, ip, port):
        cap = cv2.VideoCapture(
            f"rtsp://{user}:{password}@{ip}:{port}/cam/realmonitor?channel=1&subtype=0"
        )
        while True:
            success, frame = cap.read()
            if not success:
                break
            else:
                ret, buffer = cv2.imencode(".jpg", frame)
                frame = buffer.tobytes()
                yield (
                    b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"
                )

    @staticmethod
    def video_feed(user, password, ip, port):
        return StreamingHttpResponse(
            StreamRTSP.gen(user, password, ip, port),
            content_type="multipart/x-mixed-replace; boundary=frame",
        )

