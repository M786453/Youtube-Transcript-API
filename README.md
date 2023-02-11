
## Youtube Transcript API

### Introduction:
Youtube Transcript API will help you **retrieve** an **English transcript** of a youtube video by sending a **GET** request . It's a **Python Flask** API.

### Usage:
In order to retrieve transcript, you need to send a **GET** request alongwith **id** of youtube video as query parameter.

##### API URL: 

`https://yttranscript.vercel.app/?video_id=`

##### Example

	import  requests
	#https://youtu.be/o8NPllzkFhE
	#In the above URL, video id is => o8NPllzkFhE
	video_id = "o8NPllzkFhE"
	URL = "https://yttranscript.vercel.app/?video_id=" + video_id
	response = requests.get(URL)
	print(response.text)
