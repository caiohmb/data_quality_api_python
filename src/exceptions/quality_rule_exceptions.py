class QualityRuleError(Exception):
    """Exceção base para erros relacionados a regras de qualidade."""
    pass

class QualityRuleNotFoundError(QualityRuleError):
    """Exceção levantada quando uma regra de qualidade não é encontrada."""
    pass

class QualityRuleExistsError(QualityRuleError):
    """Exceção levantada quando uma regra de qualidade já existe."""
    pass