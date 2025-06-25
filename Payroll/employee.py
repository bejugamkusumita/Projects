from tkinter import *
from tkinter import messagebox
import time
import pymysql
import os


# import tempfile
class EmployeeSystem:
    def __init__(self, root):

        self.root = root
        self.root.title("Employee Payroll")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        title = Label(self.root, text="Employee payroll", font=(" Playfair Display", 30, "bold"), bg="orange",
                      fg="white", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        # -----------------------frame 1-------------------------------
        # ------Variables----
        self.var_emp_code = StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_hr_location = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_proof_id = StringVar()
        self.var_contact = StringVar()
        self.var_status = StringVar()
        self.var_experience = StringVar()
        # Variables fram2
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_salary = StringVar()
        self.var_t_days = StringVar()
        self.var_absent = StringVar()
        self.var_medical = StringVar()
        self.var_pf = StringVar()
        self.var_convence = StringVar()
        self.var_netsal = StringVar()
        Frame1 = Frame(self.root, bd=2, relief=RIDGE, bg="#FEF9F2")
        Frame1.place(x=10, y=70, width=750, height=620)
        title2 = Label(Frame1, text="Employee Details", font=("times new roman", 20), bg="lightgray", fg="#B03052",
                       anchor="w", padx=10).place(x=0, y=0, relwidth=1)
        lb1_code = Label(Frame1, text="Employee Id", font=("Georgia", 20), bg="white", fg="#131842").place(x=10, y=70)
        txt_code = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_emp_code, bg="#D4F6FF",
                         fg="black").place(x=170, y=75, width=200)
        btn_search = Button(Frame1, text="Search", command=self.search, font=("times new roman", 20), bg="#58D68D",
                            fg="#FFFFFF").place(x=460, y=73, height=30)
        # row1
        lb1_designation = Label(Frame1, text="Designation", font=("times new roman", 20), bg="white",
                                fg="#131842").place(x=10, y=120)
        txt_designation = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_designation, bg="#D4F6FF",
                                fg="#131842").place(x=170, y=125, width=200)
        lb1_dob = Label(Frame1, text="D.O.B", font=("times new roman", 20), bg="white", fg="#131842").place(x=390,
                                                                                                            y=120,
                                                                                                            width=100)
        txt_dob = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_dob, bg="#D4F6FF",
                        fg="black").place(x=520, y=125)
        # row2
        lb1_Name = Label(Frame1, text="Name", font=("times new roman", 20), bg="white", fg="#131842").place(x=10, y=170)
        txt_Name = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_name, bg="#D4F6FF",
                         fg="black").place(x=170, y=175, width=200)

        lb1_doj = Label(Frame1, text="D.O.J", font=("times new roman", 20), bg="white", fg="#131842").place(x=390,
                                                                                                            y=170)
        txt_doj = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_doj, bg="#D4F6FF",
                        fg="black").place(x=520, y=175)
        # row 3
        lb1_age = Label(Frame1, text="Age", font=("times new roman", 20), bg="white", fg="#131842").place(x=10, y=220)
        txt_age = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_age, bg="#D4F6FF",
                        fg="black").place(x=170, y=225, width=200)
        lb1_experience = Label(Frame1, text="Experience", font=("times new roman", 20), bg="white", fg="#131842").place(
            x=390, y=220)
        txt_experience = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_experience, bg="#D4F6FF",
                               fg="black").place(x=520, y=225)
        # row 4

        lb1_gender = Label(Frame1, text="Gender", font=("times new roman", 20), bg="white", fg="#131842").place(x=10,
                                                                                                                y=270)
        txt_gender = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_gender, bg="#D4F6FF",
                           fg="black").place(x=170, y=275, width=200)
        lb1_proof = Label(Frame1, text="Proof Id", font=("times new roman", 20), bg="white", fg="#131842").place(x=390,
                                                                                                                 y=270)
        txt_proof = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_proof_id, bg="#D4F6FF",
                          fg="black").place(x=520, y=275)
        # row 5
        lb1_email = Label(Frame1, text="Email", font=("times new roman", 20), bg="white", fg="#131842").place(x=10,
                                                                                                              y=320)
        txt_email = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_email, bg="#D4F6FF",
                          fg="black").place(x=170, y=325, width=200)
        lb1_contact = Label(Frame1, text="Contact", font=("times new roman", 20), bg="white", fg="#131842").place(x=390,
                                                                                                                  y=320)
        txt_contact = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_contact, bg="#D4F6FF",
                            fg="black").place(x=520, y=325)
        # row 6
        lb1_hired = Label(Frame1, text="Hired Location", font=("times new roman", 18), bg="white", fg="#131842").place(
            x=10, y=373)
        txt_hired = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_hr_location, bg="#D4F6FF",
                          fg="black").place(x=170, y=375, width=200)
        lb1_status = Label(Frame1, text="Status", font=("times new roman", 20), bg="white", fg="#131842").place(x=390,
                                                                                                                y=370)
        txt_status = Entry(Frame1, font=("times new roman", 15), textvariable=self.var_status, bg="#D4F6FF",
                           fg="black").place(x=520, y=375)
        # row 7
        lb1_address = Label(Frame1, text="Address", font=("times new roman", 18), bg="white", fg="#131842").place(x=10,
                                                                                                                  y=423)
        self.txt_address = Text(Frame1, font=("times new roman", 15), bg="#D4F6FF", fg="black")
        self.txt_address.place(x=170, y=425, width=550, height=180)
        # -------------------------frame 2----------------------------------
        Frame2 = Frame(self.root, bd=3, relief=RIDGE, bg="#FEF9F2")
        Frame2.place(x=770, y=70, width=580, height=300)
        title3 = Label(Frame2, text="Employee Salary", font=("times new roman", 20), bg="lightgray", fg="#B03052",
                       anchor="w", padx=10).place(x=0, y=0, relwidth=1)
        # row1
        lb1_month = Label(Frame2, text="Month", font=("times new roman", 18), bg="white", fg="#131842").place(x=10,
                                                                                                              y=60)
        txt_month = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_month, bg="#D4F6FF",
                          fg="black").place(x=90, y=62, width=100)

        lb1_year = Label(Frame2, text="Year", font=("times new roman", 18), bg="white", fg="#131842").place(x=210, y=60)
        txt_year = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_year, bg="#D4F6FF",
                         fg="black").place(x=270, y=62, width=100)
        lb1_salary = Label(Frame2, text=" B.Salary", font=("times new roman", 18), bg="white", fg="#131842").place(
            x=370, y=60)
        txt_salary = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_salary, bg="#D4F6FF",
                           fg="black").place(x=470, y=62, width=100)

        # row2
        lb1_days = Label(Frame2, text="Total Days", font=("times new roman", 18), bg="white", fg="#131842").place(x=10,
                                                                                                                  y=120)
        txt_days = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_t_days, bg="#D4F6FF",
                         fg="black").place(x=170, y=125, width=100)
        lb1_absent = Label(Frame2, text="absent", font=("times new roman", 18), bg="white", fg="#131842").place(x=300,
                                                                                                                y=120)
        txt_absent = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_absent, bg="#D4F6FF",
                           fg="black").place(x=420, y=125, width=120)
        # row 3
        lb1_medical = Label(Frame2, text="Medical", font=("times new roman", 18), bg="white", fg="#131842").place(x=10,
                                                                                                                  y=150)
        txt_medical = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_medical, bg="#D4F6FF",
                            fg="black").place(x=170, y=155, width=100)
        lb1_pf = Label(Frame2, text="pf", font=("times new roman", 18), bg="white", fg="#131842").place(x=300, y=150)
        txt_pf = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_pf, bg="#D4F6FF", fg="black").place(
            x=420, y=155, width=120)
        # row 4
        lb1_convience = Label(Frame2, text="Convience", font=("times new roman", 20), bg="white", fg="#131842").place(
            x=10, y=180)
        txt_convience = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_convence, bg="#D4F6FF",
                              fg="black").place(x=170, y=185, width=100)
        lb1_net_sal = Label(Frame2, text="Net salary", font=("times new roman", 20), bg="white", fg="#131842").place(
            x=300, y=180)
        txt_net_sal = Entry(Frame2, font=("times new roman", 15), textvariable=self.var_netsal, bg="#D4F6FF",
                            fg="black").place(x=420, y=185, width="120")
        # buttons
        btn_cal = Button(Frame2, text="Calculate", command=self.calculate, font=("times new roman", 20), bg="orange",
                         fg="#FFFFFF").place(x=150, y=225, height=30, width=120)
        btn_save = Button(Frame2, text="Save", command=self.add, font=("times new roman", 20), bg="green",
                          fg="#FFFFFF").place(x=285, y=225, height=30, width=120)
        btn_clear = Button(Frame2, text="Clear", command=self.clear, font=("times new roman", 20), bg="grey",
                           fg="#FFFFFF").place(x=420, y=225, height=30, width=120)

        btn_update = Button(Frame2, text="Update", command=self.update, font=("times new roman", 20), bg="blue",
                            fg="#FFFFFF").place(x=150, y=260, height=30, width=160)
        btn_delete = Button(Frame2, text="Delete", command=self.delete, font=("times new roman", 20), bg="red",
                            fg="#FFFFFF").place(x=340, y=260, height=30, width=170)
        # btn_print = Button(, text='Print Receipt', command=self.show_receipt, font=("times new roman", 20),

        # bg="lightblue", fg="black").place(x=190, y=262, width=120, height=30)
        # frame 3
        Frame3 = Frame(self.root, bd=3, relief=RIDGE, bg="#FEF9F2")
        Frame3.place(x=770, y=380, width=580, height=310)
        # calci frame
        self.var_txt = StringVar()
        self.var_operator = ""

        def btn_click(num):
            self.var_operator = self.var_operator + str(num)
            self.var_txt.set(self.var_operator)

        def result():
            res = str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator = ''

        def clear(self):
            for var in [self.var_emp_code, self.var_designation, self.var_name,
                        self.var_age, self.var_gender, self.var_email, self.var_hr_location,
                        self.var_dob, self.var_doj, self.var_proof_id, self.var_contact,
                        self.var_status, self.var_experience, self.var_month, self.var_year,
                        self.var_salary, self.var_t_days, self.var_absent, self.var_medical,
                        self.var_pf, self.var_convence, self.var_netsal]:
                var.set("")
            self.txt_address.delete('1.0', END)

        # calci
        cal_Frame = Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        cal_Frame.place(x=2, y=2, width=210, height=302)
        txt_Result = Entry(cal_Frame, bg="light grey", textvariable=self.var_txt, font=("times new roman", 20, "bold"),
                           justify="right")
        txt_Result.place(x=0, y=0, relwidth=1, height=57)

        # row1
        btn_7 = Button(cal_Frame, text='7', command=lambda: btn_click(7), font=("times new roman", 15, "bold")).place(
            x=2, y=58, width=50, height=50)
        btn_8 = Button(cal_Frame, text='8', command=lambda: btn_click(8), font=("times new roman", 15, "bold")).place(
            x=53, y=58, width=50, height=50)
        btn_9 = Button(cal_Frame, text='9', command=lambda: btn_click(9), font=("times new roman", 15, "bold")).place(
            x=104, y=58, width=50, height=50)
        btn_d = Button(cal_Frame, text='/', command=lambda: btn_click('/'), font=("times new roman", 15, "bold")).place(
            x=155, y=58, width=50, height=50)
        # row2
        btn_4 = Button(cal_Frame, text='4', command=lambda: btn_click(4), font=("times new roman", 15, "bold")).place(
            x=2, y=109, width=50, height=50)
        btn_5 = Button(cal_Frame, text='5', command=lambda: btn_click(5), font=("times new roman", 15, "bold")).place(
            x=53, y=109, width=50, height=50)
        btn_6 = Button(cal_Frame, text='6', command=lambda: btn_click(6), font=("times new roman", 15, "bold")).place(
            x=104, y=109, width=50, height=50)
        btn_m = Button(cal_Frame, text='', command=lambda: btn_click(''), font=("times new roman", 15, "bold")).place(
            x=155, y=109, width=50, height=50)
        # row 3
        btn_1 = Button(cal_Frame, text='1', command=lambda: btn_click(1), font=("times new roman", 15, "bold")).place(
            x=2, y=161, width=50, height=50)
        btn_2 = Button(cal_Frame, text='2', command=lambda: btn_click(2), font=("times new roman", 15, "bold")).place(
            x=53, y=161, width=50, height=50)
        btn_3 = Button(cal_Frame, text='3', command=lambda: btn_click(3), font=("times new roman", 15, "bold")).place(
            x=104, y=161, width=50, height=50)
        btn_mi = Button(cal_Frame, text='-', command=lambda: btn_click('-'),
                        font=("times new roman", 15, "bold")).place(x=155, y=161, width=50, height=50)
        # row 4
        btn_0 = Button(cal_Frame, text='0', command=lambda: btn_click(0), font=("times new roman", 15, "bold")).place(
            x=2, y=213, width=50, height=50)
        btn_do = Button(cal_Frame, text='.', command=lambda: btn_click('.'),
                        font=("times new roman", 15, "bold")).place(x=53, y=213, width=50, height=50)
        btn_a = Button(cal_Frame, text='+', command=lambda: btn_click('+'), font=("times new roman", 15, "bold")).place(
            x=104, y=213, width=50, height=50)
        btn_e = Button(cal_Frame, text='=', command=result, font=("times new roman", 15, "bold")).place(x=155, y=213,
                                                                                                        width=50,
                                                                                                        height=50)
        btn_c = Button(cal_Frame, text='Clear', command=clear, font=("times new roman", 15, "bold")).place(x=0, y=263,
                                                                                                           width=205,
                                                                                                           height=37)
        # salary frame
        sal_Frame = Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        sal_Frame.place(x=210, y=2, width=360, height=301)
        title2 = Label(sal_Frame, text="Salary Reciept", font=("times new roman", 20), bg="lightgray", fg="#B03052",
                       anchor="w", padx=10).place(x=0, y=0, relwidth=1)
        sal_Frame2 = Frame(sal_Frame, bg="white", bd=2, relief=RIDGE)
        sal_Frame2.place(x=0, y=35, relwidth=1, height=230)

        def show_receipt(self):
            print("Generating receipt...")  # Debugging print
            if self.var_month.get() == '' or self.var_year.get() == '' or self.var_salary.get() == '' or self.var_t_days.get() == '':
                messagebox.showerror('Error', "All fields are required")
            else:
                self.calculate()
                new_sample = f''' \tCompany Name, XYZ\n\tAddress: Xyz, Floor 4
                 -----------------------------------------
                  Employee ID\t\t: {self.var_emp_code.get()}
                  Salary of\t\t: {self.var_month.get()}-{self.var_year.get()}
                  Generated on\t\t: {time.strftime("%d-%m-%Y")}
                 -----------------------------------------
                  Total days\t\t: {self.var_t_days.get()}
                  Total Present\t\t: {str(int(self.var_t_days.get()) - int(self.var_absent.get()))}
                  Total Absent\t\t: {self.var_absent.get()}
                  Convenience\t\t: Rs.{self.var_convence.get()}
                  Medical \t\t: Rs.{self.var_medical.get()}
                  PF\t\t: Rs.{self.var_pf.get()}
                  Gross Payment\t\t: Rs.{self.var_salary.get()}
                  Net Salary\t\t: Rs.{self.var_netsal.get()}
                 --------------------------------------------
                 This is a computer-generated slip, no signature required     
                                    '''

                self.txt_salary_recipt.delete("1.0", END)
                self.txt_salary_recipt.insert(END, new_sample)

        scroll_y = Scrollbar(sal_Frame2, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)
        self.txt_salary_recipt = Text(sal_Frame2, font=("times new roman", 15), bg="light yellow",
                                      yscrollcommand=scroll_y.set)
        self.txt_salary_recipt.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)

    # btn_print = Button(sal_Frame, text='print',command=self.print,font=("times new roman", 20),bg="lightblue",fg="black").place(x=190, y=262, width=120,height=30)
    def search(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="employee_payroll")
            cur = con.cursor()
            cur.execute("select * from employee where e_id=%s", (self.var_emp_code.get()))
            row = cur.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("Error", "employee id doesnot exist,try again with another id", parent=self.root)
            else:
                print(row)
            self.var_emp_code.set(row[0])
            self.var_designation.set(row[1])
            self.var_name.set(row[2])
            self.var_age.set(row[3])
            self.var_gender.set(row[4])
            self.var_email.set(row[5])
            self.var_hr_location.set(row[6])
            self.var_dob.set(row[7])
            self.var_doj.set(row[8])
            self.var_contact.set(row[9])
            self.var_experience.set(row[10])
            self.var_proof_id.set(row[11])
            self.var_status.set(row[12])
            self.txt_address.delete('1.0', END)
            self.txt_address.insert(END, row[22])

            # frame 2
            self.var_month.set(row[13])
            self.var_year.set(row[14])
            self.var_salary.set(row[15])
            self.var_t_days.set(row[16])
            self.var_pf.set(row[17])
            self.var_medical.set(row[18])
            self.var_convence.set(row[19])
            self.var_netsal.set(row[20])
            self.var_absent.set(row[21])


        except Exception as ex:
            messagebox.showerror("ERROR", f"Error due to:{ex}")
            # cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",)

    def clear(self):
        self.var_emp_code.set("")
        self.var_designation.set("")
        self.var_name.set("")
        self.var_age.set("")
        self.var_gender.set("")
        self.var_email.set("")
        self.var_hr_location.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_contact.set("")
        self.var_experience.set("")
        self.var_proof_id.set("")
        self.var_status.set("")
        self.txt_address.delete('1.0', END)

        # frame 2
        self.var_month.set("")
        self.var_year.set("")
        self.var_salary.set("")
        self.var_t_days.set("")
        self.var_pf.set("")
        self.var_medical.set("")
        self.var_convence.set("")
        self.var_netsal.set("")
        self.var_absent.set("")
        self.txt_salary_recipt.delete('1.0', END)
        self.txt_salary_recipt.insert(END, self.new_sample)

    def delete(self):
        if self.var_emp_code.get() == '':
            messagebox.showerror("Error", "please enter employee id")
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="payroll")
            cur = con.cursor()
            cur.execute("select * from emp_salary where e_id=%s", (self.var_emp_code.get()))
            row = cur.fetchone()
            # print(row)
            if row == None:
                messagebox.showerror("Error", "employee id doesnot exist,try again with another id", parent=self.root)
            else:
                op = messagebox.askyesno("Confirm", "Are you Sure?")
                if op == TRUE:
                    cur.execute("Delete from emp_salary where e_id=%s", (self.var_emp_code.get()))
                    con.commit()
                    con.close()
                    messagebox.showerror("Delete", "Employee record deleted successfully", parent=self.root)
                    self.clear()

        except Exception as ex:
            messagebox.showerror("ERROR", f"Error due to:{ex}")

    def add(self):
        # frame 1
        if self.var_emp_code.get() == "" or self.var_salary.get() == "":
            messagebox.showerror("Error", "employee details are required")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", db="payroll")
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s", (self.var_emp_code.get()))
                row = cur.fetchone()
                # print(row)
                if row != None:
                    messagebox.showerror("Error", "employee id already exist,try again with another id",
                                         parent=self.root)
                else:

                    cur.execute(
                        "insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",

                        (
                            self.var_emp_code.get(),
                            self.var_designation.get(),
                            self.var_name.get(),
                            self.var_age.get(),
                            self.var_gender.get(),
                            self.var_email.get(),
                            self.var_hr_location.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                            self.var_contact.get(),
                            self.var_experience.get(),
                            self.var_proof_id.get(),
                            self.var_status.get(),
                            self.txt_address.get('1.0', END),

                            # frame 2
                            self.var_month.get(),
                            self.var_year.get(),
                            self.var_salary.get(),
                            self.var_t_days.get(),
                            self.var_pf.get(),
                            self.var_medical.get(),
                            self.var_convence.get(),
                            self.var_netsal.get(),
                            self.var_absent.get(),
                            self.var_emp_code.get() + ".txt"
                        )
                        )
                    con.commit()
                    con.close()
                    # file_=open("Salary Receipt/"+str(self.var_emp_code.get()+".txt"),'w')
                    # file.write(self.txt_salary_recipt.get("1.0",END))
                    # file_.close()
                    messagebox.showinfo("Success", "recored:)")

            except Exception as ex:
                messagebox.showerror("ERROR", f"Error due to:{ex}")

    def update(self):
        # frame 1
        if self.var_emp_code.get() == "" or self.var_salary.get() == "":
            messagebox.showerror("Error", "Employee details are required")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", db="payroll")
                cur = con.cursor()
                cur.execute("SELECT * FROM emp_salary WHERE e_id=%s", (self.var_emp_code.get(),))
                row = cur.fetchone()
                # print(row)
                if row is None:
                    messagebox.showerror("Error", "Employee ID invalid! Try again with another ID", parent=self.root)
                else:
                    cur.execute("""
                        UPDATE emp_salary 
                        SET e_id=%s, designation=%s, name=%s, age=%s, gender=%s, email=%s, hr_location=%s, 
                        dob=%s, doj=%s, contact=%s, exp=%s, proof_id=%s, status=%s, address=%s, month=%s, year=%s, 
                        salary=%s, t_days=%s, pf=%s, medical=%s, covence=%s, net_salary=%s, Salary_reciept=%s, 
                        Absent_days=%s 
                        WHERE e_id=%s
                    """, (
                        self.var_emp_code.get(),
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_hr_location.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_contact.get(),
                        self.var_experience.get(),
                        self.var_proof_id.get(),
                        self.var_status.get(),
                        self.txt_address.get('1.0', END),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_t_days.get(),
                        self.var_pf.get(),
                        self.var_medical.get(),
                        self.var_convence.get(),
                        self.var_netsal.get(),
                        self.var_emp_code.get() + ".txt",
                        self.var_absent.get(),
                        self.var_emp_code.get()  # where the record should be updated by emp_code
                    ))

                    con.commit()
                    con.close()

                    # Writing the salary receipt to a text file
                    # with open(f"Salary Receipt/{self.var_emp_code.get()}.txt", 'w') as file_:
                    # file_.write(self.txt_salary_recipt.get("1.0", END))

                    messagebox.showinfo("Success", "Updated successfully!")

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {ex}")

    def calculate(self):
        if self.var_month.get() == '' or self.var_year.get() == '' or self.var_salary.get() == '' or self.var_t_days.get() == '':
            messagebox.showerror('Error', "All fields are required")
        else:
            per_day = float(self.var_salary.get()) / float(self.var_t_days.get())
            work_day = float(self.var_t_days.get()) - float(self.var_absent.get())
            sal = per_day * work_day
            deduct = float(self.var_medical.get()) + float(self.var_pf.get())
            addition = float(self.var_convence.get())
            net_sal = sal - deduct + addition
            self.var_netsal.set(str(round(net_sal, 2)))

            # Construct the receipt
            new_sample = f''' \tCompany Name, XYZ\n\tAddress: Xyz, Floor 4
             -----------------------------------------
              Employee ID\t\t: {self.var_emp_code.get()}
              Salary of\t\t: {self.var_month.get()}-{self.var_year.get()}
              Generated on\t\t: {time.strftime("%d-%m-%Y")}
             -----------------------------------------
              Total days\t\t: {self.var_t_days.get()}
              Total Present\t\t: {str(int(self.var_t_days.get()) - int(self.var_absent.get()))}
              Total Absent\t\t: {self.var_absent.get()}
              Convence\t\t: Rs.{self.var_convence.get()}
              Medical \t\t: Rs.{self.var_medical.get()}
              Pf\t\t: Rs.{self.var_pf.get()}
              Gross Payment\t\t: Rs.{self.var_salary.get()}
              Net Salary\t\t: Rs.{self.var_netsal.get()}
             --------------------------------------------
             This is a computer-generated slip, not required any signature     
                        '''

            # Clear the previous receipt and insert the new one
            self.txt_salary_recipt.delete("1.0", END)
            self.txt_salary_recipt.insert(END, new_sample)
            scroll_y = Scrollbar(sal_Frame2, orient=VERTICAL)
            scroll_y.pack(fill=Y, side=RIGHT)

            self.txt_salary_recipt = Text(sal_Frame2, font=("times new roman", 15), bg="light yellow",
                                          yscrollcommand=scroll_y.set)
            self.txt_salary_recipt.pack(fill=BOTH, expand=1)

            scroll_y.config(command=self.txt_salary_recipt.yview)

    def check_connection(self):
        try:
            con = pymysql.connect(host="localhost", user="root", password="", db="payroll")
            cur = con.cursor()
            cur.execute("select * from emp_salary")
            row = cur.fetchall()
            print(row)


        except Exception as ex:
            messagebox.showerror("ERROR", f"Error due to:{ex}")

    def print(self):
        file_ = tempfile.mktemp(".txt")
        open(file_, 'w').write(self.txt_salary_recipt.get("1.0", END))
        os.startfile(file_, "print")
        print(self.txt_salary_recipt.get("1.0", END))


root = Tk()
obj = EmployeeSystem(root)
root.mainloop()
