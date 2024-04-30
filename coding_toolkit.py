from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import List
from java_api_usage_migrator_tool import JavaAPIUsageMigratorTool
from java_library_breaking_release_identifier_tool import JavaLibraryBreakingReleaseIdentifierTool
from java_library_breaking_usage_identifier_tool import JavaLibraryBreakingUsageIdentifierTool
from java_unsupported_api_usage_identier_tool import JavaUnsupportedAPIUsageIdentifierTool
from java_library_upgrade_patch_generator_tool import JavaLibraryUpgradePatchGeneratorTool

class GreetingsToolkit(BaseToolkit, ABC):
    name: str = "Coding Toolkit"
    description: str = "Coding Toolkit for TI Autonomous Software Engineer"

    def get_tools(self) -> List[BaseTool]:
        return [
            JavaAPIUsageMigratorTool(),
            JavaLibraryBreakingReleaseIdentifierTool(),
            JavaLibraryBreakingUsageIdentifierTool(),
            JavaUnsupportedAPIUsageIdentifierTool(),
            JavaLibraryUpgradePatchGeneratorTool()
        ]

    def get_env_keys(self) -> List[str]:
        return ["FROM"]