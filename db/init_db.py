from src.gateway.sqlite_client import SQLiteClient, SQLiteBase
from src.model.quality_rule_model import QualityRuleModel

if __name__ == "__main__":
    sqlite_client = SQLiteClient()
    SQLiteBase.metadata.create_all(bind=sqlite_client._engine)