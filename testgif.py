import tkinter as tk

'''--------------global variables----------------'''
framelist = []      # List to hold all the frames
frame_index = 0 
count = 0
anim = None
list_gif_frames =[]

'''-----------------methods---------------------'''
def animate_gif(count):  
    global anim
    l1.config(image = framelist[count])
    count +=1
        
    if count > last_frame:
        count = 0  
    #recall animate_gif method    
    anim = window.after(100, lambda :animate_gif(count))        
          
def stop_gif():
    global anim
    #stop recall method
    window.after_cancel(anim)

'''-------------Tkinter GUI main window----------------------'''
window = tk.Tk()
window.title("GIF LOADED")
window.geometry("300x300")
'''--------------count all frames in gif and saved in a list-----------------'''
while True:
    try:
        # Read a frame from GIF file
        part = 'gif -index {}'.format(frame_index)
        frame = tk.PhotoImage(file='loading.gif', format=part)
    except:
        print("break")
        last_frame = frame_index - 1    # Save index for last frame
        break               # Will break when GIF index is reached
    framelist.append(frame)
    print(len(framelist))
    frame_index += 1 
'''------------label to show gif--------------------'''
l1 = tk.Label(window, bg="purple", image = "")
l1.pack()
'''-----------------button to start gif--------------------'''
b1 = tk.Button(window, text = "start", command = lambda :animate_gif(0))
b1.pack()
'''---------------button to stop gif---------------------------'''
b2 = tk.Button(window, text = "stop", command = stop_gif)
b2.pack()

window.mainloop()