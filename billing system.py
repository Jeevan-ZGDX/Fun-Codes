from tkinter import *
root=Tk()
root.tittle('billing slip')
root.geometry('1280x720')
bg_color='#4D0039'

#==================Top section=======================
title=Label(root,text='Billing Software',bg=bg_color,fg='white',font=('times new romman',25 ,'bold'),relif=GROOVE,bd=12)
title.pack(fill=X)

root.mainloop()
