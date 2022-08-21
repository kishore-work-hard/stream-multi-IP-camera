import cv2
import concurrent.futures

RTSP_URL = "rtsp://wowzaec2demo.streamlock.net/vod/mp4:BigBuckBunny_115k.mp4"
RTSP_List = [{'url': RTSP_URL,'img_count': '1'},{'url': RTSP_URL,'img_count': '2'},{'url': RTSP_URL,'img_count': '3'}]

def url_to_video(url):
    link = url.get('url')
    img_no = url.get('img_count')
    video = cv2.VideoCapture(link)
    while True:
        _, frame = video.read()
        cv2.imshow(img_no, frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(url_to_video, RTSP_List)
