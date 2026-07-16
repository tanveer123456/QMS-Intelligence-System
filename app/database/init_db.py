from app.database.session import engine
from app.database.base import Base

# Import all models here
# from app.models.user import User


def create_tables():
    """
    Create all database tables.
    """
    Base.metadata.create_all(bind=engine)