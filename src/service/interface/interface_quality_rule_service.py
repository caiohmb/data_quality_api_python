from abc import ABC, abstractmethod
from src.model.quality_rule_model import QualityRuleModel

class IQualityRuleService(ABC):

    @abstractmethod
    def create_quality_rule(self, 
                rule_type: str,
                table_target: str, 
                column_target: str,
                min_value: float | None = None,
                max_value: float | None = None,
                enum_value: list | None = None,
                regex_expr: str | None = None,
                ) -> QualityRuleModel:
        pass

    @abstractmethod
    def read_quality_rules(self, rule_id: int) -> list[QualityRuleModel]:
        pass

    def read_by_target_table(self, 
                             table_target: str, 
                             is_active: bool | None = None) -> list[QualityRuleModel]:
        pass

    @abstractmethod
    def update_quality_rule(self, 
                rule_id: int,
                rule_type: str | None = None,
                table_target: str | None = None, 
                column_target: str | None = None,
                min_value: float | None = None,
                max_value: float | None = None,
                enum_value: list | None = None,
                regex_expr: str | None = None,
                is_active: bool | None = None
                ) -> QualityRuleModel:
        pass

    @abstractmethod
    def deactivate_by_id(self, rule_id: int) -> QualityRuleModel:
        pass

    @abstractmethod
    def activate_by_id(self, rule_id: int) -> QualityRuleModel:
        pass