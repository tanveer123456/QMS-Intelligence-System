from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class AuthService:
    """
    Business logic for authentication.
    """

    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def register_user(
        self,
        user_data: UserCreate,
    ) -> User:
        """
        Register a new user.
        """

        # Check email
        existing_email = self.user_repository.get_by_email(
            user_data.email
        )

        if existing_email:
            raise ValueError("Email already registered.")

        # Check username
        existing_username = self.user_repository.get_by_username(
            user_data.username
        )

        if existing_username:
            raise ValueError("Username already exists.")

        # Hash password
        password_hash = hash_password(
            user_data.password
        )

        # Save user
        return self.user_repository.create(
            user_data=user_data,
            password_hash=password_hash,
        )