class RepoError(Exception):
    """Exceção genérica para erros de repositório."""
    pass

class RuleNotFoundError(RepoError):
    """Exceção levantada quando uma regra não é encontrada."""
    pass

class DeleteInactiveError(RepoError):
    """Exceção levantada quando se tenta deletar uma regra já inativa."""
    pass

class RevertActiveError(RepoError):
    """Exceção levantada quando se tenta reverter uma regra já ativa."""
    pass

class UpdateInactiveError(RepoError):
    """Exceção levantada quando se tenta atualizar uma regra inativa."""
    pass