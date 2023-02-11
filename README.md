
## Youtube Transcript API

### Introduction:
Youtube Transcript API will help you **retrieve** an **English transcript** of a youtube video by sending a **GET** request . It's a **Python Flask** API.

### Usage:
In order to retrieve transcript, you need to send a **GET** request alongwith **id** of youtube video as query parameter.

##### API URL: 

	https://yttranscript.vercel.app/?video_id=

##### Example

	import requests
	#https://youtu.be/JKxlsvZXG7c
	#In the above URL, video id is => JKxlsvZXG7c
	video_id = "JKxlsvZXG7c"
	URL = "https://yttranscript.vercel.app/?video_id=" + video_id
	response = requests.get(URL)
	print(response.text)

##### Output

	nginx it's like a gateway that standsbetween the internet and your back-endinfrastructurewhen you visit a web app the first placeyour request will go is to a web serverits job is to look at the requestedresource and determine where to find iton the server then send it backas the response in fact if you open upthe network tab in chrome dev toolsright nowyou can look at the server header on anyresponse and 
	there's a good chance it'llbe nginxit's extremely popular with high trafficsites because it can handle more than 10000 simultaneous connections with itsevent driven architectureit's also commonly used as a reverseproxy where it acts as a traffic lightto distribute the load to multiplebackend servers while also providingsecurityand caching for better performance inmost cases it'll be installed on a linuxserver with the configuration file beingfound in the etcdirectory you customize the behavior ofyour server by defining directivesa directive is just a key value pair orif followed by braces it's known as acontext which itself holds moredirectivesin the global context we might want tospecify things like a usernameand where to save our error logs butmost of your configuration will likelybe done in the http contextnow one of the most important roles ofnginx is to serve out static contentlikeimages and html we can handle that inthe http context where we'll define oneor more serverseach server is distinguished by the portthat it listens to nginx will keep trackof every request to the serverwhich you can write to an access log themost important thing though is to tellthe server where to find the raw fileswhich we do in the location contextnow when a user navigates to our domainit knows where to find the htmlon the file system and we might want toset up a second locationto match any image pattern to the imagesdirectory other common things you mighthandle in your server configinclude ssl certificates rewrites androuting to a proxy server when i replaceroot with proxy passi can point to a completely differentserver 
	on the internet what we'vecreated is a reverse proxy that canhandle cachinganonymity and load balancing this hasbeen nginx in 100 secondshit the like button if you want to seemore short videos like this thanks forwatchingand i will see you in the next one


