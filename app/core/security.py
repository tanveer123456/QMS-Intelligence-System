"""
Security utilities for the QMS Intelligence System.

This module provides:
1. Password hashing and verification
2. JWT token creation
3. JWT token validation
"""

from datetime import datetime, timedelta, timezone
from typing import Any

from jose import JWTError, jwt
from pwdlib import PasswordHash

from app.core.config import settings

# ==========================================================
# Password Hashing
# ==========================================================

password_hasher = PasswordHash.recommended()


def hash_password(password: str) -> str:
    """
    Hash a plain-text password.

    Args:
        password: User's plain-text password.

    Returns:
        Secure hashed password.
    """
    return password_hasher.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    """
    Verify a plain password against its stored hash.

    Args:
        plain_password: Password entered by the user.
        hashed_password: Password hash stored in database.

    Returns:
        True if passwords match, otherwise False.
    """
    return password_hasher.verify(
        plain_password,
        hashed_password,
    )


# ==========================================================
# JWT Token
# ==========================================================

def create_access_token(
    subject: str,
    expires_delta: timedelta | None = None,
) -> str:
    """
    Generate a JWT access token.

    Args:
        subject: Usually the user's email or username.
        expires_delta: Optional custom expiration time.

    Returns:
        Encoded JWT token.
    """

    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.access_token_expire_minutes
        )

    payload: dict[str, Any] = {
        "sub": subject,
        "exp": expire,
    }

    encoded_jwt = jwt.encode(
        payload,
        settings.secret_key,
        algorithm=settings.algorithm,
    )

    return encoded_jwt


def decode_access_token(token: str) -> dict[str, Any] | None:
    """
    Decode and validate a JWT token.

    Args:
        token: JWT access token.

    Returns:
        Token payload if valid, otherwise None.
    """

    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm],
        )

        return payload

    except JWTError:
        return None