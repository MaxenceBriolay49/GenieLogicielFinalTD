from model.mapping import Base


from sqlalchemy import Column, String, Integer


class Sport(Base):
    __tablename__ = 'sport'

    id = Column(Integer, nullable=False, primary_key=True)
    libelle = Column(String(30), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "libelle": self.libelle
        }
