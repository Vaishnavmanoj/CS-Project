from tkinter import *
from tkinter import ttk
import random
import time
import datetime
import tkinter.messagebox
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background='powder blue')

        

        cmbNameTablets=StringVar() 
        Ref = StringVar() 
        Dose =StringVar() 
        NumberTablets=StringVar() 
        Lot=StringVar() 
        IssuedDate=StringVar() 
        ExpDate=StringVar() 
        DailyDose=StringVar() 
        PossibleSideEffects=StringVar() 
        Furtherinformation=StringVar() 
        StorageAdvice=StringVar() 
        DrivingUsingMachines=StringVar() 
        HowtoUseMedication=StringVar() 
        PatientID=StringVar()
        NHSNumber=StringVar() 
        PatientName=StringVar() 
        DateofBirth=StringVar() 
        PatientAddress=StringVar() 
        Prescription=StringVar()
        #=======================Function mdeclaration=================

        def iExit():
            iExit=tkinter.messagebox.askyesno("Hospital Management System","Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return
        
        def iPrescription():

            return

        def iReceipt():

            return

        def iDelete():

            cmbNameTablets.set("") 
            self.cboNameTablet.current(0)
            Ref.set("") 
            Dose.set("") 
            NumberTablets.set("") 
            Lot.set("")
            IssuedDate.set("") 
            ExpDate.set("") 
            DailyDose.set("")
            PossibleSideEffects.set("")
            Furtherinformation.set("") 
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("")
            PatientID.set("")
            NHSNumber.set("") 
            PatientName.set("") 
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)

            return

        def iReset():

            cmbNameTablets.set("")
            self.cboNameTablet.current(0)  
            Ref.set("") 
            Dose.set("") 
            NumberTablets.set("") 
            Lot.set("")
            IssuedDate.set("") 
            ExpDate.set("") 
            DailyDose.set("")
            PossibleSideEffects.set("")
            Furtherinformation.set("") 
            StorageAdvice.set("")
            DrivingUsingMachines.set("")
            HowtoUseMedication.set("")
            PatientID.set("")
            NHSNumber.set("") 
            PatientName.set("") 
            DateofBirth.set("")
            PatientAddress.set("")
            self.txtPrescription.delete("1.0",END)
            self.txtFrameDetail.delete("1.0",END)

            return
         
    
        #============================Frame============================
        MainFrame=Frame(self.root)
        MainFrame.grid()

        TitleFrame= Frame(MainFrame, bd=20, width=1350, padx=2, pady=40, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle=Label(TitleFrame,font=('arial',40,'bold'), text='Hospital Mangament Systems',padx=2, pady=4)
        self.lblTitle.grid()

        FrameDetail=Frame(MainFrame,bd=20,width=1350,height=100,padx=2, pady=40,relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame=Frame(MainFrame,bd=20,width=1350,height=50,padx=2, pady=40,relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame=Frame(MainFrame,bd=20,width=1350,height=400,padx=2, pady=40,relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT=Frame(DataFrame,bd=10,width=800,height=400,padx=2, pady=40,relief=RIDGE)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT=Frame(DataFrame,bd=10,width=450,height=400,padx=2, pady=40,relief=RIDGE)
        DataFrameRIGHT.pack(side=RIGHT)


        # ===================== DATAFRAMELEFT ===========================
        
        self.lblNameTablet=Label(DataFrameLEFT,font=('arial',12,'bold'), text='Name of Tablets:',padx=2, pady=4)
        self.lblNameTablet.grid(row=0,column=0,sticky=W)

        self.cboNameTablet=ttk.Combobox(DataFrameLEFT,textvariable=cmbNameTablets,state='readoly',font=('arial',12,'bold'),width=20)

        self.cboNameTablet['value']=('','Ibuprofen','Co-codamol','Paracetamol','Amlodipine')
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=0,column=1)

        self.lblFurtherInfo=Label(DataFrameLEFT,font=('arial',12,'bold'), text='Further Information:',padx=2, pady=4)
        self.lblFurtherInfo.grid(row=0,column=2,sticky=W)
        self.txtFurtherInfo=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable = Furtherinformation, width=25)
        self.txtFurtherInfo.grid(row=0,column=3)

        self.lblRef=Label(DataFrameLEFT,font=('arial',12,'bold'), text='Reference No:',padx=2, pady=4)
        self.lblRef.grid(row=1,column=0,sticky=W)
        self.txtRef=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable = Ref, width=25)
        self.txtRef.grid(row=1,column=1)

        self.lblStorage=Label(DataFrameLEFT,font=('arial',12,'bold'), text='Storage Advice:',padx=2, pady=4)
        self.lblStorage.grid(row=1,column=2,sticky=W)
        self.txtStorage=Entry(DataFrameLEFT,font=('arial',12,'bold'),textvariable = StorageAdvice, width=25)
        self.txtStorage.grid(row=1,column=3)

        self.lblNoOfTablets = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="No of Tablets: ", padx=2, pady=4)
        self.lblNoOfTablets.grid(row=3, column=0, sticky=W)
        self.txtNoOftablets = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable = NumberTablets, width=25)
        self.txtNoOftablets.grid(row=3, column=1)

        self.lblUseMedication = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Driving Machines: ", padx=2, pady=4)
        self.lblUseMedication.grid(row=3, column=2, sticky=W)
        self.txtUseMedication = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable = HowtoUseMedication, width=25)
        self.txtUseMedication.grid(row=3, column=3)

        self.lblLot = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Lot: ", padx=2, pady=4)
        self.lblLot.grid(row=4, column=0, sticky=W)
        self.txtLot = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable = Lot, width=25)
        self.txtLot.grid(row=4, column=1)

        self.lblPatientID = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Patient ID: ", padx=2, pady=4)
        self.lblPatientID.grid(row=4, column=2, sticky=W)
        self.txtPatientID = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable = PatientID, width=25)
        self.txtPatientID.grid(row=4, column=3)

        self.lblIssuedDate = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Issued Date: ", padx=2, pady=4)
        self.lblIssuedDate.grid(row=5, column=0, sticky=W)
        self.txtIssuedDate = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable = IssuedDate, width=25)
        self.txtIssuedDate.grid(row=5, column=1)

        self.lblNHSNumber = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="NHS Number: ", padx=2, pady=4)
        self.lblNHSNumber.grid(row=5, column=2, sticky=W)
        self.txtNHSNumber = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable = NHSNumber, width=25)
        self.txtNHSNumber.grid(row=5, column=3)

        self.lblNHSNumber = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Exp Date: ", padx=2, pady=4)
        self.lblNHSNumber.grid(row=6, column=0, sticky=W)
        self.txtNHSNumber = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable = ExpDate, width=25)
        self.txtNHSNumber.grid(row=6, column=1)

        self.lblNHSNumber = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Patient Name: ", padx=2, pady=4)
        self.lblNHSNumber.grid(row=6, column=2, sticky=W)
        self.txtNHSNumber = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable =PatientName , width=25)
        self.txtNHSNumber.grid(row=6, column=3)

        self.lblNHSNumber = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Daily Dose: ", padx=2, pady=4)
        self.lblNHSNumber.grid(row=7, column=0, sticky=W)
        self.txtNHSNumber = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable = DailyDose, width=25)
        self.txtNHSNumber.grid(row=7, column=1)

        self.lblNHSNumber = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Date of Birth: ", padx=2, pady=4)
        self.lblNHSNumber.grid(row=7, column=2, sticky=W)
        self.txtNHSNumber = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable = DateofBirth, width=25)
        self.txtNHSNumber.grid(row=7, column=3)

        self.lblNHSNumber = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Side Effects: ", padx=2, pady=4)
        self.lblNHSNumber.grid(row=8, column=0, sticky=W)
        self.txtNHSNumber = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable = PossibleSideEffects, width=25)
        self.txtNHSNumber.grid(row=8, column=1)

        self.lblNHSNumber = Label(DataFrameLEFT, font=("arial", 12, "bold"), text="Patient Address: ", padx=2, pady=4)
        self.lblNHSNumber.grid(row=8, column=2, sticky=W)
        self.txtNHSNumber = Entry(DataFrameLEFT, font=("arial", 12, "bold"), textvariable = PatientAddress, width=25)
        self.txtNHSNumber.grid(row=8, column=3)

        # ===============Dataframe Right====================
        self.txtPrescription =Text(DataFrameRIGHT, font=("arial", 12, "bold"), width=43,height=14, padx=2, pady=4)
        self.txtPrescription.grid(row=0, column=0)

        # ===============ButtonFrame====================
        self.btnPrescription=Button(ButtonFrame,text='Prescription',font=('arial',12,'bold'),width=24,bd=4,command=iPrescription)
        self.btnPrescription.grid(row=0,column=0)
        self.btnReceipt=Button(ButtonFrame,text='Receipt',font=('arial',12,'bold'),width=24,bd=4,command=iReceipt)
        self.btnReceipt.grid(row=0,column=1)
        self.btnDelete=Button(ButtonFrame,text='Delete',font=('arial',12,'bold'),width=24,bd=4,command=iDelete)
        self.btnDelete.grid(row=0,column=2)
        self.btnReset=Button(ButtonFrame,text='Reset',font=('arial',12,'bold'),width=24,bd=4,command=iReset)
        self.btnReset.grid(row=0,column=3)
        self.btnExit=Button(ButtonFrame,text='Exit',font=('arial',12,'bold'),width=24,bd=4, command=iExit)
        self.btnExit.grid(row=0,column=4)

        # ===============FrameDetail====================
        self.lblLabel=Label(FrameDetail,font=('arial', 10, 'bold'),pady=8, 
        text="Name of Tablets\tReference No.\t Dosage\t No. of Tablets\t Lot\t Issued Date\t Exp. Date\tDaily Dose\tStorage Advice\tNHS Number\t Patient's Name\t DOB\t Address",)
        self.lblLabel.grid(row=0, column=0)
        
        self.txtFrameDetail =Text(FrameDetail, font=("arial", 12, "bold"), width=141,height=4, padx=2, pady=4)
        self.txtFrameDetail.grid(row=1, column=0)
        



        
if __name__ =='__main__':
    root=Tk()
    application=Hospital(root)
    root.mainloop()
