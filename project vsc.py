from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="Hospital Management System",
                         fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # =============Dataframe========
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataFrameLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                   font=("times new roman", 12, "bold"), text="Patient Information")
        DataFrameLeft.place(x=0, y=5, width=980, height=350)

        DataFrameRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                                    font=("times new roman", 12, "bold"), text="Prescription")
        DataFrameRight.place(x=990, y=5, width=460, height=350)

        # ================ buttons frame============
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # ================ Details frame============
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # =============================== DataFrameLeft

        lblNameTablet = Label(DataFrameLeft, text="Names of Tablet", font=(
            "times new roman", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)

        comNameTablet = ttk.Combobox(DataFrameLeft, font=(
            "times new roman", 12, "bold"), width=33)
        comNameTablet["values"] = (
            "Nice", "Corona Vaccine", "Acetaminophen", "Adderall", "Amlodipine", "Ativan")
        comNameTablet.grid(row=0, column=1)

        lblref = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Refence No:", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=1, column=1)
        lbDose = Label(DataFrameLeft, font=("arial", 12, "bold"),
                       text="Dose: ", padx=2, pady=4)
        lbDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=35)
        txtDose.grid(row=2, column=1)

        lblNoOfTablets = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="No of Tablets: : ", padx=2, pady=6)
        lblNoOfTablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=3, column=1)

        lblNoOfTablets = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Lot: ", padx=2, pady=6)
        lblNoOfTablets.grid(row=4, column=0, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=4, column=1)

        lblNoOfTablets = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Issue Date: ", padx=2, pady=6)
        lblNoOfTablets.grid(row=5, column=0, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=5, column=1)

        lblNoOfTablets = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Expiry Date: ", padx=2, pady=6)
        lblNoOfTablets.grid(row=6, column=0, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=6, column=1)

        lblNoOfTablets = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Daily Dose: ", padx=2, pady=6)
        lblNoOfTablets.grid(row=7, column=0, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=7, column=1)

        lblNoOfTablets = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Side Effect: ", padx=2, pady=6)
        lblNoOfTablets.grid(row=8, column=0, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=8, column=1)

        lblNoOfTablets = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Further Information: ", padx=2, pady=6)
        lblNoOfTablets.grid(row=0, column=2, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=0, column=3)

        lblNoOfTablets = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Blood Pressure: ", padx=2, pady=6)
        lblNoOfTablets.grid(row=1, column=2, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=1, column=3)

        lblNoOfTablets = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Storage Advice: ", padx=2, pady=6)
        lblNoOfTablets.grid(row=2, column=2, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=2, column=3)

        lblNoOfTablets = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Medication: ", padx=2, pady=6)
        lblNoOfTablets.grid(row=3, column=2, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=3, column=3)

        lblNoOfTablets = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Patient ID: ", padx=2, pady=6)
        lblNoOfTablets.grid(row=4, column=2, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=4, column=3)

        lblNoOfTablets = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="NHS Number: ", padx=2, pady=6)
        lblNoOfTablets.grid(row=5, column=2, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=5, column=3)

        lblNoOfTablets = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Patient Name: ", padx=2, pady=6)
        lblNoOfTablets.grid(row=6, column=2, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=6, column=3)

        lblNoOfTablets = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Date of Birth: ", padx=2, pady=6)
        lblNoOfTablets.grid(row=7, column=2, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=7, column=3)

        lblNoOfTablets = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Patient Address: ", padx=2, pady=6)
        lblNoOfTablets.grid(row=8, column=2, sticky=W)
        txtNoOftablets = Entry(DataFrameLeft, font=(
            "arial", 13, "bold"), width=35)
        txtNoOftablets.grid(row=8, column=3)

        # ===============Dataframe Right====================
        self.txtPrescription = Text(DataFrameRight, font=(
            "arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ======================Buttons================
        btnPrescription = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=(
            "arial", 12, "bold"), width=23, height=16, padx=2, pady=6)
        btnPrescription.grid(row=0, column=0)

        123456

root = Tk()
ob = Hospital(root)
root.mainloop()
