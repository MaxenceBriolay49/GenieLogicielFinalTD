import unittest
import uuid
from exceptions import InvalidData, Error, ResourceNotFound
from controller.member_controller import MemberController
from model.database import DatabaseEngine
from model.mapping.member import Member


class TestCoachController(unittest.TestCase):
    """
    Unit Tests sport controller
    https://docs.python.org/fr/3/library/unittest.html
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls._database_engine = DatabaseEngine()
        cls._database_engine.create_database()
        with cls._database_engine.new_session() as session:

            # Person
            john = Member(id=str(uuid.uuid4()),
                          firstname="john", lastname="do",
                          email="john.do@mail.com")
            session.add(john)
            session.flush()
            cls.john_id = john.id

    def setUp(self) -> None:
        """
        Function called before each test
        """
        self.member_controller = MemberController(self._database_engine)

    def test_list_members(self):
        coaches = self.member_controller.list_members()
        self.assertGreaterEqual(len(coaches), 1)

    def test_get_member(self):
        coach = self.member_controller.get_member(self.john_id)
        self.assertEqual(coach['firstname'], "john")
        self.assertEqual(coach['lastname'], "do")
        self.assertEqual(coach['id'], self.john_id)

    def test_get_member_not_exists(self):
        with self.assertRaises(ResourceNotFound):
            self.member_controller.get_member(str(uuid.uuid4()))

    def test_create_member(self):
        data = {
            "firstname": "Han",
            "lastname": "Solo",
            "email": "han.solo@star.com"
        }
        coach_data = self.member_controller.create_member(data)
        self.assertIn('id', coach_data)
        self.assertEqual(data['firstname'], coach_data['firstname'])
        self.assertEqual(data['lastname'], coach_data['lastname'])

    def test_create_member_missing_data(self):
        data = {}
        with self.assertRaises(InvalidData):
            self.member_controller.create_member(data)

    def test_create_member_error_already_exists(self):
        data = {"firstname": "john", "lastname": "do", "email": "john.do@hostmail.fr"}
        with self.assertRaises(Error):
            self.member_controller.create_member(data)

    def test_update_member(self):
        member_data = self.member_controller.update_member(
            self.john_id, {"email": "john.do@updated.com"})
        self.assertEqual(member_data['email'], "john.do@updated.com")

    def test_update_member_invalid_data(self):
        with self.assertRaises(InvalidData):
            self.member_controller.update_member(self.john_id, {"email": "test"})

    def test_update_member_not_exists(self):
        with self.assertRaises(ResourceNotFound):
            self.member_controller.update_member("test", {"description": "test foot"})

    def test_delete_member(self):
        with self._database_engine.new_session() as session:
            rob = Member(id=str(uuid.uuid4()), firstname="rob", lastname="stark",
                         email="rob.stark@winterfell.com")
            session.add(rob)
            session.flush()
            rob_id = rob.id

        self.member_controller.delete_member(rob_id)
        with self.assertRaises(ResourceNotFound):
            self.member_controller.delete_member(rob_id)

    def test_delete_member_not_exists(self):
        with self.assertRaises(ResourceNotFound):
            self.member_controller.delete_member(str(uuid.uuid4()))

    def test_search_member(self):
        coach = self.member_controller.search_member("john", "do")
        self.assertEqual(coach['id'], self.john_id)

    def test_search_member_not_exists(self):
        with self.assertRaises(ResourceNotFound):
            self.member_controller.search_member("john", "snow")


if __name__ == '__main__':
    unittest.main()
