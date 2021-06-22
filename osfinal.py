# ROUND ROBIN SCHEDULING WITH OPTIMUM QUANTUM TIME
import matplotlib.pyplot as plt
import numpy as np
import math
import copy
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
matplotlib.interactive(True)
import random
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
    


def unpack_all():
        rr.pack_forget()
        l5.pack_forget()
        destroy.pack_forget()
#round robin starts here
def rr():
        unpack_all()
        n = random.randint(3, 10)
        arrivalTime = [i for i in range(n)]
        arrivalTime2=arrivalTime
        burstTime = [random.randint(1, 30) for i in range(n)]
        burstTime2=burstTime
        process = ['P' + str(i) for i in range(n)]
        process2=['P' + str(i) for i in range(n)]
        quantom = random.randint(0, 30)
        execTime = [0 for _ in range(n)]
        execTime2=[0 for _ in range(n)]
        d = arrivalTime[:]
        d2=copy.deepcopy(d)
        e = burstTime[:]
        e2=copy.deepcopy(e)
        p = process[:]
        p2=copy.deepcopy(p)
        f = Frame(root)
        switch=-1
        switch2=-1
        f.pack()
        Label(f, text="\nRound Robin Scheduling\n", font=('Helveltika bold', 12)).pack()
        Label(f, text="Arrival Time:  " + str(arrivalTime)).pack(anchor=W)
        Label(f, text="Process:  " + str(process)).pack(anchor=W)
        Label(f, text="Quantom:  " + str(quantom)).pack(anchor=W)
        Label(f, text="Burst Time:  " + str(burstTime)).pack(anchor=W)
        flag = False
        cnt = execTime[:]
        while len(d) > 0:
            switch+=1
            flag = True
            if e[0] > quantom:
                flag = False
                e[0] -= quantom
                e.append(e[0])
                p.append(p[0])
                d.append(d[0])
            del d[0]
            if flag:
                for i in d:
                    cnt[i] += e[0]
            else:
                for i in d:
                    cnt[i] += quantom
            del p[0]
            del e[0]
        for x in arrivalTime:
            t = burstTime[x] % quantom
            if t == 0:
                execTime[x] = cnt[x] + quantom
            else:
                execTime[x] = cnt[x] + t

        TatTime = list()
        for i in range(0, n):
            TatTime.append(execTime[i] - arrivalTime[i])
        waitTime = [TatTime[i] - burstTime[i] for i in range(n)]

        for i in range(len(waitTime)):
            if waitTime[i] < 0:
                waitTime[i] = 0

        avg = sum(waitTime) / float(n)
        avg_tat=sum(TatTime)/float(n)
        Label(f, text="\n----- After Performing Round Robin Scheduling Algorithm -----\n").pack(anchor=W)
        Label(f, text="Arrival Time:  " + str(arrivalTime)).pack(anchor=W)
        Label(f, text="Process:  " + str(process)).pack(anchor=W)
        Label(f, text="Quantom:  " + str(quantom)).pack(anchor=W)
        Label(f, text="Burst Time:  " + str(burstTime)).pack(anchor=W)
        Label(f, text="Completion Time:  " + str(execTime)).pack(anchor=W)
        Label(f, text="Turn Around Time:  " + str(TatTime)).pack(anchor=W)
        Label(f, text="Wait Time:  " + str(waitTime)).pack(anchor=W)
        Label(f, text="Context Switches:  " + str(switch)).pack(anchor=W)
        Label(f, text="Average Turn Around Time: " + str(avg_tat)).pack(anchor=W)
        Label(f, text="Average Wait Time: " + str(avg)).pack(anchor=W)
        l1 = Label(root, text='')
        #l1.pack()
        #runOther.pack(padx=120, side=LEFT)
        #destroy.pack(padx=10, side=LEFT)


        cnt.clear()
        quant=list()
        quantom_list=list()
        Label(f, text="\n----- After Performing Round Robin Algorithm with Optimum Quantum Time-----\n").pack(anchor=W)
        #second scheduling starts
        flag = False
        cnt = execTime2[:]
        cnt_shadow=burstTime2[:]        
        cnt_shadow.sort()
        mid=len(cnt_shadow)//2
        res=int((cnt_shadow[mid]+cnt_shadow[~mid])/2)
        quantom2=math.ceil(math.sqrt(res*cnt_shadow[len(cnt_shadow)-1]))
        while len(d2) > 0:
            switch2+=1
            cnt_shadow.clear()
            cnt_shadow=e2[:]        
            cnt_shadow.sort()
            mid=len(cnt_shadow)//2
            res=int((cnt_shadow[mid]+cnt_shadow[~mid])/2)
            quantom2=math.ceil(math.sqrt(res*cnt_shadow[len(cnt_shadow)-1]))
            quant.append(quantom2)
            quantom_list.append(quantom)
            #Label(f, text="Quantom:  " + str(quantom2)).pack(anchor=W)
            flag = True
            if e2[0] > quantom2:
                flag = False
                e2[0] -= quantom2
                e2.append(e2[0])
                p2.append(p2[0])
                d2.append(d2[0])
            del d2[0]
            if flag:
                for i in d2:
                    cnt[i] += e2[0]
            else:
                for i in d2:
                    cnt[i] += quantom2
            del p2[0]
            del e2[0]
        for x in arrivalTime2:
            t2 = burstTime2[x] % quantom2
            if t2 == 0:
                execTime2[x] = cnt[x] + quantom2
            else:
                execTime2[x] = cnt[x] + t2

        TatTime2 = list()
        for i in range(0, n):
            TatTime2.append(execTime2[i] - arrivalTime2[i])
        waitTime2 = [TatTime2[i] - burstTime2[i] for i in range(n)]

        for i in range(len(waitTime2)):
            if waitTime2[i] < 0:
                waitTime2[i] = 0

        avg2 = sum(waitTime2) / float(n)
        avg_tat2=sum(TatTime2)/float(n)
        # Label(f, text="\n----- After Performing Round Robin Algorithm with Optimum Quantum Time-----\n").pack(anchor=W)
        Label(f, text="Arrival Time:  " + str(arrivalTime2)).pack(anchor=W)
        Label(f, text="Process:  " + str(process2)).pack(anchor=W)
        #Label(f, text="Quantom:  " + str(quantom2)).pack(anchor=W)
        Label(f,text = "Burst Time:  "+ str(burstTime2)).pack(anchor = W)
        Label(f, text="Completion Time:  " + str(execTime2)).pack(anchor=W)
        Label(f, text="Turn Around Time:  " + str(TatTime2)).pack(anchor=W)
        Label(f, text="Wait Time:  " + str(waitTime2)).pack(anchor=W)
        Label(f, text="Context Switches:  " + str(switch2)).pack(anchor=W)
        Label(f, text="Average Turn Around Time: " + str(avg_tat2)).pack(anchor=W)
        Label(f, text="Average Wait Time: " + str(avg2)).pack(anchor=W)
        l1 = Label(root, text='')
        l1.pack()
        #runOther.pack(padx=120, side=LEFT)
        destroy.pack(padx=10, side=LEFT)
       

#round robin ends here
#graph 
        def plot():
          
            # the figure that will contain the plot
            fig = Figure(figsize = (5, 5),dpi = 100)
            
            # list of squares
            #y = [i**2 for i in range(101)]
          
            # adding the subplot
            plot1 = fig.add_subplot(111)
            plot1.set_title("Waiting time comparison")
            plot1.set_xlabel("Process number")
            plot1.set_ylabel("Waiting Time")
          
            # plotting the graph
            plot1.plot(waitTime)
            plot1.plot(waitTime2)

            canvas = FigureCanvasTkAgg(fig,master = window)  
            canvas.draw()
            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().pack()
          
            # creating the Matplotlib toolbar
            toolbar = NavigationToolbar2Tk(canvas, window)
            toolbar.update()
          
            # placing the toolbar on the Tkinter window
            canvas.get_tk_widget().pack()

        
        def plot1():
          
            # the figure that will contain the plot
            fig = Figure(figsize = (5, 5),dpi = 100)
          
            # list of squares
            #y = [i**2 for i in range(101)]
          
            # adding the subplot
            plot1 = fig.add_subplot(111)
            plot1.set_title("Turn Around Time Comparison")
            plot1.set_xlabel("Process number")
            plot1.set_ylabel("Turn Around Time")
          
            # plotting the graph
            plot1.plot(TatTime)
            plot1.plot(TatTime2)

            canvas2 = FigureCanvasTkAgg(fig,master = window2)  
            canvas2.draw()
            # placing the canvas on the Tkinter window
            canvas2.get_tk_widget().pack()
          
            # creating the Matplotlib toolbar
            toolbar2 = NavigationToolbar2Tk(canvas2, window2)
            toolbar2.update()
          
            # placing the toolbar on the Tkinter window
            canvas2.get_tk_widget().pack()    


        def plot_quant():
          
            # the figure that will contain the plot
            fig = Figure(figsize = (5, 5),dpi = 100)
          
            # list of squares
            #y = [i**2 for i in range(101)]
          
            # adding the subplot
            plot_quant = fig.add_subplot(111)
            plot_quant.set_title("Quantum Time Comparison")
            plot_quant.set_xlabel("Context Switches")
            plot_quant.set_ylabel("Quantum Time")
          
            # plotting the graph
           # plot_quant.plot(quantom_list)
            plot_quant.plot(quant)

            canvas_quant = FigureCanvasTkAgg(fig,master = window_quant)  
            canvas_quant.draw()
            # placing the canvas on the Tkinter window
            canvas_quant.get_tk_widget().pack()
          
            # creating the Matplotlib toolbar
            toolbar_quant = NavigationToolbar2Tk(canvas_quant, window_quant)
            toolbar_quant.update()
          
            # placing the toolbar on the Tkinter window
            canvas_quant.get_tk_widget().pack()        

#plotting the waiting time
        window = Tk()
  
        # setting the title 
        window.title('Graph for comparison of waiting time')
        # dimensions of the main window
        window.geometry("500x500")
          
        # button that displays the plot
        plot_button1 = Button(master = window, command = plot, width = 35, text = "Waiting time")          
        # place the button 
        # in main window
        plot_button1.pack(padx=10)
#plotting the turn around time window
        window2 = Tk()
  
        # setting the title 
        window2.title('Graph for comparison of turn around time')
        # dimensions of the main window
        window2.geometry("500x500")
        plot_button2 = Button(master = window2, command = plot1, width = 35, text = "Turn around time")
        plot_button2.pack(padx=10)

#plotting the graph function
        window_quant =  Tk()
        window_quant.title('Graph for comparison of quantum time')
        # dimensions of the main window
        window_quant.geometry("500x500")
        plot_button_quant = Button(master = window_quant, command = plot_quant, width = 35, text = "Quantum time")

        plot_button_quant.pack(padx=10)
#graph plotting ends
root = Tk()
root.title("Scheduling Algorithm Simulator\n")
destroy = Button(root, text="Quit", command=quit)
# runOther = Button(root, text="Run Other", command=app)
f = Frame(root)
f.pack()
f.pack_forget()
w = Label(root, text="\n    Scheduling Algorithm Simulator \n   \t", font=('Helveltika bold', 14))
#c = Label(root, text="\nChoose any one from below:\n")
w.pack()
#c.pack() 
rr = Button(root, text="Round Robin Scheduling", width=35, command=rr)
rr.pack(padx=10)
l5 = Label(root, text='')
l5.pack()
   
   
destroy.pack(padx=10)
  
# the main Tkinter window





root.mainloop()        


# if __name__ == '__main__':
#     app()