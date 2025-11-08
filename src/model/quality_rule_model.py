from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, Boolean

from sqlalchemy import Column, String, Float, JSON, Integer

from src.gateway.sqlite_client import SQLiteBase


class QualityRuleModel(SQLiteBase):
    __tablename__ = "quality_rules"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="quality_rules_pk"),
        UniqueConstraint("rule_type", "table_target", "column_target", name="quality_rules_unique_rule"),
    )

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    rule_type = Column(String, nullable=False)
    table_target = Column(String, nullable=False)
    column_target = Column(String, nullable=False)
    min_value = Column(Float, nullable=True)
    max_value = Column(Float, nullable=True)
    enum_value = Column(JSON, nullable=True)
    regex_expr = Column(String, nullable=True)
    is_active = Column(Boolean, default=False)  # 1 for active, 0 for inactive
