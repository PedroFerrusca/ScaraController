import serial
import serial_ports
from comandoArduino import CommandArduino
from Tkinter import Tk, RIGHT, BOTH, RAISED, LEFT, Canvas, NW, Text, END
from PIL import Image, ImageTk
import commands
from ttk import Frame, Button, Style, Combobox, Entry
from timeit import default_timer as timer 
from time import sleep
serialA = None
state = 0
baudrate = 115200
		
class App(Frame):

	def __init__(self, parent):

		Frame.__init__(self, parent)
		self.parent = parent
		self.initGUI()

	def initGUI(self):

		self.parent.title("SCARA Program by Pedro Ferrusca")
		#self.openLog(commands.getoutput("date"))
		self.logName = commands.getoutput("date")
		self.logName = self.logName.replace(" ", "")
		self.logName = self.logName.replace(":", "-")
		self.openLog(self.logName)
		self.style = Style()
		self.pack(fill=BOTH, expand=1)
		self.style.theme_use("default")
		self.startFrame = Frame(self, relief=RAISED, borderwidth=1)
		self.startFrame.pack(fill=BOTH, expand=True)
		self.logo = Image.open("SCARA.jpg")
		self.RobotImage = ImageTk.PhotoImage(self.logo)
		self.startCanvas =Canvas(self.startFrame, bg="white", height=self.logo.size[1]+20,
		 width=self.logo.size[0]+20)
		self.log = ""
		self.startCanvas.create_image(10,10, anchor=NW, image=self.RobotImage)
		self.startCanvas.pack(fill=BOTH, expand=1)
		self.startButton = Button(self, text="Start", command=self.destroyStart)
		self.startButton.pack()
		#self.mainCanvas = Canvas(self.startFrame, bg="white", height=self.logo.size[1]+20, width=500)
		self.mainText = Text(self.startFrame, width=50, height=50)
		self.mainFrame = Frame(self.startFrame, borderwidth=1, height=self.logo.size[1]+20, width=500)
		self.botonera1 = Frame(self.mainFrame, borderwidth=1)
		s = commands.getoutput("ls /dev/ttyA*")
		s2 = serial_ports.serialPorts()
		#self.devices = ["com5", "com6", "com7", "com8"]
		#self.devices = s.split('\n', s.count('\n'))
		self.devices = s2
		self.comboConnect = Combobox(self.botonera1, values=self.devices)
		self.comboConnect.pack(side=LEFT)
		self.connectButton = Button(self.botonera1, text="Connect with SCARA Robot", command=self.Connect)
		self.connectButton.pack(side=LEFT)
		self.botonera2 = Frame(self.mainFrame, borderwidth=1)
		self.botonera3 = Frame(self.mainFrame, borderwidth=1)
		self.botonera4 = Frame(self.mainFrame, borderwidth=1)
		self.botonera5 = Frame(self.mainFrame, borderwidth=1)
		self.botonera6 = Frame(self.mainFrame, borderwidth=1)
		self.degrees = Entry(self.botonera2)
		self.degrees2 = Entry(self.botonera3)
		self.degrees3 = Entry(self.botonera4)
		self.posX = Entry(self.botonera5)
		self.posY = Entry(self.botonera5)
		self.m1Button = Button(self.botonera2, text="M1", command=self.sendDegreesM1)
		self.m1Button.pack(side=LEFT)
		self.m2Button = Button(self.botonera3, text="M2", command=self.sendDegreesM2)
		self.m2Button.pack(side=LEFT)
		self.m3Button = Button(self.botonera4, text="M3", command=self.sendDegreesM3)
		self.m3Button.pack(side=LEFT)
		self.posXYButton = Button(self.botonera6, text="Position", command=self.sendPos)
		self.posXYButton.pack(side=LEFT)
		self.degrees.pack(side=LEFT)
		self.degrees2.pack(side=LEFT)
		self.degrees3.pack(side=LEFT)
		self.posX.pack(side=LEFT)
		self.posY.pack(side=LEFT)
		
	
	def destroyStart(self):
		self.startCanvas.destroy()
		self.startButton.destroy()
		self.botonera1.pack()
		self.botonera2.pack()
		self.botonera3.pack()
		self.botonera4.pack()
		self.botonera5.pack()
		self.botonera6.pack()
		#self.mainCanvas.pack(fill=BOTH, side=LEFT)
		self.mainText.pack(fill=BOTH, side=LEFT)
		self.log = 'Send Commands'
		self.mainText.insert(END, self.log)
		self.mainFrame.pack(fill=BOTH, side=LEFT)

	def Connect(self):
		s = "connected to " + self.comboConnect.get()
		print(s)
		serialA = serial.Serial(self.comboConnect.get(), baudrate, timeout=3)
		sleep(2)
		state=1
		c = CommandArduino("56", 1, serialA)
		print(c.send())
		self.printMessages("Connected: "+ self.comboConnect.get(), self.logName)
		
		
	def sendDegreesM1(self):
		m1 = (abs(int(self.degrees.get()))+1000)*(int(self.degrees.get())/abs(int(self.degrees.get())))
		serialA = serial.Serial(self.comboConnect.get(), baudrate, timeout=3)
		if m1 != 0:
			print(m1)
		if serialA.isOpen():
			m1command= CommandArduino(str(m1), 1, serialA)
			#m1command.send()
			self.printMessages("Sent: " + m1command.send(), self.logName)
			
				
		else:
			print("not connected")
			self.printMessages("Not Connected, Command attempted: "+ str(m1), self.logName)
		self.degrees.delete(0, END)
		
	def sendDegreesM2(self):
		m2 = (abs(int(self.degrees2.get()))+2000)*(int(self.degrees2.get())/abs(int(self.degrees2.get())))
		serialA = serial.Serial(self.comboConnect.get(), baudrate, timeout=3)
		if m2 != 0:
			print(m2)
		if serialA.isOpen():
			m2command= CommandArduino(str(m2), 1, serialA)
			#m2command.send()
			self.printMessages("Sent: " + m2command.send(), self.logName)
			
			
				
		else:
			print("not connected")
			self.printMessages("Not Connected, Command attempted: "+ str(m2), self.logName)
		self.degrees2.delete(0, END)

	def sendDegreesM3(self):
		m3 = (abs(int(self.degrees3.get()))+3000)*(int(self.degrees3.get())/abs(int(self.degrees3.get())))
		if m3 != 0:
			print(m3)
		if serialA is not None:
			m3command= CommandArduino(m3, 1, serialA)
			m3command.send()
			
				
		else:
			print("not connected")
			self.printMessages("Not Connected, Command attempted: "+ str(m3) , self.logName)
		self.degrees3.delete(0, END)
	def sendPos(self):
		print("pos")

	def sendStop(self):
		state =0

	def printMessages(self, Message, path):
		self.log = '\n' + Message
		self.mainText.insert(END, self.log)
		path = "Logs/" + path + ".txt"
		self.currentLog = open(path, "a")
		self.currentLog.write('\n' + Message + commands.getoutput("date +'%k:%M:%S'"))
		self.currentLog.close()

	def openLog(self, path):
		path = "Logs/" + path + ".txt"
		self.currentLog = open(path, "w")
		self.currentLog.write("Begin" + '\n' + commands.getoutput("date"))
		self.currentLog.close()
		

		



def main():

	root = Tk()
	ex = App(root)
	root.mainloop()

if __name__ == '__main__':
	main()

