from database import Base
from sqlalchemy import Column, Integer, \
                       String


class Guild(Base):
    __tablename__ = 'Guild'
    GuildID = Column(Integer, primary_key=True)
    Prefix = Column(String(80), nullable=False)

    def __repr__(self):
        return f'<Guild: {self.GuildID}, {self.Prefix}>'