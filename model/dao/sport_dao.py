from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from model.mapping.sport import Sport
from model.dao.dao import DAO

from exceptions import Error, ResourceNotFound
from sqlalchemy.exc import SQLAlchemyError


class SportDAO(DAO):

    def __init__(self, database_session):
        super().__init__(database_session)

    def get_all(self):
        try:
            return self._database_session.query(Sport).order_by(Sport.libelle).all()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        pass

    def update(self, entity, data: dict):
        pass

    def delete(self, entity):
        pass

    def get(self, id):
        try:
            return self._database_session.query(Sport).filter_by(id=id).one()
        except NoResultFound:
            raise ResourceNotFound()