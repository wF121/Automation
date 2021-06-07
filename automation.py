from tkinter import *
from tkinter import messagebox
import sqlite3




root = Tk()

root.title('Automation')




#lists

car =  [19225735, '611926', '2018', 'Hyundai', 'Sonata', 'White', 'Recon', '$25,000', 'Sedan', '32,123']  
car1 = [19886578, '012345', '2016', 'Acura', 'MDX', 'White', 'Recon', '$20,500', 'SUV', '62,356']
car2 = [19579858, '018557', '2012', 'Honda', 'Pilot', 'Black', 'Saleable', '$$16,998', 'SUV', 107,000]
car3 = [19886500, '162824', '2016', 'Dodge', 'Challenger', 'BLack', 'Saleable', '$21,998', 'Sports', '85,000']
car4 = [19673820, '218339', '2014', 'Dodge', 'Journey', 'Orange', 'Saleable', '$13,998', 'Mini-Van', '53,000']
car5 = [19799631, '553257', '2018', 'Nissan', 'Rogue', 'Grey', 'Recon', '$16,998', 'SUV','33,272']
car6 = [19886198, '512511', '2019', 'Infiniti', 'Q50', 'Silver', 'Whole Sale', '$25,000', 'Sedan', '29,982']
car7 = [19579572, '154326', '2012', 'Mercedes-Benz', 'CL550', 'Black', 'Whole Sale', '$25,000', 'Coupe', '78,525']
car8 = [19470280, '125468', '2017', 'Ford', 'Focus RS', 'Grey', 'In-Transit', '$36,000', 'Sports', '11,000']
car9 = [19579750, 'A19496', '2011', 'Ford', 'Escape', 'Red', 'In-Transit', '9,998', 'SUV', '119,000']

#funtions
def search():
    x = int(stockNumber.get()) 
    if (x == car[0]):
        vinNumber.delete(0, END)
        vinNumber.insert(0, car[1])
        year.delete(0, END)#
        year.insert(0, car[2])
        make.delete(0, END)#
        make.insert(0, car[3])
        model.delete(0, END)#
        model.insert(0, car[4])
        color.delete(0, END)#
        color.insert(0, car[5])
        status.delete(0, END)#
        status.insert(0, str(car[6]))
        price.delete(0, END)#
        price.insert(0, car[7])
        size.delete(0, END)#
        size.insert(0, car[8])
        mileage.delete(0, END)#
        mileage.insert(0, str(car[9]))
    if  (x == car1[0]):
        vinNumber.delete(0, END)#
        vinNumber.insert(0, car1[1])
        year.delete(0, END)#
        year.insert(0, car1[2])
        make.delete(0, END)#
        make.insert(0, car1[3])
        model.delete(0, END)#
        model.insert(0, car1[4])
        color.delete(0, END)#
        color.insert(0, car1[5])
        status.delete(0, END)#
        status.insert(0, str(car1[6]))
        price.delete(0, END)#
        price.insert(0, car1[7])
        size.delete(0, END)#
        size.insert(0, car1[8])
        mileage.delete(0, END)#
        mileage.insert(0, str(car1[9]))
    if  (x == car2[0]):
        vinNumber.delete(0, END)#
        vinNumber.insert(0, car2[1])
        year.delete(0, END)#
        year.insert(0, car2[2])
        make.delete(0, END)#
        make.insert(0, car2[3])
        model.delete(0, END)#
        model.insert(0, car2[4])
        color.delete(0, END)#
        color.insert(0, car2[5])
        status.delete(0, END)#
        status.insert(0, str(car2[6]))
        price.delete(0, END)#
        price.insert(0, car2[7])
        size.delete(0, END)#
        size.insert(0, car2[8])
        mileage.delete(0, END)#
        mileage.insert(0, str(car2[9]))
    if  (x == car3[0]):
        vinNumber.delete(0, END)#
        vinNumber.insert(0, car3[1])
        year.delete(0, END)#
        year.insert(0, car3[2])
        make.delete(0, END)#
        make.insert(0, car3[3])
        model.delete(0, END)#
        model.insert(0, car3[4])
        color.delete(0, END)#
        color.insert(0, car3[5])
        status.delete(0, END)#
        status.insert(0, str(car3[6]))
        price.delete(0, END)#
        price.insert(0, car3[7])
        size.delete(0, END)#
        size.insert(0, car3[8])
        mileage.delete(0, END)#
        mileage.insert(0, str(car3[9]))
    if  (x == car4[0]):
        vinNumber.delete(0, END)#
        vinNumber.insert(0, car4[1])
        year.delete(0, END)#
        year.insert(0, car4[2])
        make.delete(0, END)#
        make.insert(0, car4[3])
        model.delete(0, END)#
        model.insert(0, car4[4])
        color.delete(0, END)#
        color.insert(0, car4[5])
        status.delete(0, END)#
        status.insert(0, str(car4[6]))
        price.delete(0, END)#
        price.insert(0, car4[7])
        size.delete(0, END)#
        size.insert(0, car4[8])
        mileage.delete(0, END)#
        mileage.insert(0, str(car4[9]))
    if  (x == car5[0]):
        vinNumber.delete(0, END)#
        vinNumber.insert(0, car5[1])
        year.delete(0, END)#
        year.insert(0, car5[2])
        make.delete(0, END)#
        make.insert(0, car5[3])
        model.delete(0, END)#
        model.insert(0, car5[4])
        color.delete(0, END)#
        color.insert(0, car5[5])
        status.delete(0, END)#
        status.insert(0, str(car5[6]))
        price.delete(0, END)#
        price.insert(0, car5[7])
        size.delete(0, END)#
        size.insert(0, car5[8])
        mileage.delete(0, END)#
        mileage.insert(0, str(car5[9]))
    if  (x == car6[0]):
        vinNumber.delete(0, END)#
        vinNumber.insert(0, car3[1])
        year.delete(0, END)#
        year.insert(0, car6[2])
        make.delete(0, END)#
        make.insert(0, car6[3])
        model.delete(0, END)#
        model.insert(0, car6[4])
        color.delete(0, END)#
        color.insert(0, car6[5])
        status.delete(0, END)#
        status.insert(0, str(car6[6]))
        price.delete(0, END)#
        price.insert(0, car6[7])
        size.delete(0, END)#
        size.insert(0, car6[8])
        mileage.delete(0, END)#
        mileage.insert(0, str(car6[9]))
    if  (x == car7[0]):
        vinNumber.delete(0, END)#
        vinNumber.insert(0, car7[1])
        year.delete(0, END)#
        year.insert(0, car7[2])
        make.delete(0, END)#
        make.insert(0, car7[3])
        model.delete(0, END)#
        model.insert(0, car7[4])
        color.delete(0, END)#
        color.insert(0, car7[5])
        status.delete(0, END)#
        status.insert(0, str(car7[6]))
        price.delete(0, END)#
        price.insert(0, car7[7])
        size.delete(0, END)#
        size.insert(0, car7[8])
        mileage.delete(0, END)#
        mileage.insert(0, str(car7[9]))
    if  (x == car8[0]):
        vinNumber.delete(0, END)#
        vinNumber.insert(0, car8[1])
        year.delete(0, END)#
        year.insert(0, car8[2])
        make.delete(0, END)#
        make.insert(0, car8[3])
        model.delete(0, END)#
        model.insert(0, car8[4])
        color.delete(0, END)#
        color.insert(0, car8[5])
        status.delete(0, END)#
        status.insert(0, str(car8[6]))
        price.delete(0, END)#
        price.insert(0, car8[7])
        size.delete(0, END)#
        size.insert(0, car8[8])
        mileage.delete(0, END)#
        mileage.insert(0, str(car8[9]))
    if  (x == car9[0]):
        vinNumber.delete(0, END)#
        vinNumber.insert(0, car9[1])
        year.delete(0, END)#
        year.insert(0, car9[2])
        make.delete(0, END)#
        make.insert(0, car9[3])
        model.delete(0, END)#
        model.insert(0, car9[4])
        color.delete(0, END)#
        color.insert(0, car9[5])
        status.delete(0, END)#
        status.insert(0, str(car9[6]))
        price.delete(0, END)#
        price.insert(0, car9[7])
        size.delete(0, END)#
        size.insert(0, car9[8])
        mileage.delete(0, END)#
        mileage.insert(0, str(car9[9]))
     
    
    
    

#fqc----------------------------------------------------
def change():
  x = int(stockNumber.get())
  if (x == car8[0]):
    status.delete(0, END)
    status.insert(0, "Recon")
    car8[6] = status.get()
  if (x == car9[0]):
    status.delete(0, END)
    status.insert(0, "Recon")
    car9[6] = status.get()

def fqcc():
  x = int(stockNumber.get())
  if (x == car[0]):
      status.delete(0, END)
      status.insert(0, str("Saleable"))
      car[6] = status.get()
  if (x == car1[0]):
      status.delete(0, END)
      status.insert(0, str("Saleable"))
      car1[6] = status.get()
  if (x == car5[0]):
      status.delete(0, END)
      status.insert(0, str("Saleable"))
      car5[6] = str(status.get())
  if (x == car8[0]):
      status.delete(0, END)
      status.insert(0, str("Saleable"))
      car8[6] = status.get()
  if (x == car9[0]):
      status.delete(0, END)
      status.insert(0, str("Saleable"))
      car9[6] = status.get()


  


def fqc():
   
    r = status.get()
    if  (r == "Recon"):
        top = Toplevel()
        top.title('FQC')
        lbl = Label(top, text="Did this vehicle pass fqc")
        lbl.grid(row=1, column=1)
        #Radiobutton=(top,"Yes", value=1).grid(row=1, column=3)
        #Radiobutton=(top, text="No", value=2).grid(row=2, column=3)
        yesb = Button(top,text = 'Yes', command=fqcc).grid(row=2, column=1)
        nob = Button(top, text='No', command=top.destroy).grid(row=2, column=2)
    else:
      messagebox.showwarning( message='No FQC in system')

        

def recieve():
  
  r = status.get()
  if (r == "In-Transit"):
    change()
  else:
    messagebox.showwarning(message="Vehicle not to be Recieved")
       
            

        
        
        
        
        
    

      



#text boxes --------------------------------------------
stockNumber = Entry(root, width=30)
stockNumber.grid(row=0, column=1, padx=20)

vinNumber = Entry(root, width=30)
vinNumber.grid(row=1, column=1, padx=20)

year = Entry(root, width=30)
year.grid(row=2, column=1, padx=20)

make = Entry(root, width=30)
make.grid(row=3, column=1, padx=20)

model = Entry(root, width=30)
model.grid(row=4, column=1, padx=20)

color = Entry(root, width=30)
color.grid(row=5, column=1, padx=20)

status = Entry(root, width=30)
status.grid(row=6, column=1, padx=20)

price = Entry(root, width=30)
price.grid(row=7, column=1, padx=20)

size = Entry(root, width=30)
size.grid(row=8, column=1, padx=20)

mileage = Entry(root, width=30)
mileage.grid(row=9, column=1, padx=20)

enter = Button(root, text = "Search", padx=40, pady=20, command=search)
enter.grid(row=10, column=0)


fqc = Button(root, text = "FQC", padx=40, pady=20, command=fqc)
fqc.grid(row=10, column=1)

recieve = Button(root, text = "Recieve", padx=40, pady=20,command=recieve)
recieve.grid(row=10, column=2)
#labels ------------------------------------------------
snLabel = Label(root, text="Stock Number")
snLabel.grid(row=0, column=0)

vnLabel = Label(root, text="Vin Number")
vnLabel.grid(row=1, column=0)

yearLabel = Label(root, text="Year")
yearLabel.grid(row=2, column=0)

makeLabel = Label(root, text="Make")
makeLabel.grid(row=3, column=0)

modelLabel = Label(root, text="Model")
modelLabel.grid(row=4, column=0)

colorLabel = Label(root, text="Color")
colorLabel.grid(row=5, column=0)

statusLabel = Label(root, text="Status")
statusLabel.grid(row=6, column=0)

priceLabel = Label(root, text="Price")
priceLabel.grid(row=7, column=0)

sizeLabel = Label(root, text="Size")
sizeLabel.grid(row=8, column=0)

mileLabel = Label(root, text="Mileage")
mileLabel.grid(row=9, column=0)






#commit changes
#conn.commit()


#close connection
#conn.close()

#root.mainloop()
