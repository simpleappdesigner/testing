# create virtual environment and activate it
install:
	: # pwd
	python3 -m venv .venv
	. .venv/bin/activate && (pip install --upgrade pip && pip install -r requirements.txt; \
		pip list)
	#: python3 --version

test:
	. .venv/bin/activate && (python3 -m pytest -vv -s )

testrunMarkTest:
	. .venv/bin/activate && (python3 -m pytest -vv -s -m runMarkTest)

testSeleniumUITest:
	. .venv/bin/activate && (python3 -m pytest -vv -s -m SeleniumUITest)

testWithHtmlReport:
	. .venv/bin/activate && (python3 -m pytest --html='TestExecutionResult.html' -vv -s )

testWithXMLReport:
	. .venv/bin/activate && (python3 -m pytest --junitxml='TestExecutionResult.xml' -vv -s )


testdistributed:
	: # n4 tries to spawn 4 processes , if n > core, then threads get spawned. -nauto - determines the number
	. .venv/bin/activate && (python3 -m pytest -vv -s -n4 )