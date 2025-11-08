from sqlalchemy.exc import IntegrityError

from src.service.interface.interface_quality_rule_service import IQualityRuleService
from src.repository.interface.interface_quality_rule_repository import IQualityRuleRepository
from src.model.quality_rule_model import QualityRuleModel
from src.exceptions.quality_rule_exceptions import QualityRuleNotFoundError
from src.exceptions.repo_exceptions import (
    RuleNotFoundError,
    DeleteInactiveError,
    RevertActiveError,
    UpdateInactiveError
)


class QualityRuleService(IQualityRuleService):

    def __init__(self, repository: IQualityRuleRepository):
        self._repository = repository

    def create_quality_rule(self,
                            rule_type: str,
                            table_target: str,
                            column_target: str,
                            min_value: float | None = None,
                            max_value: float | None = None,
                            enum_value: list | None = None,
                            regex_expr: str | None = None) -> QualityRuleModel:
        try:
            return self._repository.create_quality_rule(
                rule_type=rule_type,
                table_target=table_target,
                column_target=column_target,
                min_value=min_value,
                max_value=max_value,
                enum_value=enum_value,
                regex_expr=regex_expr
            )
        except IntegrityError as e:
            raise ValueError("Regra de qualidade já existe com os mesmos parâmetros.") from e
        except Exception as e:
            raise ValueError("Erro ao criar a regra de qualidade.") from e
    



    def read_quality_rules(self, rule_id: int) -> QualityRuleModel:
        rule = self._repository.read_quality_rules(rule_id)
        if not rule:
            raise QualityRuleNotFoundError(f"Regra de qualidade com ID {rule_id} não encontrada.")
        return rule
        

    def read_by_target_table(self, table_target: str, is_active: bool | None = None) -> list[QualityRuleModel]:
        rules = self._repository.read_by_target_table(table_target=table_target, is_active=is_active)
        return rules


    def update_quality_rule(self,
                            rule_id: int,
                            rule_type: str | None = None,
                            table_target: str | None = None,
                            column_target: str | None = None,
                            min_value: float | None = None,
                            max_value: float | None = None,
                            enum_value: list | None = None,
                            regex_expr: str | None = None) -> QualityRuleModel:
        try:
            return self._repository.update_quality_rule(
                rule_id=rule_id,
                rule_type=rule_type,
                table_target=table_target,
                column_target=column_target,
                min_value=min_value,
                max_value=max_value,
                enum_value=enum_value,
                regex_expr=regex_expr
            )
        except RuleNotFoundError as e:
            raise QualityRuleNotFoundError(f"Regra de qualidade com ID {rule_id} não encontrada.") from e
        except UpdateInactiveError as e:
            raise ValueError(f"Não é possível atualizar uma regra inativa (ID {rule_id}).") from e
    

    def deactivate_by_id(self, rule_id: int) -> QualityRuleModel:
        try:
            return self._repository.delete_quality_rule(rule_id)
        except RuleNotFoundError as e:
            raise QualityRuleNotFoundError(f"Regra de qualidade com ID {rule_id} não encontrada.") from e
        except DeleteInactiveError as e:
            raise ValueError(f"Regra com ID {rule_id} já está inativa.") from e

    def activate_by_id(self, rule_id: int) -> QualityRuleModel:
        try:
            return self._repository.revert_delete(rule_id)
        except RuleNotFoundError as e:
            raise QualityRuleNotFoundError(f"Regra de qualidade com ID {rule_id} não encontrada.") from e
        except RevertActiveError as e:
            raise ValueError(f"Regra com ID {rule_id} já está ativa.") from e
    

if __name__ == "__main__":
    from src.repository.sqlite_quality_rule_repository import SQLiteQualityRuleRepository
    repo = SQLiteQualityRuleRepository()
    service = QualityRuleService(repository=repo)
    print(service.read_quality_rules(rule_id=1))
    # service.read_by_target_table(table_target="users")
    # service.create_quality_rule(
    #     rule_type="range",
    #     table_target="users",
    #     column_target="age",
    #     min_value=18,
    #     max_value=99
    # )
    # service.update_quality_rule(
    #     rule_id=1,
    #     min_value=21
    # )
    # service.deactivate_by_id(rule_id=1)
    # service.activate_by_id(rule_id=1)