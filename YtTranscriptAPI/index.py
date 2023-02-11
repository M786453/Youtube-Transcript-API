from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from flask_cors import cross_origin, CORS

app = Flask(__name__)

cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

@app.route('/')
def home():
    video_id = request.args.get('video_id')
    return getVideoTranscript(video_id)


def getVideoTranscript(video_id):
    # try:
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, ['en'])
    except:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, ['en-US'])

    video_full_transcript = ""

    for trans in transcript:
        video_full_transcript += trans["text"]



    return video_full_transcript 