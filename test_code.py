from code_oops import *
from pytest import mark
import time
def test_hello_bioler_plate_helloWorld():
    assert True

def quality_hello_bioler_plate_helloWorld():
    assert True

@mark.runMarkTest
def test_boiler_plate_mark():
    assert True

@mark.runMarkTest
@mark.parametrize("name,letter_count",[('simple',6),('simpl',4)])
def test_boiler_plate_mark_parameterized(name,letter_count):
    assert len(name) == letter_count

@mark.parametrize("filter",[10,20])
def test_is_instance_and_wrapper(filter):
    a = A('1')
    my_word = MyWord('10')
    assert isinstance(my_word._conv_bn_activation(20)(str),str),f'failed for {filter}' # Right way! called my_word._conv_bn_activation(20)(str) with (str)

@mark.SeleniumUITest
class SeleniumAndFixtureTest:
    def test_access_pythonanywhere_and_check_website_is_up(self,chrome_browser):
        chrome_browser.get('https://simpleappdesigner.pythonanywhere.com/')
        assert chrome_browser.title == 'Simpleappdesigner - tools'
        time.sleep(3)
    def test_access_ip_and_user_agent(self,chrome_browser):
        chrome_browser.get('http://digialert.in/SUdata/get_ip_and_agent')
        assert True
        time.sleep(3)