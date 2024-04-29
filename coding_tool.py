from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class CodingInput(BaseModel):
    instructions: str = Field(..., description="Instructions for Code updates")

class CodingOutput(BaseModel):
    diff: str = Field(..., description="Code changes")

class CodingTool(BaseTool):
    """
    Coding Tool
    """
    name: str = "Coding Tool"
    args_schema: Type[BaseModel] = CodingInput
    description: str = "Coding Tool to make code changes or write code"

    def _execute(self, instructions: str = None):
        """
        Executes the tool (TODO)
        """
        diff = instructions + "\n" + "Code changes"
        return CodingOutput(diff=diff)