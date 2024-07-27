from sqlalchemy import create_engine
from models.base_model import Base
from models.place import Place  # Ensure this import matches your directory structure

# Replace this with your actual database URI
DATABASE_URI = 'mysql+mysqldb://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db'

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
