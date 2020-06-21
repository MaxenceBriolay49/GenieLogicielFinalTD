from model.mapping import Base

from sqlalchemy import Column, String, UniqueConstraint, Integer


class Association(Base):
    __tablename__ = 'association'
    __table_args__ = (UniqueConstraint('idMembre', 'idSport'),)

    idMembre = Column(String(36), nullable=False, primary_key=True)
    idSport = Column(Integer, nullable=False, primary_key=True)

    def to_dict(self):
        return {
            "idMembre": self.idMembre,
            "idSport": self.idSport
        }
