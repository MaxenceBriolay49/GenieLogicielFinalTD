from model.database import DatabaseEngine
from controller.member_controller import MemberController

from vue.root_frame import RootFrame


def main():
    print("Welcome in BDS App")

    # Init db
    database_engine = DatabaseEngine(url='sqlite:///bds.db')
    database_engine.create_database()

    # controller
    member_controller = MemberController(database_engine)

    # init vue
    root = RootFrame(member_controller)
    root.master.title("bds subscription app")
    root.show_menu()

    # start
    root.mainloop()


if __name__ == "__main__":
    main()
