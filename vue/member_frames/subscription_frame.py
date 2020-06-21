from tkinter import *
from tkinter import messagebox

from vue.base_frame import BaseFrame
from exceptions import Error


class SubscriptionFrame(BaseFrame):
    def __init__(self, member_controller, sport_controller, master=None):
        super().__init__(master)
        self._member_controller = member_controller
        self._sport_controller = sport_controller
        self.coach_value = IntVar()
        self.create_widgets()
        self.name_pattern = re.compile("^[\S-]{2,50}$")
        self.email_pattern = re.compile("^([a-zA-Z0-9_\.-]+)@([a-zA-Z0-9_\.-]+)\.([a-zA-Z]{2,5})$")
        self.sports = self.init_sport_list()

    def create_widgets(self):

        self.firstname_entry = self.create_entry("Firstname", row=0, validate_callback=self.validate_name)
        self.lastname_entry = self.create_entry("Lastname", row=1, validate_callback=self.validate_name)
        self.email_entry = self.create_entry("Email", row=2, validate_callback=self.validate_email)
        yDefil = Scrollbar(self, orient='vertical')
        self.listbox = Listbox(self, yscrollcommand=yDefil.set, width=30, selectmode='multiple')
        yDefil['command'] = self.listbox.yview
        yDefil.grid(row=4, column=2, sticky='ns')
        self.listbox.grid(row=4, column=1, sticky='nsew')

        # self.comboBox = self.create_comboBox("Sport", row=4, columnspan=3, current=0)

        self.valid = Button(self, text="valid", fg="red",
                            command=self.valid)
        self.cancel = Button(self, text="cancel", fg="red",
                             command=self.show_menu)

        self.coachButton = Checkbutton(self, text='coach', variable=self.coach_value)
        self.coachButton.grid(row=4, column=3)

        self.valid.grid(row=5, column=1, sticky=E)
        self.cancel.grid(row=5, column=2, sticky=W)

    def validate_name(self, event, entry=None):
        if not self.name_pattern.match(entry.get()):
            entry.config(fg='red')
        else:
            entry.config(fg='black')

    def validate_email(self, event, entry=None):
        if not self.email_pattern.match(entry.get()):
            entry.config(fg='red')
        else:
            entry.config(fg='black')

    # def validate_sport(self, event, entry=None):
    #     if not self.comboExample.current() == 0

    def valid(self):
        test = self.listbox.curselection()
        sports_data = []
        for sport in test:
            sports_data.append(self.sports[sport])
        data = dict(firstname=self.firstname_entry.get(), lastname=self.lastname_entry.get(),
                    email=self.email_entry.get(), coach=self.coach_value == 1, sports=sports_data)
        try:
            member_data = self._member_controller.create_member(data)
            messagebox.showinfo("Success",
                                "Member %s %s created !" % (member_data['firstname'], member_data['lastname']))

        except Error as e:
            messagebox.showerror("Error", str(e))
        return

        self.show_menu()

    def init_sport_list(self):
        sports = self._sport_controller.list_sport()
        for index, sport in enumerate(sports):
            text = sport['libelle']
            self.listbox.insert('end', text)
        return sports
