from behave import *
import requests
from Utilities.configurations import *
from Utilities.resources import *


@given('Book Details to be added to Library')
def step_impl(context):
    context.url = getconfig()['API']['endpoint'] + apiresources.addbook
    context.headers = {"Content-Type":"application/json"}
    context.addBookPayload = addBookPayload("FGHJ","3256")

@when('Execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url,
                                     json=context.addBookPayload,
                                     headers=context.headers, )
@then('Book is successfully added')
def step_impl(context):
    print(context.response.json())
    resp = context.response.json()
    context.bookid = resp['ID']
    print(context.bookid)
    assert resp['Msg'] == "successfully added"

@given('Book Details with {isbn} and {aisle}')
def step_impl(context,isbn,aisle):
    context.url = getconfig()['API']['endpoint'] + apiresources.addbook
    context.headers = {"Content-Type": "application/json"}
    context.addBookPayload = addBookPayload(isbn, aisle)

@given('I have GITHUB credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('arvindlav', "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")
    context.url2 = getconfig()['API']['url2']
    #print(url)
    #response = se.get(url)
    #print(response.status_code)

@when('I hit GetRepo API of GITHUB')
def step_impl(context):
    context.response = context.se.get(context.url2)

@then('Status code of response should {statusCode:d}')
def step_impl(context,statusCode):
    # print(statusCode)
    # print(context.response.status_code)
    assert context.response.status_code == statusCode

@given('I have GITHUB credentials for checking Branches')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('arvindlav', "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")
    context.url3 = getconfig()['API']['url3']

@when('I hit GetRepo Branch with {owner} and {repo}')
def step_impl(context,owner,repo):
    repository= owner/repo
    print(context.url3+repository)
    context.response = context.se.get(context.url3/repository)

@given('I have Formula One Circuits')
def step_impl(context):
    context.se = requests.session()
    context.url = getconfig()['API']['url4']

@when('I hit Formula One Circuits to get Body')
def step_impl(context):
    context.resp = context.se.get(context.url)
    context.resp_json = context.resp.json()
    print(context.resp_json)
@then('I assert that Circuit ID {circuitid} and {value}')
def step_impl(context,circuitid,value):
    print("--------------------------------------------")
    assert context.resp_json['MRData']['CircuitTable']['Circuits'][20]['circuitId'] == value
    #assert(context.resp_json('[MRData]')) == circuitid