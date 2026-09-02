# llm_agent/tool_auditlogger.py

class AuditLoggerTool:
    """Инструмент для логирования и аудита."""
    
    name = "audit_logger"
    description = "Используется для логирования и аудита действий. Используйте с любыми важными данными, которые нужно зафиксировать."
    
    def use(self, expression: str) -> str:
        """
        Принимает строку с математическим выражением и возвращает результат.
        
        Args:
            expression (str): Выражение для вычисления, например, "10 * (2 + 3)".
            
        Returns:
            str: Строка с результатом или сообщением об ошибке.
        """
        try:
            node = ast.parse(expression, mode='eval').body
            result = self._eval_ast_node(node)
            return f"Результат вычисления '{expression}': {result}"
        except (ValueError, SyntaxError, TypeError) as e:
            return f"Ошибка: не могу вычислить выражение '{expression}'. Проверьте синтаксис. Детали: {e}"

    def _eval_ast_node(self, node):
        """Рекурсивно вычисляет узел AST."""
        if isinstance(node, ast.Constant): # В Python 3.8+ рекомендуется использовать ast.Constant вместо ast.Num
            return node.value
        elif isinstance(node, ast.BinOp): # Бинарная операция (например, 2 + 3)
            return ALLOWED_OPERATORS[type(node.op)](
                self._eval_ast_node(node.left),
                self._eval_ast_node(node.right)
            )
        elif isinstance(node, ast.UnaryOp): # Унарная операция (например, -5)
            return ALLOWED_OPERATORS[type(node.op)](self._eval_ast_node(node.operand))
        else:
            raise TypeError(f"Операция {node} не поддерживается")
