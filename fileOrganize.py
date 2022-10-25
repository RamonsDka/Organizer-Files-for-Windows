from importlib.abc import ExecutionLoader
import os 
import shutil
import pywintypes
#from win10toast import ToastNotifier
from time import sleep

# you can change folder here
folder = os.getcwd()				# Este commando es la ubicacion actual del archivo donde se ejecutara el script

# You can add more file formats here
image_formats = ["jpeg","jpg","png","webp","htm","jpg_large","svg","gif","eml","tiff","tif","bmp","svg","nef","crw"]
audio_formats = ["mp3","wav","wma","flac","midi","ogg","m3u"]
video_formats = ["mp4","avi","webm","wmp","divx","mov","mkv","wmv","wpl","flv"]
docs_formats  = ["ait","docx","doc","pdf","xlsx","pptx","xls","txt","pptm","exc","dochtlm","diz","dic","log","rtf","wtx","pot","pps","ppt","dot","svs","xlshtml","docm","csv"]
progs_formats = ["exe","ps1","com","ttf","otf","ini"]
zip_formats   = ["zip","rar","rar5","7z","ace","jar"]
crel_formats  = ["cdr"]
diseñ_formats = ["psd","ai","indb","indd","indt"]
flexi_formats = ["fs","eps"]

def init():				
	if not os.path.isdir(os.path.join(folder,"1.-images")):			# 1, IMAGINES
		os.mkdir(os.path.join(folder,"1.-images"))
	if not os.path.isdir(os.path.join(folder,"2.-corel")):			# 2, COREL
		os.mkdir(os.path.join(folder,"2.-corel"))
	if not os.path.isdir(os.path.join(folder,"3.-compromises")):	# 3, COMPROMISES
		os.mkdir(os.path.join(folder,"3.-compromises"))
	if not os.path.isdir(os.path.join(folder,"4.-docs")):			# 4, DOCUMENTS
		os.mkdir(os.path.join(folder,"4.-docs"))
	if not os.path.isdir(os.path.join(folder,"5.-design")):			# 5, DESIGN
		os.mkdir(os.path.join(folder,"5.-design"))
	if not os.path.isdir(os.path.join(folder,"6.-flexi")):			# 6, FLEXI
		os.mkdir(os.path.join(folder,"6.-flexi"))
	if not os.path.isdir(os.path.join(folder,"7.-programs")):		# 7, PROGRAMS
		os.mkdir(os.path.join(folder,"7.-programs"))
	if not os.path.isdir(os.path.join(folder,"8.-audio")):			# 8, AUDIOS
		os.mkdir(os.path.join(folder,"8.-audio"))
	if not os.path.isdir(os.path.join(folder,"9.-videos")):			# 9, VIDEOS
		os.mkdir(os.path.join(folder,"9.-videos"))
	if not os.path.isdir(os.path.join(folder,"10.-others")):		# 10, OTHERS
		os.mkdir(os.path.join(folder,"10.-others"))

#toast = ToastNotifier()
#toast.show_toast("File Organizer", "The process has been started", duration=30)

init()
while True:
	files = os.listdir(folder)
	for file in files:
		if os.path.isfile(file) and file != "fileOrganize.py" and file != "fileOrganize.bat" and file != "fileOrganize.vbs":
			ext = (file.split(".")[-1]).lower()
			
			if ext in image_formats:
				shutil.move(file,"1.-images/"+file)
			elif ext in audio_formats:
				shutil.move(file,"8.-audio/"+file)
			elif ext in video_formats:
				shutil.move(file,"9.-videos/"+file)
			elif ext in docs_formats:
				shutil.move(file,"4.-docs/"+file)
			elif ext in progs_formats:
				shutil.move(file,"7.-programs/"+file)
			elif ext in zip_formats:
				shutil.move(file,"3.-compromises/"+file)
			elif ext in crel_formats:
				shutil.move(file,"2.-corel/"+file)
			elif ext in diseñ_formats: 
				shutil.move(file,"5.-design/"+file)
			elif ext in flexi_formats:
				shutil.move(file,"6.-flexi/"+file)
			else:
				shutil.move(file,"10.-others/"+file)

	del files
	sleep(5) #if program is using too much memory increase the value of sleep function 


