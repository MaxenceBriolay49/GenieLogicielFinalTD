

from tkinter import *
from tkinter import messagebox

from vue.base_frame import BaseFrame
from exceptions import Error


class SubscriptionFrame(BaseFrame):

    def __init__(self, member_controller, master=None):
        super().__init__(master)
        self._member_controller = member_controller
        self.create_widgets()
        self.name_pattern = re.compile("^[\S-]{2,50}$")
        self.email_pattern = re.compile("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")

    def create_widgets(self):

        self.firstname_entry = self.create_entry("Firstname", row=0, validate_callback=self.validate_name)
        self.lastname_entry = self.create_entry("Lastname", row=1, validate_callback=self.validate_name)
        self.email_entry = self.create_entry("Email", row=2, validate_callback=self.validate_email)

        self.valid = Button(self, text="valid", fg="red",
                            command=self.valid)
        self.cancel = Button(self, text="cancel", fg="red",
                             command=self.show_menu)
        self.valid.grid(row=4, column=1, sticky=E)
        self.cancel.grid(row=4, column=2, sticky=W)

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

    def valid(self):

        data = dict(firstname=self.firstname_entry.get(), lastname=self.lastname_entry.get(),
                    email=self.email_entry.get())
        try:
            member_data = self._member_controller.create_member(data)
            messagebox.showinfo("Success",
                                "Member %s %s created !" % (member_data['firstname'], member_data['lastname']))

        except Error as e:
            messagebox.showerror("Error", str(e))
            return

        self.show_menu()
