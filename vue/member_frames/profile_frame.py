
from tkinter import *
from tkinter import messagebox
from vue.base_frame import BaseFrame


class ProfileFrame(BaseFrame):

    def __init__(self, member_controller, member, master=None):
        super().__init__(master)
        self._member = member
        self._member_controller = member_controller
        self._name_pattern = re.compile("^[\S-]{2,50}$")
        self._email_pattern = re.compile("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
        self._create_widgets()

    def _create_widgets(self):

        self.title = Label(self, text="Profile: ")
        self.title.grid(row=0, column=0, sticky=W)

        self.firstname_entry = self.create_entry("Firstname: ", text=self._member['firstname'],
                                                 row=1, validate_callback=self.validate_name,
                                                 disabled=True, columnspan=3)
        self.lastname_entry = self.create_entry("Lastname: ", text=self._member['lastname'],
                                                row=2, validate_callback=self.validate_name,
                                                disabled=True, columnspan=3)
        self.email_entry = self.create_entry("Email: ", text=self._member['email'],
                                             row=3, validate_callback=self.validate_email,
                                             disabled=True, columnspan=4)

        # Buttons
        self.edit_button = Button(self, text="Edit",
                                  command=self.edit)
        self.cancel_button = Button(self, text="Cancel", command=self.refresh)
        self.update_button = Button(self, text="Update", command=self.update)
        self.remove_button = Button(self, text="Remove", command=self.remove)
        self.return_button = Button(self, text="Return", fg="red",
                                    command=self.back)

        self.return_button.grid(row=5, column=0)
        self.edit_button.grid(row=5, column=1, sticky="nsew")
        self.remove_button.grid(row=5, column=2, sticky="nsew")

    def validate_name(self, event, entry=None):
        if not self._name_pattern.match(entry.get()):
            entry.config(fg='red')
        else:
            entry.config(fg='black')

    def validate_email(self, event, entry=None):
        if not self._email_pattern.match(entry.get()):
            entry.config(fg='red')
        else:
            entry.config(fg='black')

    def edit(self):
        self.edit_button.grid_forget()
        self.remove_button.grid_forget()
        self.firstname_entry.config(state=NORMAL)
        self.lastname_entry.config(state=NORMAL)
        self.email_entry.config(state=NORMAL)
        self.cancel_button.grid(row=5, column=2, sticky="nsew")
        self.update_button.grid(row=5, column=1, sticky="nsew")

    def refresh(self):
        # Restore window with member value and cancel edition
        self.cancel_button.grid_forget()
        self.update_button.grid_forget()
        self.firstname_entry.delete(0, END)
        self.firstname_entry.insert(0, self._member['firstname'])
        self.firstname_entry.config(state=DISABLED)
        self.lastname_entry.delete(0, END)
        self.lastname_entry.insert(0, self._member['lastname'])
        self.lastname_entry.config(state=DISABLED)
        self.email_entry.delete(0, END)
        self.email_entry.insert(0, self._member['email'])
        self.email_entry.config(state=DISABLED)
        self.edit_button.grid(row=5, column=1, sticky="nsew")
        self.remove_button.grid(row=5, column=2, sticky="nsew")

    def update(self):

        data = dict(firstname=self.firstname_entry.get(), lastname=self.lastname_entry.get(),
                    email=self.email_entry.get())
        member = self._member_controller.update_member(self._member['id'], data)
        self._member = member
        self.refresh()

    def remove(self):
        member_id = self._member['id']
        self._member_controller.delete_member(member_id)
        # show confirmation
        messagebox.showinfo("Success",
                            "Member %s %s deleted !" % (self._member['firstname'], self._member['lastname']))
        self.back()
