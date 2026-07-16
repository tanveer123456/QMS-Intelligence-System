from app.database.base import Base
from app.database.session import engine

# Import all models here
from app.models.user import User


def create_tables() -> None:
    """Create all database tables."""
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    print("Creating database tables...")
    create_tables()
    print("Database initialized successfully.")