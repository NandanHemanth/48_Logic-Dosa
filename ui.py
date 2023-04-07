import tkinter
from subprocess import call
from subprocess import PIPE, Popen, STDOUT, TimeoutExpired
from numpy import size

root = tkinter.Tk()

def algo():
    cmd="Python3 {}".format("astar.py")
    process_machine = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, text=True)
    pass

def quiz():
    path_to_file="C:/Users/Mithul/Desktop/vsc/hackathon/dotSlash/48_Logic-Dosa/article.txt"
    import mcqg
    mcqg.main(path_to_file)

def quit():
    root.destroy()
    

root.title("LogicDosa")

root.geometry("1000x500")

welcome= tkinter.Label(root, text="Welcome to greater learning.",font=('Helevetica',24))
welcome.pack()


options=tkinter.Label(root,text="\n\nChoose a service.",font=('Helevetica',20))
options.pack()

button1=tkinter.Button(root,command=algo,text="Visualise Algorithms",height=3,width=15,fg="white",bg="black",activebackground="white",activeforeground="black")
button1.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

button2=tkinter.Button(root,command=quiz,text="Generate a quiz",height=3,width=15,fg="white",bg="black",activebackground="white",activeforeground="black")
button2.place(relx=0.5,rely=0.7,anchor=tkinter.CENTER)

button3=tkinter.Button(root,command=quit,text="QUIT",height=3,width=15,fg="white",bg="black",activebackground="white",activeforeground="black")
button3.place(relx=0.5,rely=0.9,anchor=tkinter.CENTER)

root.attributes('-fullscreen', True)
root.mainloop()