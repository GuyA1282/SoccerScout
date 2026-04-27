from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Player(Base):
	__tablename__ = 'players'
	
	id = Column(Integer, primary_key=True)
	first_name = Column(String)
	last_name = Column(String)
	age = Column(Integer)
	league = Column(String)
	jewish_score = Column(Float, default=0.0)
	
	def __init__(self, first_name, last_name, age, league):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.league = league


if __name__ == "__main__":
	engine = create_engine('sqlite:///scouting.db', echo=True)
	Base.metadata.create_all(engine)
	print("Database and tables created successfully!")
