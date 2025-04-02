from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

BANCODEDADOS_URL = os.getenv("BANCODEDADOS_URL")

engine = create_engine(BANCODEDADOS_URL, connect_args={"options":"-c client_encoding=utf-8"})

SessaoLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    try:
        db = SessaoLocal()
        yield db
    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    finally:
        db.close()