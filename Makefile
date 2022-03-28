# Makefile

install: # установить зависимости
	poetry install

brain-games: #запуск проекта
	poetry run brain-games

build: #сборка
	poetry build

publish: #публикация
	poetry publish --dry-run

package-install: #пакет
	python3 -m pip install dist/hexlet_code-0.1.0-py3-none-any.whl