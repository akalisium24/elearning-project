# Перечень артефактов проекта «Онлайн-обучение» (Вариант 14)

## Матрица артефактов

| ID | Артефакт | Тип | Этап | Владелец | Место хранения | Формат | Версия | Статус | Критерии готовности |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| A-01 | ТЗ | Документ | Анализ | Аналитик | Git docs/tz.md | Markdown | v1.0 | Готов | Согласовано, 8 разделов |
| A-02 | IDEF0 A-0 | Модель | Анализ | Аналитик | Git docs/idef0.png | PNG | v1.0 | Готов | Стрелки подписаны |
| A-03 | IDEF1X | Модель | Анализ | Аналитик | Git docs/idef1x.png | PNG | v1.0 | Готов | 6 сущностей, связи |
| A-04 | Архитектура | Документ | Проектирование | Архитектор | Git docs/architecture.md | Markdown | v1.0 | Готов | 4 слоя, ADR >= 3 |
| A-05 | UML Component | Модель | Проектирование | Архитектор | Git docs/components.puml | PlantUML | v1.0 | Готов | Без циклов |
| A-06 | Схема БД | Данные | Проектирование | Архитектор | Git docs/schema.sql | SQL | v1.0 | Готов | PK/FK, 6 таблиц |
| A-07 | Код courses | Код | Разработка | Разработчик | Git courses/ | Python | main | В работе | Модуль + тесты |
| A-08 | Код lessons | Код | Разработка | Разработчик | Git lessons/ | Python | main | В работе | Модуль + тесты |
| A-09 | Код results | Код | Разработка | Разработчик | Git results/ | Python | main | В работе | Модуль + тесты |
| A-10 | Модульные тесты | Тесты | Разработка | Тестировщик | Git */tests/ | Python | main | В работе | Покрытие >= 70% |
| A-11 | Интеграционные тесты | Тесты | Тестирование | Тестировщик | Git tests/ | Python | main | План | Покрытие >= 70% |
| A-12 | pyproject.toml | Конфигурация | Разработка | DevOps | Git | TOML | main | Готов | black, ruff, pytest |
| A-13 | .gitignore | Конфигурация | Разработка | DevOps | Git | Text | main | Готов | Python + IDE + БД |
| A-14 | CI workflow | Конфигурация | Разработка | DevOps | Git .github/workflows/ci.yml | YAML | main | План | pytest + coverage |
| A-15 | README | Документ | Все этапы | Разработчик | Git README.md | Markdown | main | Готов | Установка, запуск |
| A-16 | Релиз v0.1.0 | Релиз | Внедрение | DevOps | GitHub Releases | Tag | v0.1.0 | Готов | Тег, описание |

## Трассировка артефактов к требованиям

| Артефакт | FR/NFR |
| :--- | :--- |
| courses/service.py | FR-02 Каталог курсов, FR-04 Управление курсами |
| courses/tests/test_service.py | FR-02 |
| lessons/service.py | FR-04 Управление уроками |
| tests/service.py | FR-06 Проверка тестов |
| results/service.py | FR-07 История попыток, FR-09 Отчёты |
| docs/architecture.md | NFR-01 Производительность, NFR-02 Безопасность |

## Артефакты CI/CD
- Отчёт pytest (JUnit XML)
- Отчёт покрытия (coverage.xml)
- Логи линтеров (ruff)
- Wheel-пакет (elearning-0.1.0-py3-none-any.whl)

## Артефакты релиза v0.1.0
- Тег v0.1.0
- Исходный код (zip)
- CHANGELOG.md
- README.md