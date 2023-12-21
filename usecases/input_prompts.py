from typing import Annotated

from fastapi import Depends

from model.inputPrompts.input_prompt_model import InputPrompts

from repositories.input_prompts import InputPromptRepository



class InputPromptUsecase:
    inputPromptRepository: InputPromptRepository

    def __init__(
            self,
            inputPromptRepository: Annotated[InputPromptRepository, Depends()]
    ) -> None:
        self.inputPromptRepository = inputPromptRepository

    def get_by_id(self, id: int) -> InputPrompts | None:
        return self.inputPromptRepository.get_by_id(id)

    def get_by_feature_id_and_model_id(self, feature_id: int, model_id : int, language_id: int) -> InputPrompts | None:
        return self.inputPromptRepository.get_by_feature_id_and_model_id(feature_id, model_id, language_id)