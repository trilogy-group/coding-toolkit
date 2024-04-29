from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class ReleaseNotesBrowserInput(BaseModel):
    library_name: str = Field(..., description="Name of the library to be updated")
    current_version: str = Field(..., description="Current version of the library")
    new_version: str = Field(..., description="New version of the library")

class ReleaseNotesBrowserOutput(BaseModel):
    is_breaking_change: bool = Field(description="Tells if it is a breaking change")
    changes: str = Field(..., description="Updates to the library")

class ReleaseNotesBrowserTool(BaseTool):
    """
    Library Release Notes Browser Tool
    """
    name: str = "Library Release Notes Browser Tool"
    args_schema: Type[BaseModel] = ReleaseNotesBrowserInput
    description: str = "Library Release Notes Browser Tool to find the changes from the current version to the new version"

    def _execute(self, library: str, current_version: str, new_version: str):
        """
        Executes the tool
        """
        is_breaking_change = True
        changes = ""
        return ReleaseNotesBrowserOutput(is_breaking_change=is_breaking_change, changes=changes)