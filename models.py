from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Player(Base):
	__tablename__ = 'players'
	
	id = Column(Integer, primary_key=True)
	name = Column(String)
	nationality = Column(String)
	birth_city = Column(String)
	jewish_probability = Column(Float, default=0.0)
	
	def __init__(self, name, nationality, birth_city, jewish_probability=0.0):
		self.name = name
		self.nationality = nationality
		self.birth_city = birth_city
		self.jewish_probability = jewish_probability


engine = create_engine('sqlite:///scouting.db', echo=False)

Session = sessionmaker(bind=engine)

if __name__ == "__main__":
	engine = create_engine('sqlite:///scouting.db', echo=True)
	Base.metadata.create_all(engine)
	print("Database and tables created successfully!")
