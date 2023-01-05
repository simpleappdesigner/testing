make file - Makefile
    $make Makefile install  --> install the depedencies from requirements.txt
to run test, options are:

$make Makefile testSeleniumUITest --> will run test which are marked as SeleniumUITest


pytest.ini
    this contain rules for searching, i.e which file names, class names or funcion names are considerd for pytest collection.
    pytest.ini , seeting! source https://docs.pytest.org/en/7.1.x/reference/reference.html#ini-options-ref

conftest.py
    contain fixtures

What this boiler plate covers?
1.make file
2.pytest configuration i.e pytest.ini
3. mark - use cases are smoketest,e2e etc
4. parametrization 
5.fixture
6.HTML report


Appendix:
Project_Folder
    Tests
        test_1.py
        test_2.py
    CodeToTest:
        code_file1.py
        Code_file2.py

how to import code in Test files in Test?
1. be in folder 'Project_Folder' and run code - python -m pytest Tests
2. create a setup.py file for CodeToTest,and install. pip install -e .

