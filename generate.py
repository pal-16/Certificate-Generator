import pandas as pd
import smtplib 
import string

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

from PIL import Image, ImageDraw, ImageFont
from pandas import ExcelWriter
from pandas import ExcelFile

password ="######" #Your Password
fromaddr = "#####" #Your Email
df = pd.read_excel('sample-excel-sheet.xlsx')   # Your excel sheet with Participants Name and Email


for i in df.index:
	image = Image.open('########.jpg')           #Your certficate template
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype('fonts/GoogleSans-Regular.ttf', size=50)
	color = 'rgb(0, 230, 118)'
	name = df['Name'][i] 
	name.upper()
	print(i+1,name)
	length=len(name)
	x=1056/2-(length*25)/2   #Here I have calcualted the coordinates of the name to be placed in the certificate assuming each alphabet taking 25 pixel and the certificate width is 1056 pixel
	print(x)
	draw.text((x, 300), name, fill=color, font=font)	
	temp="sample"
	imageName = "certificates/"+temp+".pdf"
	image.save(imageName)
	
	toaddr = df['Email'][i]
	msg = MIMEMultipart() 
	msg['From'] = "#####"   #Your Email Id 
	msg['Subject'] = "Certificate for Completing your Android Study Jam"
	body = '''Please find attached your certificate for completion of the Kotlin Course powered by Anrdoid.
			  
	Regards
	DSC 
			'''

	msg.attach(MIMEText(body, 'plain')) 

	filename = name +".pdf"
	attachment = open(imageName, "rb")
	p = MIMEBase('application', 'octet-stream') 

	p.set_payload((attachment).read()) 
	encoders.encode_base64(p) 
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
	msg.attach(p) 

	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login(fromaddr, password) 
	text = msg.as_string() 
	s.sendmail(fromaddr, toaddr, text) 

s.quit() 
 