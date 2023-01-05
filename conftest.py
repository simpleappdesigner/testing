from selenium import webdriver
from pytest import fixture

# fixture, scope 'function' fixture for every function. 
# Possible values for scope are: function, class, module, package or session.
@fixture(scope='function')
def chrome_browser():
    return webdriver.Chrome()