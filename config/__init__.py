
from pydantic import BaseSettings
from sqlalchemy.orm import sessionmaker 

class Settings(BaseSettings):
  db_uri: str

  #def init(self):
    #if self.db_uri is not None:
      #create_all()

def make_settings():
    return Settings(_env_file='.env')
  
