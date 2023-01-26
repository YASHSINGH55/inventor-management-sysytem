from csv import excel
from tkinter import messagebox
import pymongo as pm
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


myclient = pm.MongoClient("mongodb+srv://unseen:11223344@student.viqqtpa.mongodb.net/test")
mydb=myclient["mydatabase"]
print(myclient.list_database_names())
user_logins=mydb["logins"]
inventory=mydb["inventory"]
print(mydb.list_collection_names())
#print(inventory.count_documents({}))
#data={"_id":"1", "Product Id":"0001","Product Name":"Mobile","Sold":"10","Remaining":"100","Defective":"5","Total":"115"}
#y=inventory.insert_one(data)
#print(y.inserted_id)
#users={"_id":"Anuj","password":"11111111"}
#x=user_logins.insert_one(users)
#print(x.inserted_id)
 
#GUI
root=tk.Tk()
root.geometry("300x100")
root.title("Login")
id_var=tk.StringVar()
passw_var=tk.StringVar()
id_1=tk.StringVar()
Pid_1=tk.StringVar()
Pname_1=tk.StringVar()
Sold_1=tk.StringVar()
Rem_1=tk.StringVar()
Def_1=tk.StringVar()
Total_1=tk.StringVar()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
def submit():
    id=id_var.get()
    password=passw_var.get()
    login_id={'_id':id,'password':password}
    print(login_id)
    verify=user_logins.find_one(login_id)
    if verify==None:
        messagebox.showerror("Connection Error", "No Database Found")
    else:
        messagebox.showinfo("Connection", "Connected Successfully")
        root.withdraw()
        home()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------        
def home():
        id=id_var.get()
        password=passw_var.get()
        home = tk.Toplevel()
        home.geometry("1920x1080")
        home.title("Inventory Management System")
        
        def refresh_data():
            treev.delete(*treev.get_children())
            for x in mydb.inventory.find():
                treev.insert("", 'end', text ="L1",values =(x['_id'], x['Product Id'],x['Product Name'],x['Sold'],x['Remaining'],x['Defective'],x['Total']))

        user_name = Label(home,text = "Welcome "+id).place( x =110, y = 10, anchor = NE)
        insert_btn=tk.Button(home,text = 'Insert Product', command = insert_data).place(x=30,y=60)
        update_btn=tk.Button(home,text = 'Update Product', command = update_data).place(x=30,y=110)
        delete_btn=tk.Button(home,text = 'Delete Product', command = delete_data).place(x=30,y=160)
        find_btn=tk.Button(home,text = 'Find', command = find_data).place(x=30,y=210)
        refresh_btn=tk.Button(home,text = 'Refresh', command = refresh_data).place(x=30,y=260)
        #C = Canvas(home, bg="yellow",height=550, width=1450).place(x=30,y=200)
        
        # Add a Treeview widget
        treev = ttk.Treeview(home)
        treev.place(x=30,y=310)
        treev["columns"] = ("_id", "Product Id","Product Name","Sold","Remaining","Defective","Total")
        
        # Defining heading
        treev['show'] = 'headings'
        
        # Assigning the width and anchor to  the
        # respective columns
        treev.column("_id",anchor=CENTER, width=80)
        treev.column("Product Id",anchor=CENTER, width=80)
        treev.column("Product Name",anchor=CENTER, width=80)
        treev.column("Sold",anchor=CENTER, width=80)
        treev.column("Remaining",anchor=CENTER, width=80)
        treev.column("Defective",anchor=CENTER, width=80)
        treev.column("Total",anchor=CENTER, width=80)
        
        # Assigning the heading names to the
        # respective columns
        treev.heading("_id",text="Serial no",anchor=CENTER)
        treev.heading("Product Id",text="Product Id",anchor=CENTER)
        treev.heading("Product Name",text="Product Name",anchor=CENTER)
        treev.heading("Sold",text="Sold",anchor=CENTER)
        treev.heading("Remaining",text="Remaining",anchor=CENTER)
        treev.heading("Defective",text="Defective",anchor=CENTER)
        treev.heading("Total",text="Total",anchor=CENTER)
    
        # Inserting the items and their features to the
        # columns built
        for x in mydb.inventory.find():
            treev.insert("", 'end', text ="L1",values =(x['_id'], x['Product Id'],x['Product Name'],x['Sold'],x['Remaining'],x['Defective'],x['Total']))
        
        home.mainloop()   
#------------------------------------------------------------------------------------------------------------------------------------------------------------------        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
def insert_data():
            insert_data_1 = tk.Toplevel()
            insert_data_1.geometry("500x500")
            insert_data_1.title("Insert Data")
            
            def insert_main():
                id_2=id_1.get()
                Pid_2=Pid_1.get()
                Pname_2=Pname_1.get()
                Sold_2=Sold_1.get()
                Rem_2=Rem_1.get()
                Def_2=Def_1.get()
                Total_2=Total_1.get()
                my_entry={"_id":id_2, "Product Id":Pid_2,"Product Name":Pname_2,"Sold":Sold_2,"Remaining":Rem_2,"Defective":Def_2,"Total":Total_2}
                #my_entry={"_id":"99", "Product Id":Pid_2,"Product Name":"Mobile","Sold":"10","Remaining":"100","Defective":"5","Total":"115"}
                try:
                    entry_data=inventory.insert_one(my_entry)
                    messagebox.showinfo("Insert", "Inserted Successfully")
                except:
                    messagebox.showerror("Insert", "Error")
                    
                
            
            id_label = tk.Label(insert_data_1, text = 'ID', font=('calibre',10, 'bold')).grid(row=0,column=0)
            id_entry = tk.Entry(insert_data_1,textvariable = id_1, font=('calibre',10,'normal')).grid(row=0,column=1)
            Product_id_label = tk.Label(insert_data_1, text = 'Product ID', font=('calibre',10, 'bold')).grid(row=1,column=0)
            Product_id_entry = tk.Entry(insert_data_1,textvariable = Pid_1, font=('calibre',10,'normal')).grid(row=1,column=1)
            Product_name_label = tk.Label(insert_data_1, text = 'Product Name', font=('calibre',10, 'bold')).grid(row=2,column=0)
            Product_name_entry = tk.Entry(insert_data_1,textvariable = Pname_1, font=('calibre',10,'normal')).grid(row=2,column=1)
            Sold_label = tk.Label(insert_data_1, text = 'Sold', font=('calibre',10, 'bold')).grid(row=3,column=0)
            Sold_entry = tk.Entry(insert_data_1,textvariable = Sold_1, font=('calibre',10,'normal')).grid(row=3,column=1)
            Remaining_label = tk.Label(insert_data_1, text = 'Remaining', font=('calibre',10, 'bold')).grid(row=4,column=0)
            Remaining_entry = tk.Entry(insert_data_1,textvariable = Rem_1, font=('calibre',10,'normal')).grid(row=4,column=1)
            Defective_label = tk.Label(insert_data_1, text = 'Defective', font=('calibre',10, 'bold')).grid(row=5,column=0)
            Defective_entry = tk.Entry(insert_data_1,textvariable = Def_1, font=('calibre',10,'normal')).grid(row=5,column=1)
            Total_label = tk.Label(insert_data_1, text = 'Total', font = ('calibre',10,'bold')).grid(row=6,column=0)
            Total_entry=tk.Entry(insert_data_1, textvariable = Total_1, font = ('calibre',10,'normal')).grid(row=6,column=1)
            Update_btn=tk.Button(insert_data_1,text = 'Insert', command = insert_main).grid(row=7,column=1)
            insert_data_1.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------            
def update_data():
    update_data_1 = tk.Toplevel()
    update_data_1.geometry("500x500")
    update_data_1.title("Update Data")
    
    def update_main_1():
                id_2=id_1.get()
                Pid_2=Pid_1.get()
                myquery={"_id":id_2}
                my_entry={"$set":{"Product Id":Pid_2}}
                try:
                    entry_data=inventory.update_one(myquery,my_entry)
                    messagebox.showinfo("Update", "Product Id Updated Successfully")
                except:
                    messagebox.showerror("Update", "Error")
    def update_main_2():
                id_2=id_1.get()
                Pname_2=Pname_1.get()
                myquery={"_id":id_2}
                my_entry={"$set":{"Product Name":Pname_2}}
                try:
                    entry_data=inventory.update_one(myquery,my_entry)
                    messagebox.showinfo("Update", "Product Name Updated Successfully")
                except:
                    messagebox.showerror("Update", "Error")
    def update_main_3():
                id_2=id_1.get()
                Sold_2=Sold_1.get()
                myquery={"_id":id_2}
                my_entry={"$set":{"Sold":Sold_2}}
                try:
                    entry_data=inventory.update_one(myquery,my_entry)
                    messagebox.showinfo("Update", "Sold Updated Successfully")
                except:
                    messagebox.showerror("Update", "Error")
    def update_main_4():
                id_2=id_1.get()
                Rem_2=Rem_1.get()
                myquery={"_id":id_2}
                my_entry={"$set":{"Remaining":Rem_2}}
                try:
                    entry_data=inventory.update_one(myquery,my_entry)
                    messagebox.showinfo("Update", "Remaining Updated Successfully")
                except:
                    messagebox.showerror("Update", "Error")
    def update_main_5():
                id_2=id_1.get()
                Def_2=Def_1.get()
                myquery={"_id":id_2}
                my_entry={"$set":{"Defective":Def_2}}
                try:
                    entry_data=inventory.update_one(myquery,my_entry)
                    messagebox.showinfo("Update", "Defective Updated Successfully")
                except:
                    messagebox.showerror("Update", "Error")
    def update_main_6():
                id_2=id_1.get()
                Total_2=Total_1.get()
                myquery={"_id":id_2}
                my_entry={"$set":{"Total":Total_2}}
                try:
                    entry_data=inventory.update_one(myquery,my_entry)
                    messagebox.showinfo("Update", "Total Updated Successfully")
                except:
                    messagebox.showerror("Update", "Error")
    
    id_label = tk.Label(update_data_1, text = 'ID', font=('calibre',10, 'bold')).grid(row=0,column=0)
    id_entry = tk.Entry(update_data_1,textvariable = id_1, font=('calibre',10,'normal')).grid(row=0,column=1)
    update_text=tk.Label(update_data_1, text = 'Enter The Value That Has To Be Updated', font=('calibre',10, 'bold')).grid(row=1,column=0)
    
    Product_id_label = tk.Label(update_data_1, text = 'Product ID', font=('calibre',10, 'bold')).grid(row=2,column=0)
    Product_id_entry = tk.Entry(update_data_1,textvariable = Pid_1, font=('calibre',10,'normal')).grid(row=2,column=1)
    Update_btn_1=tk.Button(update_data_1,text = 'Update', command = update_main_1).grid(row=2,column=2)
    Product_name_label = tk.Label(update_data_1, text = 'Product Name', font=('calibre',10, 'bold')).grid(row=3,column=0)
    Product_name_entry = tk.Entry(update_data_1,textvariable = Pname_1, font=('calibre',10,'normal')).grid(row=3,column=1)
    Update_btn_2=tk.Button(update_data_1,text = 'Update', command = update_main_2).grid(row=3,column=2)
    Sold_label = tk.Label(update_data_1, text = 'Sold', font=('calibre',10, 'bold')).grid(row=4,column=0)
    Sold_entry = tk.Entry(update_data_1,textvariable = Sold_1, font=('calibre',10,'normal')).grid(row=4,column=1)
    Update_btn_3=tk.Button(update_data_1,text = 'Update', command = update_main_3).grid(row=4,column=2)
    Remaining_label = tk.Label(update_data_1, text = 'Remaining', font=('calibre',10, 'bold')).grid(row=5,column=0)
    Remaining_entry = tk.Entry(update_data_1,textvariable = Rem_1, font=('calibre',10,'normal')).grid(row=5,column=1)
    Update_btn_4=tk.Button(update_data_1,text = 'Update', command = update_main_4).grid(row=5,column=2)
    Defective_label = tk.Label(update_data_1, text = 'Defective', font=('calibre',10, 'bold')).grid(row=6,column=0)
    Defective_entry = tk.Entry(update_data_1,textvariable = Def_1, font=('calibre',10,'normal')).grid(row=6,column=1)
    Update_btn_5=tk.Button(update_data_1,text = 'Update', command = update_main_5).grid(row=6,column=2)
    Total_label = tk.Label(update_data_1, text = 'Total', font = ('calibre',10,'bold')).grid(row=7,column=0)
    Total_entry=tk.Entry(update_data_1, textvariable = Total_1, font = ('calibre',10,'normal')).grid(row=7,column=1)
    Update_btn_6=tk.Button(update_data_1,text = 'Update', command = update_main_6).grid(row=7,column=2)
    

    update_data_1.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------
def delete_data():
    delete_data_1 = tk.Toplevel()
    delete_data_1.geometry("500x500")
    delete_data_1.title("Delete Data")
    def delete_main():
                id_2=id_1.get()
                my_entry={"_id":id_2}
                #my_entry={"_id":"99", "Product Id":Pid_2,"Product Name":"Mobile","Sold":"10","Remaining":"100","Defective":"5","Total":"115"}
                try:
                    entry_data=inventory.delete_one(my_entry)
                    messagebox.showinfo("Delete", "Deleted Successfully")
                except:
                    messagebox.showerror("Delete", "Error")
    id_label = tk.Label(delete_data_1, text = 'ID', font=('calibre',10, 'bold')).grid(row=0,column=0)
    id_entry = tk.Entry(delete_data_1,textvariable = id_1, font=('calibre',10,'normal')).grid(row=0,column=1)
    Delete_btn=tk.Button(delete_data_1,text = 'Delete', command = delete_main).grid(row=1,column=1)
    delete_data_1.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def find_data():
            find_data_1 = tk.Toplevel()
            find_data_1.geometry("1080x400")
            find_data_1.title("Find Data")
            
            def find_main_1():
                treev.delete(*treev.get_children())
                id_2=id_1.get()
                myquery={"_id":id_2}
                z=mydb.inventory.find_one(myquery)
                if z==None:
                   messagebox.showerror("Find", "Data Not Found") 
                else:
                    for x in mydb.inventory.find(myquery):
                        treev.insert("", 'end', text ="L1",values =(x['_id'], x['Product Id'],x['Product Name'],x['Sold'],x['Remaining'],x['Defective'],x['Total']))
                        messagebox.showinfo("Find", "Data Found Successfully")
                
            def find_main_2():
                        treev.delete(*treev.get_children())
                        Pid_2=Pid_1.get()
                        myquery={"Product Id":Pid_2}
                        z=mydb.inventory.find_one(myquery)
                        if z==None:
                            messagebox.showerror("Find", "Data Not Found") 
                        else:
                            for x in mydb.inventory.find(myquery):
                                treev.insert("", 'end', text ="L1",values =(x['_id'], x['Product Id'],x['Product Name'],x['Sold'],x['Remaining'],x['Defective'],x['Total']))
                                messagebox.showinfo("Find", "Data Found Successfully")
            def find_main_4():
                        treev.delete(*treev.get_children())
                        Sold_2=Sold_1.get()
                        myquery={"Sold":Sold_2}
                        z=mydb.inventory.find_one(myquery)
                        if z==None:
                            messagebox.showerror("Find", "Data Not Found") 
                        else:
                            for x in mydb.inventory.find(myquery):
                                treev.insert("", 'end', text ="L1",values =(x['_id'], x['Product Id'],x['Product Name'],x['Sold'],x['Remaining'],x['Defective'],x['Total']))
                                messagebox.showinfo("Find", "Data Found Successfully")
            def find_main_5():
                        treev.delete(*treev.get_children())
                        Rem_2=Rem_1.get()
                        myquery={"Remaining":Rem_2}
                        z=mydb.inventory.find_one(myquery)
                        if z==None:
                            messagebox.showerror("Find", "Data Not Found") 
                        else:
                            for x in mydb.inventory.find(myquery):
                                treev.insert("", 'end', text ="L1",values =(x['_id'], x['Product Id'],x['Product Name'],x['Sold'],x['Remaining'],x['Defective'],x['Total']))
                                messagebox.showinfo("Find", "Data Found Successfully")
            def find_main_6():
                        treev.delete(*treev.get_children())
                        Def_2=Def_1.get()
                        myquery={"Defective":Def_2}
                        z=mydb.inventory.find_one(myquery)
                        if z==None:
                            messagebox.showerror("Find", "Data Not Found") 
                        else:
                            for x in mydb.inventory.find(myquery):
                                treev.insert("", 'end', text ="L1",values =(x['_id'], x['Product Id'],x['Product Name'],x['Sold'],x['Remaining'],x['Defective'],x['Total']))
                                messagebox.showinfo("Find", "Data Found Successfully")
            def find_main_7():
                treev.delete(*treev.get_children())
                Total_2=Total_1.get()
                myquery={"Total":Total_2}
                
                z=mydb.inventory.find_one(myquery)
                if z==None:
                    messagebox.showerror("Find", "Data Not Found") 
                else:
                    for x in mydb.inventory.find(myquery):
                        treev.insert("", 'end', text ="L1",values =(x['_id'], x['Product Id'],x['Product Name'],x['Sold'],x['Remaining'],x['Defective'],x['Total']))
                        messagebox.showinfo("Find", "Data Found Successfully")
            def find_main_3():
                        treev.delete(*treev.get_children())
                        Pname_2=Pname_1.get()
                        myquery={"Product Name":Pname_2}
                        z=mydb.inventory.find_one(myquery)
                        if z==None:
                            messagebox.showerror("Find", "Data Not Found") 
                        else:
                            for x in mydb.inventory.find(myquery):
                                treev.insert("", 'end', text ="L1",values =(x['_id'], x['Product Id'],x['Product Name'],x['Sold'],x['Remaining'],x['Defective'],x['Total']))
                                messagebox.showinfo("Find", "Data Found Successfully")
            def find_main_8():
                        treev.delete(*treev.get_children())
                        id_2=id_1.get()
                        Pid_2=Pid_1.get()
                        Pname_2=Pname_1.get()
                        Sold_2=Sold_1.get()
                        Rem_2=Rem_1.get()
                        Def_2=Def_1.get()
                        Total_2=Total_1.get()
                       
                        myquery={"_id":id_2, "Product Id":Pid_2,"Product Name":Pname_2,"Sold":Sold_2,"Remaining":Rem_2,"Defective":Def_2,"Total":Total_2}
                        z=mydb.inventory.find_one(myquery)
                        if z==None:
                            messagebox.showerror("Find", "Data Not Found") 
                        else:
                            for x in mydb.inventory.find(myquery):
                                treev.insert("", 'end', text ="L1",values =(x['_id'], x['Product Id'],x['Product Name'],x['Sold'],x['Remaining'],x['Defective'],x['Total']))
                                messagebox.showinfo("Find", "Data Found Successfully")         
                
            
            id_label = tk.Label(find_data_1, text = 'ID', font=('calibre',10, 'bold')).grid(row=0,column=0)
            id_entry = tk.Entry(find_data_1,textvariable = id_1, font=('calibre',10,'normal')).grid(row=0,column=1)
            find_btn_1=tk.Button(find_data_1,text = 'Find', command = find_main_1).grid(row=0,column=2)
            Product_id_label = tk.Label(find_data_1, text = 'Product ID', font=('calibre',10, 'bold')).grid(row=1,column=0)
            Product_id_entry = tk.Entry(find_data_1,textvariable = Pid_1, font=('calibre',10,'normal')).grid(row=1,column=1)
            find_btn_2=tk.Button(find_data_1,text = 'Find', command = find_main_2).grid(row=1,column=2)
            Product_name_label = tk.Label(find_data_1, text = 'Product Name', font=('calibre',10, 'bold')).grid(row=2,column=0)
            Product_name_entry = tk.Entry(find_data_1,textvariable = Pname_1, font=('calibre',10,'normal')).grid(row=2,column=1)
            find_btn_3=tk.Button(find_data_1,text = 'Find', command = find_main_3).grid(row=2,column=2)
            Sold_label = tk.Label(find_data_1, text = 'Sold', font=('calibre',10, 'bold')).grid(row=3,column=0)
            Sold_entry = tk.Entry(find_data_1,textvariable = Sold_1, font=('calibre',10,'normal')).grid(row=3,column=1)
            find_btn_4=tk.Button(find_data_1,text = 'Find', command = find_main_4).grid(row=3,column=2)
            Remaining_label = tk.Label(find_data_1, text = 'Remaining', font=('calibre',10, 'bold')).grid(row=4,column=0)
            Remaining_entry = tk.Entry(find_data_1,textvariable = Rem_1, font=('calibre',10,'normal')).grid(row=4,column=1)
            find_btn_5=tk.Button(find_data_1,text = 'Find', command = find_main_5).grid(row=4,column=2)
            Defective_label = tk.Label(find_data_1, text = 'Defective', font=('calibre',10, 'bold')).grid(row=5,column=0)
            Defective_entry = tk.Entry(find_data_1,textvariable = Def_1, font=('calibre',10,'normal')).grid(row=5,column=1)
            find_btn_6=tk.Button(find_data_1,text = 'Find', command = find_main_6).grid(row=5,column=2)
            Total_label = tk.Label(find_data_1, text = 'Total', font = ('calibre',10,'bold')).grid(row=6,column=0)
            Total_entry=tk.Entry(find_data_1, textvariable = Total_1, font = ('calibre',10,'normal')).grid(row=6,column=1)
            find_btn_7=tk.Button(find_data_1,text = 'Find', command = find_main_7).grid(row=6,column=2)
            ind_btn_8=tk.Button(find_data_1,text = 'Find', command = find_main_8).grid(row=7,column=1)
            # Add a Treeview widget
            treev = ttk.Treeview(find_data_1)
            treev.place(x=350,y=0)
            treev["columns"] = ("_id", "Product Id","Product Name","Sold","Remaining","Defective","Total")
            
            # Defining heading
            treev['show'] = 'headings'
            
            # Assigning the width and anchor to  the
            # respective columns
            treev.column("_id",anchor=CENTER, width=80)
            treev.column("Product Id",anchor=CENTER, width=80)
            treev.column("Product Name",anchor=CENTER, width=80)
            treev.column("Sold",anchor=CENTER, width=80)
            treev.column("Remaining",anchor=CENTER, width=80)
            treev.column("Defective",anchor=CENTER, width=80)
            treev.column("Total",anchor=CENTER, width=80)
            
            # Assigning the heading names to the
            # respective columns
            treev.heading("_id",text="Serial no",anchor=CENTER)
            treev.heading("Product Id",text="Product Id",anchor=CENTER)
            treev.heading("Product Name",text="Product Name",anchor=CENTER)
            treev.heading("Sold",text="Sold",anchor=CENTER)
            treev.heading("Remaining",text="Remaining",anchor=CENTER)
            treev.heading("Defective",text="Defective",anchor=CENTER)
            treev.heading("Total",text="Total",anchor=CENTER)
            find_data_1.mainloop()
#login window    
id_label = tk.Label(root, text = 'ID', font=('calibre',10, 'bold')).grid(row=0,column=0)
id_entry = tk.Entry(root,textvariable = id_var, font=('calibre',10,'normal')).grid(row=0,column=1)
passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold')).grid(row=1,column=0)
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*').grid(row=1,column=1)
sub_btn=tk.Button(root,text = 'Connect to Database', command = submit).grid(row=2,column=1)

root.mainloop()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
