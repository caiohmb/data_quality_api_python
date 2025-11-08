from src.repository.interface.interface_quality_rule_repository import IQualityRuleRepository
from src.model.quality_rule_model import QualityRuleModel
from src.gateway.sqlite_client import SQLiteClient

class SQLiteQualityRuleRepository(IQualityRuleRepository):
    def __init__(self):
        self._sqlite_client = SQLiteClient()


    def create_quality_rule(self,
                rule_type: str,
                table_target: str, 
                column_target: str,
                min_value: float | None = None,
                max_value: float | None = None,
                enum_value: list | None = None,
                regex_expr: str | None = None,
                ) -> QualityRuleModel:
        with self._sqlite_client._get_session() as session:
            rule = QualityRuleModel(
                rule_type=rule_type,
                table_target=table_target,
                column_target=column_target,
                min_value=min_value,
                max_value=max_value,
                enum_value=enum_value,
                regex_expr=regex_expr,
                is_active=True
            )
            session.add(rule)
            session.commit()
            session.refresh(rule)
            return rule

    def read_quality_rules(self, rule_id: int) -> list[QualityRuleModel]:
        with self._sqlite_client._get_session() as session:
            rules = session.query(QualityRuleModel).filter(QualityRuleModel.id == rule_id).all()
            return rules
        
    def read_by_target_table(self, 
                             table_target: str, 
                             is_active: bool | None = None) -> list[QualityRuleModel]:
        with self._sqlite_client._get_session() as session:
            query = session.query(QualityRuleModel).filter(QualityRuleModel.table_target == table_target)
            if is_active is not None:
                query = query.filter(QualityRuleModel.is_active == is_active)
            rules = query.all()
            return rules
        
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
        with self._sqlite_client._get_session() as session:
            rule = session.query(QualityRuleModel).filter(QualityRuleModel.id == rule_id).first()
            if rule_type is not None:
                rule.rule_type = rule_type
            if table_target is not None:
                rule.table_target = table_target
            if column_target is not None:
                rule.column_target = column_target
            if min_value is not None:
                rule.min_value = min_value
            if max_value is not None:
                rule.max_value = max_value
            if enum_value is not None:
                rule.enum_value = enum_value
            if regex_expr is not None:
                rule.regex_expr = regex_expr
            if is_active is not None:
                rule.is_active = is_active
            session.commit()
            session.refresh(rule)
            return rule
        
    def delete_quality_rule(self, rule_id: int) -> QualityRuleModel:
        with self._sqlite_client._get_session() as session:
            rule = session.query(QualityRuleModel).filter(QualityRuleModel.id == rule_id).first()
            rule.is_active = False
            session.commit()
            session.refresh(rule)
            return rule
        
    def revert_delete(self, rule_id: int) -> QualityRuleModel:
        with self._sqlite_client._get_session() as session:
            rule = session.query(QualityRuleModel).filter(QualityRuleModel.id == rule_id).first()
            rule.is_active = True
            session.commit()
            session.refresh(rule)
            return rule
    

if __name__ == "__main__":
    repo = SQLiteQualityRuleRepository()
    new_rule = repo.create_quality_rule(
        rule_type="min_value",
        table_target="users",
        column_target="age",
        min_value=18.0
    )
    print(new_rule)

    