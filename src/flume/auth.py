# auth.py

import firebase_admin
from firebase_admin import credentials, auth
import asyncio


class FirebaseAuth:
    def __init__(self, service_account_info: dict):
        self.cred = credentials.Certificate(service_account_info)
        firebase_admin.initialize_app(self.cred)

    def verify_token_sync(self, token: str):
        """Synchronous token verification.

        Args:
            token (str): The Firebase ID token to verify.

        Returns:
            dict: The decoded token if verification is successful.

        Raises:
            ValueError: If the token is invalid or expired.
        """
        try:
            decoded_token = auth.verify_id_token(token)
            return decoded_token
        except Exception as e:
            raise ValueError("Invalid token") from e

    async def verify_token_async(self, token: str):
        """Asynchronous token verification.

        Args:
            token (str): The Firebase ID token to verify.

        Returns:
            dict: The decoded token if verification is successful.

        Raises:
            ValueError: If the token is invalid or expired.
        """
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self.verify_token_sync, token)
