from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type, List

class UnsupportedFeature(BaseModel):
    file_path: str = Field(..., description="File path")
    unsupported_api_feature: str = Field(..., description="Unsupported API feature")

class JavaUnsupportedAPIUsageIdentifierInput(BaseModel):
    repo_url: str = Field(..., description="Repository URL")

class JavaUnsupportedAPIUsageIdentifierOutput(BaseModel):
    status: str = Field(..., description="Status of the tool")
    unsupported_features: List[UnsupportedFeature] = Field(..., description="List of unsupported features")

class JavaUnsupportedAPIUsageIdentifierTool(BaseTool):
    """
    Java Unsupported API Usage Identifier Tool
    """
    name: str = "Java Unsupported API Usage Identifier Tool"
    args_schema: Type[BaseModel] = JavaUnsupportedAPIUsageIdentifierInput
    description: str = "Identifies where an unsupported java api/feature is used in the codebase"

    def _execute(self, repo_url: str):
        """
        Executes the tool (TODO)
        """
        status = "success"
        unsupported_features = []
        return JavaUnsupportedAPIUsageIdentifierOutput(status=status, unsupported_features=unsupported_features)