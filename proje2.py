from roboflow import Roboflow

rf = Roboflow(api_key="------------")#API Key kısmı yazılır.
project = rf.workspace().project("konteyner_veri_seti")
model = project.version("2").model

job_id, signed_url, expire_time = model.predict_video(
    "video2.mp4",
    fps=5,
    prediction_type="batch-video",
)

results = model.poll_until_video_results(job_id)

print(results)