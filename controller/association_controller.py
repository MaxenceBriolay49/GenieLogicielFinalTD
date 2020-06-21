import re

from model.dao.association_dao import AssociationDAO

from exceptions import Error, InvalidData


class AssociationController:

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def set_sports_for_member(self, membre):
        with self._database_engine.new_session() as session:
            AssociationDAO(session).set_sport_for_member(membre)
