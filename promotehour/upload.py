from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive



def upload_file():
	gauth = GoogleAuth()
	gauth.LocalWebserverAuth()

	drive = GoogleDrive(gauth)
	with open("shit.csv", 'r+') as infile:
		content = infile.read()
		file1 = drive.CreateFile({"title": "scraper_results.csv", "mimeType": 'text/csv'})
		file1.SetContentString(content)
		file1.Upload()