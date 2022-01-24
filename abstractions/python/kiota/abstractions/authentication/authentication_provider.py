from abc import ABC, abstractmethod

from ..request_information import RequestInformation


class AuthenticationProvider(ABC):
    """
    Authenticates the application request
    """
    @abstractmethod
    async def authenticate_request(self, request: RequestInformation) -> None:
        """Authenticates the application request

        Args:
            request (RequestInformation): The request to authenticate
        """
        pass