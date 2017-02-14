from tkinter import *
import isodata
import iso_graphic



class GUI:
	def __init__(self, master):
		self.master = master

		# configuring window options
		#master.configure(background='#a0adb8')
		master.minsize(width=700, height=680)
		
		#self.origin()
		isodata.clusterize()
		iso_graphic.origin()
		iso_graphic.clusterized()

		# labels for points display
		labels = []
		Label(master, text='Original points').place(x=20, y=10)
		for i, point in enumerate(isodata.points):
			t = str(i+1) + ' : ' + str(point)
			self.label = Label(master, text=t).place(x=20, y=(i+2)*15)

		clusters = isodata.clusterize()
		Label(master, text='Clusters:').place(x=20, y=220)
		
		for i, cluster in enumerate(clusters):
			z = 0
			text = "Cluster " + str(i+1)
			Label(master, text=text).place(x=20, y=(i+16)*16)
			#for point in cluster:
			#	Label(master, text=point).place(x=20, y=(i+16)*16)
			#	z = (i+16)*16

		

		cluster_button = Button(master, text='Clusterize').place(x=10, y=600)

		Label(master, text='Original points').place(x=400, y=310)
		Label(master, text='Clusterized points').place(x=400, y=620)

		self.canvas1 = Canvas(master, width=400, height=300)
		self.img1 = PhotoImage(file='origin.png')
		self.disp1 = self.img1.subsample(2, 2)
		self.canvas1.create_image(0, 0, image=self.disp1, anchor="nw")
		self.canvas1.place(x=250, y=10)
		
		self.canvas2 = Canvas(master, width=400, height=300)
		self.img2 = PhotoImage(file='clusters.png')
		self.disp2 = self.img2.subsample(2, 2)
		self.canvas2.create_image(0, 0, image=self.disp2, anchor="nw")
		self.canvas2.place(x=250, y=330)
		


	def origin(self):
		isodata.clusterize()
		iso_graphic.origin()
		iso_graphic.clusterized()


	

	def clusterized(self):

		self.canvas2 = Canvas(width=400, height=300)
		self.img2 = PhotoImage(file='clusters.png')
		self.disp2 = self.img2.subsample(2, 2)
		self.canvas2.create_image(0, 0, image=self.disp2, anchor="nw")
		self.canvas2.place(x=250, y=330)
		
	

root = Tk()
root.title("Isodata algorithm")
dic = GUI(root)
root.mainloop()
