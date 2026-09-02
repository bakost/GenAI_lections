# LLM Agent

![Tests](https://github.com/bakost/GenAI_lections/actions/workflows/python-tests.yml/badge.svg)
![Coverage](https://raw.githubusercontent.com/bakost/GenAI_lections/main/3_1_LLM_agent/coverage.svg)

Простой LLM-агент с инструментами (калькулятор, веб-поиск) и аудит-логированием.

## AuditLogger

Класс [`AuditLogger`](llm_agent/tool_auditlogger.py) логирует все действия
агента — входящие запросы, планы, результаты выполнения инструментов и
финальные ответы — в структурированном JSON-формате для последующего аудита.

## Запуск тестов

```bash
pip install -r requirements.txt
coverage run -m pytest tests/ -v
coverage report -m
```
