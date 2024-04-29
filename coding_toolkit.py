from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from coding_tool import CodingTool


class GreetingsToolkit(BaseToolkit, ABC):
    name: str = "Coding Toolkit"
    description: str = "Coding Toolkit for TI Autonomous Software Engineer"

    def get_tools(self) -> List[BaseTool]:
        return [CodingTool()]

    def get_env_keys(self) -> List[str]:
        return ["FROM"]