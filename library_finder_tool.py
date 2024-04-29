from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class LibraryFinderInput(BaseModel):
    description: str = Field(..., description="Describing to find libraries in a subdomain or whole codebase")

class LibraryFinderOutput(BaseModel):
    libraries: str = Field(..., description="List of libraries")

class LibraryFinderTool(BaseTool):
    """
    Library Finder Tool
    """
    name: str = "Library Finder Tool"
    args_schema: Type[BaseModel] = LibraryFinderInput
    description: str = "Library Finder Tool to find all the libraries in the codebase"

    def _execute(self, description: str = None):
        """
        Executes the tool (TODO)
        """
        libraries = "library1, library2, library3"
        return LibraryFinderOutput(libraries=libraries)