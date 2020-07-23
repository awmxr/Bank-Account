# Amir Marvasti Nejad
# All Right Reserved
# 1399.2.27
# T03 with tkinter
import tkinter as tk
import datetime as dt
import tkinter.messagebox as tm
class Account:
    Interest_rate = 15 / 100
    number_of_accounts = 0
    def __init__(self,owner,balance,last_used):
        self.owner = owner
        self.balance = balance
        self.last_used = last_used
        Account.number_of_accounts += 1
    
    def deposit(self,a):
        self.balance += int(a)
        self.last_used = dt.datetime.today()
        # print(f"{self.last_used.year}/{self.last_used.month}/{self.last_used.day}")
        # print(self.balance)
    
    def witdraw(self,a):
        if self.balance < int(a):
            print("mojodi kafi nist")
        else:
            self.balance -= int(a)
            self.last_used = dt.datetime.today()
            print(f"{self.last_used.year}/{self.last_used.month}/{self.last_used.day}")
            print(self.balance)

    @classmethod
    def change_rate(cls,new_rate):
        cls.Interest_rate = new_rate / 100
    
    def __str__(self):
        return f"Account Owner : {self.owner}\nAccount Balance : {self.balance}"
    
    def __del__(self):
        print(f"Account of {self.owner} with balance of {self.balance} has been removed.")

class Application(tk.Frame):
    accounts = {}
    def __init__(self,master=None):
        # super().__init__(master)
        super().__init__(master)
        self.master = master
        # self.owner = owner
        # self.balance = balance
        # self.last_used = last_used
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.make = tk.Button(self)
        self.make["text"] = "1.make an Account"
        self.make["command"] = self.make_Account
        self.make.pack()
        self.Show_accounts = tk.Button(self)
        self.Show_accounts["text"] = "2.Show Accounts"
        self.Show_accounts["command"] = self.show__accounts2
        self.Show_accounts.pack()
        self.quit = tk.Button(self, text="QUIT", fg="red",command=self.master.destroy)
        self.quit.pack()

    def make_Account(self):
        self.newtk = tk.Tk()
        self.label1 = tk.Label(self.newtk,text = "Name")
        self.entry1 = tk.Entry(self.newtk)
        self.label2 = tk.Label(self.newtk,text = "Mojodi Avalie")
        self.entry2 = tk.Entry(self.newtk)
        self.buttom1 = tk.Button(self.newtk)
        self.buttom1["text"] = "Enter"
        self.buttom1["command"] = self.hty
        self.label1.pack()
        self.entry1.pack()
        self.label2.pack()
        self.entry2.pack()
        self.buttom1.pack(side = tk.BOTTOM)
        

    
    def show__accounts2(self):
        self.newtk_acco2 = tk.Tk()
        # self.make_lis = []
        self.label_search = tk.Label(self.newtk_acco2,text = "Search")
        self.entry_search = tk.Entry(self.newtk_acco2)
        self.buttom_search = tk.Button(self.newtk_acco2,text = "Enter",command = self.search)
        self.label_search.pack()
        self.entry_search.pack()
        self.buttom_search.pack()
        for i in Application.accounts.values():
            self.lablen = tk.Label(self.newtk_acco2,text = i.owner)
            self.lablen.pack()
            
            
    
    def search(self):
        
        # self.name_list = []
        # for i in range(len(Application.accounts)):
        #     self.name_list.append()
        if self.entry_search.get() in Application.accounts.keys():
            self.x = Application.accounts.get(self.entry_search.get())
            self.newtk_acco = tk.Tk()
            self.newtk_acco2.destroy()
            self.button_acco = tk.Button(self.newtk_acco,text = f"{self.x.owner}",command = self.show_account3)
            self.button_acco.pack()
            # self.j = self.i
        else:
            tm.showinfo( f"Hello", "not found")


            

    def show_account3(self):
        self.newtk_acco3 = tk.Tk()
        self.newtk_acco.destroy()
        self.label_balance = tk.Label(self.newtk_acco3,text = f"Mojodi : {self.x.balance}")
        self.label_lastused = tk.Label(self.newtk_acco3,text = f"Last used : {self.x.last_used}")
        self.label_balance.pack()
        self.label_lastused.pack()
        self.buttom11 = tk.Button(self.newtk_acco3)
        self.buttom11["text"] = f"deposit"
        self.buttom11["command"] = self.show_deposit 
        self.buttom22 = tk.Button(self.newtk_acco3)
        self.buttom22["text"] = "witdraw"
        self.buttom22["command"] = self.show_witdraw
        self.buttom11.pack()
        self.buttom22.pack()
        # self.buttom2["command"] = self.show_deposit(acco)


    def show_deposit(self):
        self.newtk_acco3.destroy()
        self.newtk_deposit = tk.Tk()
        self.label_deposit = tk.Label(self.newtk_deposit,text = "mablaghe morede nazar ra vared konid")
        self.entry_deposit = tk.Entry(self.newtk_deposit)
        self.buttom_deposit = tk.Button(self.newtk_deposit)
        self.buttom_deposit["text"] = "Enter"
        # self.ezafe = self.entry_deposit.get()
        self.buttom_deposit["command"] = self.do_deposit
        self.label_deposit.pack()
        self.entry_deposit.pack()
        self.buttom_deposit.pack()
    def do_deposit(self):
        self.x.deposit(self.entry_deposit.get())
        self.newtk_deposit.destroy()
    def show_witdraw(self):
        self.newtk_acco3.destroy()
        self.newtk_witdraw = tk.Tk()
        self.label_witdraw = tk.Label(self.newtk_witdraw,text = "mablaghe morede nazar ra vared konid")
        self.entry_witdraw = tk.Entry(self.newtk_witdraw)
        self.buttom_witdraw = tk.Button(self.newtk_witdraw)
        self.buttom_witdraw["text"] = "Enter"
        self.buttom_witdraw["command"] = self.do_witdraw
        self.label_witdraw.pack()
        self.entry_witdraw.pack()
        self.buttom_witdraw.pack()
    def do_witdraw(self):
        if int(self.entry_witdraw.get()) > self.x.balance:
            tm.showinfo( f"Hello", "mojodi kafi nist")
        else:
            self.x.witdraw(self.entry_witdraw.get())
            self.newtk_witdraw.destroy()





    
    def hty(self):
        a = str(self.entry1.get())
        b = int(self.entry2.get())
        c = dt.datetime.today()
        person = Account(a,b,c)
        Application.accounts.update({a:person})
        # Application.accounts.append((self.owner,self.balance,self.last_used))
        tm.showinfo( f"Hello {a}", "your Account is ready")
        self.newtk.destroy()
        


        # print(a,b)

# accounts = []
root = tk.Tk()
app = Application(master=root)
app.mainloop()



