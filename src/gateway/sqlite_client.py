from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

SQLiteBase = declarative_base()

class SQLiteClient:
    database_path = "sqlite:///db/database.db"

    def __init__(self):
        self._engine = create_engine(self.database_path, connect_args={"check_same_thread": False})
        self._SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        self._Base = declarative_base()

    def __call__(self) -> Session:
        session_local = self._SessionLocal()
        try:
            yield session_local
        finally:
            session_local.close()

    def _get_session(self) -> Session:
        return next(self.__call__())



