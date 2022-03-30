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

make lint: #запуск flake8
	poetry run flake8 brain_games

brain-even: #запуск четного
	poetry run brain-even

brain-calc: #запуск калькулятора
	poetry run brain-calc

brain-gcd: #запуск НОД
	poetry run brain-gcd

brain-progression: #запуск прогрессий
	poetry run brain-progression