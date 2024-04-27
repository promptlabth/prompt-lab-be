from typing import Annotated, Optional

from fastapi import Depends

from app.repositories.facebook import FacebookRepository



class FacebookUsecase:
    facebookRepository: FacebookRepository

    def __init__(
            self,
            facebookRepository: Annotated[FacebookRepository, Depends()]
    ) -> None:
        self.facebookRepository = facebookRepository

    def get_facebook_token_by_user_id(self, id: str) -> Optional[str]:
        return self.facebookRepository.get_facebook_token_by_user_id(id)
    
    