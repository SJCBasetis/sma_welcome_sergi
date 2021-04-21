:: delete old coverage
coverage erase

:: run tests
nosetests --with-coverage --cover-package=src --cover-html

pause