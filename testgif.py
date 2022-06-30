import tkinter as tk

from matplotlib.pyplot import flag

class LoadingGif:
    def __init__(self):
        '''-------------Tkinter GUI main search_window----------------------'''
        self.framelist = []      # List to hold all the frames
        self.frame_index = 0 
        self.count = 0
        self.anim = None
        self.flag = True
        self.search_window = tk.Tk()
        self.search_window.title("GIF LOADED")
        self.search_window.geometry("300x300")
    '''-----------------methods---------------------'''
    def animate_gif(self, count):  
        if count == 0 and self.flag == True:
            self.l1 = tk.Label(self.search_window, bg="purple", text='', font=('Georgia 80'))
            self.l1.pack()
            self.flag = False
            
        self.l1.config(text='.'*count)
        count +=1
        
        if count > 3:
            count = 0  
        #recall animate_gif method    
        anim = self.l1.after(300, lambda :self.animate_gif(count))        
            
    def stop_gif(self):
        global anim
        #stop recall method
        self.l1.destroy()
        self.flag = True
    '''--------------count all frames in gif and saved in a list-----------------'''

    def generateGif(self):
        while True:
            try:
                # Read a frame from GIF file
                part = 'gif -index {}'.format(self.frame_index)
                frame = tk.PhotoImage(file='loading.gif', format=part)
            except:
                print("break")
                self.last_frame = self.frame_index - 1    # Save index for last frame
                break               # Will break when GIF index is reached
            self.framelist.append(frame)
            print(len(self.framelist))
            self.frame_index += 1 

        '''-----------------button to start gif--------------------'''
        self.b1 = tk.Button(self.search_window, text = "start", command = lambda :self.animate_gif(0))
        self.b1.pack()
        '''---------------button to stop gif---------------------------'''
        self.b2 = tk.Button(self.search_window, text = "stop", command = self.stop_gif)
        self.b2.pack()

        self.search_window.mainloop()

    
gif = LoadingGif()
gif.generateGif()