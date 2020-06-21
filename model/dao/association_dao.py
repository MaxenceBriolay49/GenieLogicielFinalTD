from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.association import Association
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound
from sqlalchemy.exc import SQLAlchemyError


class AssociationDAO(DAO):

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        pass

    def get_all(self):
        pass

    def get_sport_from_membre(self, idMembre):
        try:
            return self._database_session.query(Association).filter_by(idMembre=idMembre)
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        pass

    def update(self, entity, data: dict):
        pass

    def delete(self, entity):
        pass

    def set_sport_for_member(self, membre):
        for sport in membre.sports:
            association = Association(idMembre=membre.id, idSport=sport['id'])
            self._database_session.add(association)
        self._database_session.flush()
