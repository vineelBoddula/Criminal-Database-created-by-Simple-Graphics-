# Sources Cited: Collier, R. "Lectures Notes for COMP1405B - Introduction to Computer Science I" [PDF document]. Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015).
#                daffy duck, Tutorialspoint. (2015-12-04). http://www.toonbarn.com/cartoon-network/the-looney-tunes-show-brings-jailbird-and-jailbunny-to-cartoon-network/ (This referance and the following are for imgages used)
#				 bugs bunny, Tutorialspoint. (2015-12-04). http://www.toonbarn.com/cartoon-network/the-looney-tunes-show-brings-jailbird-and-jailbunny-to-cartoon-network/ 
#				 batman, comicVine. (2015-12-04). http://static.comicvine.com/uploads/original/11125/111253442/4897645-batman.jpg
#				 Superman, wired. (2015-12-04). http://www.wired.com/images_blogs/underwire/2013/06/handcuffs.jpg
#				 lex luthor, supermanHomepage. (2015-12-04). http://www.supermanhomepage.com/images/miscellaneous/sup15-lex.jpg 
#				loading, encrypted-tbn3.gstatic (2015-12-04) .tumblrhttps://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcR00TzefNxjmgoyGnh4gz-l5nL2lchYKogZkBmDQwy9Y2vgjzMZFw
#				 death note, vignette2.wikia.nocookie. (2015-12-04). http://vignette2.wikia.nocookie.net/bleachfanfiction/images/d/d3/Death_note_delete.gif/revision/latest?cb=20150416055804
#				Spiderman, 	30.media.tumblr (2015-12-04) .http://30.media.tumblr.com/tumblr_l3u6r41mdT1qbkj2ko1_500.jpg

from SimpleGraphics import * 

# this turns off SimpleGraphics auto refresh and speeds everything up
setAutoUpdate(False)

# this changes the background colour to black and the line width to 0
background("black")

setOutline("white")

#criminal database class 
class CriminalDatabase:
	
	#init method 
	def __init__(self,name,age,height,eyeColor,imgName,dangerLevel): 
		self.__name = name
		self.__age = age
		self.__height = height
		self.__eyeColor = eyeColor
		self.__imgName = imgName
		self.__dangerLevel = dangerLevel
	
	#down below are setters methods (mutator) 
	def setName(self,name):
		self.__name = name 
	
	def setAge(self,age):
		self.__age = age 
	
	def setHeight(self,height):
		self.__height = height 
	
	def setEyeColor(self,eyeColor):
		self.__eyeColor = eyeColor
	
	def setImgName(self, imgName):
		self.__imgName = imgName
	
	def setDangerLevel(self, dangerLevel):
		self.__dangerLevel = dangerLevel
	
	#down below are getter methods (accessors)
	def getName(self):
		return self.__name
	
	def getAge(self):
		return self.__age
	
	def getHeight(self):
		return self.__height
	
	def getEye(self):
		return self.__eyeColor
	
	def getImgName(self):
		return self.__imgName
	
	def getDangerLevel(self):
		return self.__dangerLevel
	
	#to check if image exists and fits
	def checkImage(self,imgName):
		flag = False
		try: 
			imgLoaded = loadImage(imgName)
			#to check img height and length  
			if(getWidth(imgLoaded) <=280 and getHeight(imgLoaded) <=210):
				flag = True
			else:
				flag = False
				print("\n--------------IMAGE IS TO BIG---------------------------")
			
		except: 	
			print("-------------------Image not found-----------------------")
			print("Please retype all the values")
			flag = False 
		return flag
		
	#This method draws everything in simplegraphics 	
	def draw(self):
		
		clear() 
		#Title
		imgLoadedTitle = loadImage("Title.gif")
		drawImage(imgLoadedTitle,0,0)
		
		#subject Name Title
		imgLoadedName = loadImage("subjectName.gif")
		drawImage(imgLoadedName,10,140)
		
		#subject Name 
		setFont("Algerian", "18")
		text(280, 162, self.getName())

		#Subject age Title 
		imgLoadedAge = loadImage("subjectAge.gif")
		drawImage(imgLoadedAge,10,210)
		
		#Subject age
		setFont("Algerian", "18")
		text(280, 232, self.getAge())
		
		#Subject height Title
		imgLoadedHeight = loadImage("subjectHeight.gif")
		drawImage(imgLoadedHeight,10,280)
		
		#Subject height 
		setFont("Algerian", "18")
		text(280, 302, self.getHeight())
		
		#Subject Eye Color Title 
		imgLoadEye = loadImage("subjectEye.gif")
		drawImage(imgLoadEye,10,355)

		#Subject Eye Color
		setFont("Algerian", "18")
		text(280, 378, self.getEye())
		
		#subject Danger Level Title 
		imgLoadDanger = loadImage("subjectDangerLevel.gif")
		drawImage(imgLoadDanger,250,420)

		#subject Danger Level
		setFill(self.getDangerLevel())
		rect(30, 500, 700, 50)
		setFill("white")
		
		#draw face image 
		imgLoadFace = loadImage(self.getImgName())
		drawImage(imgLoadFace,480,150)
		
		
		
def main(): 
	print("--------------Loading data from the TextFile-----------------")
	
	#load the loading image
	imgLoad = loadImage("loading.gif")
	drawImage(imgLoad,10,0)
	#dictionary
	criminalDatabaseDic = {}
	#loads all data from textfile to the dictionary
	criminalDatabaseDic = loadDatabase(criminalDatabaseDic)
	
	
	while not closed(): 
		
		print("\n======================================================")
		print("Menu: ")
		print("	A. Add subject to the Criminal Database ")
		print("	B. Remove subject from the Criminal Database")
		print("	C. Search the database")
		print("	D. Display everyone in the database")
		print("	Q. Save changes to database and QUIT")
		userInput = str(input("Please select one of the menu: ")).upper()
		flag = False 
		flagTwo= False
		
		#add to the database 
		if(userInput == "A"): 
			
			while True: 
				try:
					name = str(input("What is the name of the subject (First Name ONLY): "))
					age = int(input("What is the age of the subject: ")) 
					height = int(input("What is the height of the subject (pleace enter in centimeters): "))
					eyeColor = str(input("What is the subject's eye color: "))
					imgName = str(input("Name of the Image: "))
					
					print("In this data base criminals are aranged in Special order")
					print("Red being the highest and Green being the lowest")
					print("Red, Yellow and Green")
					dangerLevel = str(input("Danger Level: ")).upper()
					if(dangerLevel =="RED"):
						dangerLevel ="firebrick3" 
					elif (dangerLevel =="GREEN"):
						dangerLevel ="chartreuse3"
					elif (dangerLevel == "YELLOW"):
						dangerLevel = "goldenrod2"
					else:
						print("----------------Invalid input of dangerLevel-----------------")
						print("AUTOMATIC setting to YELLOW")
						dangerLevel = "goldenrod2"
					#Creating obejct 
					criminal = CriminalDatabase(name,age,height,eyeColor,imgName,dangerLevel)
					flag = criminal.checkImage(imgName)
					
					
					if(flag == True):
						
						if name in criminalDatabaseDic:
							print("-----------------Subject already exists---------------------")
							
						else: 
							criminalDatabaseDic[name] =  name,age,height,eyeColor,imgName,dangerLevel
							criminal.draw()
							break
					
				except ValueError:
					print("-----------------------Invalid Input------------------------------")
					
		#remove from the database 
		elif(userInput =="B"):
			name = str(input("What is the name of the subject (First Name ONLY): "))
			try:
				del criminalDatabaseDic[name] #delete
				print("Subject found and Successful deletion")
				clear() 
		
				#Title
				imgLoadedTitle = loadImage("Title.gif")
				drawImage(imgLoadedTitle,0,0)
		
				#Deleted
				imgLoadedDeleted = loadImage("DeathnoteDelete.gif")
				drawImage(imgLoadedDeleted,150,150)
			except KeyError:
				print(name," This subject doesn't exist \n")
			
		#search the database 
		elif(userInput =="C"):
			name = str(input("What is the name of the subject to be searched (First Name ONLY): "))
			if name in criminalDatabaseDic:
				name,age,height,eyeColor,imgName,dangerLevel = criminalDatabaseDic[name]
				criminal = CriminalDatabase(name,age,height,eyeColor,imgName,dangerLevel)
				criminal.draw()
			else:
				print("-----------------Can't find the subject----------------")
		
		#list everyone in the database 		
		elif(userInput =="D"): 
			print("\nLIST OF SUBJECTS IN DATABASE")
			for key in criminalDatabaseDic:
				print(key)
				
		#save everything to the textfile 
		elif(userInput == "Q"):
			safeToFile(criminalDatabaseDic)
			print("Successfull saved to the database")
			break	
		else:
			print("---------Invalid input----------------")

#load database function 			
def loadDatabase(criminalDatabaseDic): 
	filehnd1 = open("CriminalDatabase.txt","r")
	value = [row.strip("\n") for row in filehnd1.readlines()]
		
	for x in range(0,len(value)):
		lst = value[x].split(" ")
		key = lst[0]
		criminalDatabaseDic[key] =  (lst[0]), int(lst[1]), int(lst[2]), (lst[3]), (lst[4]), (lst[5])
		
	
	return criminalDatabaseDic

#save everything to textfile 
def safeToFile(criminalDatabaseDic):
		fileName = "CriminalDatabase.txt"
		filehnd1 =open(fileName, "w") #write to the file
		
		for val in criminalDatabaseDic.values():
			
			val = str(val)
			val = val.strip("(")
			val = val.strip(")") 
			val = val.replace(",", "")
			val = val.replace("'","")
			
			filehnd1.write(str(val) + "\n")

main() #run main function 