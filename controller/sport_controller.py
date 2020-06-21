
from model.dao.sport_dao import SportDAO


class SportController:

    def __init__(self, database_engine):
        self._database_engine = database_engine
        self._frames = []

    def list_sport(self):
        with self._database_engine.new_session() as session:
            sports = SportDAO(session).get_all()
            sports_data = [sport.to_dict() for sport in sports]
        return sports_data
