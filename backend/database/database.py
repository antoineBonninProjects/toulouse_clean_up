from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()
"""Base: The base class for database tables
"""

db_path = "sqlite:///"+os.path.join(os.path.dirname(__file__), 'memory.sqlite')

engine = create_engine(db_path)
Session = sessionmaker(bind=engine)
"""
The session object to interract with our database.
"""

class SigFoxMessages(Base):
    """
    A class that represents the table storing the payload of incoming SigFox messages.

    Attributes:
        id (Column): the message ID, it is the primary key of the table "sigfox_messages"
        device_id (Column): the ID of the SigFox message that has sent the frame
        seq_num (Column): the sequence number of the message to store for the given SigFox device.
        weight (Column): the weight that has been uplinked by the SigFox device.
    """
    __tablename__= "sigfox_messages"

    id = Column("id", Integer, primary_key=True)
    device_id = Column("device_id", String)
    seq_num = Column("seq#", Integer)
    weight = Column("weight", Integer)

    @property
    def serialize(self):
        """
        Returns object data in easily serializeable format

        Returns:
            dict: the serialized representation of the SigFoxMessages class attributes.
        """
        return {
            'id': self.id,
            'device_id': self.device_id,
            'seq_num': self.seq_num,
            'weight': self.weight
        }

Base.metadata.create_all(bind=engine)