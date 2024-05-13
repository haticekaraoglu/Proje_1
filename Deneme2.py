from roboflow import Roboflow
import cv2 

rf = Roboflow(api_key="-----------------------")#Bu kısma API key gelicek.

project = rf.workspace().project("konteyner_veri_seti")
model = project.version("2").model



job_id, signed_url, expire_time = model.predict_video(
    "video1.mp4",
    fps=5,
    prediction_type="batch-video",
)
results = model.poll_until_video_results(job_id)

video=cv2.VideoCapture("video1.mp4")
w=int(video.get(3))
h=int(video.get(4))

size=(w,h)

resultss=cv2.VideoWriter('record.avi',cv2.VideoWriter_fourcc(*'XVID'),24,size)

while True:
    ret,frame=video.read()

    if ret==True:
        resultss.write(frame)
        cv2.imshow('frame',frame )

        kInp=cv2.waitKey(1)
        if kInp==ord('s'):
            break
    else:
        break


video.release()
resultss.release()
cv2.destroyAllWindows()

print(results)