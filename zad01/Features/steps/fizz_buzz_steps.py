from behave import *
from FizzBuzz import FizzBuzz
from assertpy import *

@given(u'I am in the zad01 directory')
def step_impl(context):
    context.fizzbuzz = FizzBuzz()


@when(u'the number is 3')
def step_impl(context):
    context.wynik = context.fizzbuzz.game(3)


@then(u'the output should be \'Fizz\'')
def step_impl(context):
    assert_that(context.wynik).is_equal_to("Fizz")


@when(u'the number is 5')
def step_impl(context):
    context.wynik = context.fizzbuzz.game(5)


@then(u'the output should be \'Buzz\'')
def step_impl(context):
    assert_that(context.wynik).is_equal_to("Buzz")


@when(u'the number is 15')
def step_impl(context):
    context.wynik = context.fizzbuzz.game(15)


@then(u'the output should be \'FizzBuzz\'')
def step_impl(context):
    assert_that(context.wynik).is_equal_to("FizzBuzz")


@when(u'the number is 7')
def step_impl(context):
    context.wynik = context.fizzbuzz.game(7)


@then(u'the output should be \':(\'')
def step_impl(context):
    assert_that(context.wynik).is_equal_to(":(")


@when(u'the number is String')
def step_impl(context):
    context.wynik = context.fizzbuzz.game("jakis_string")


@then(u'the output should be \'ValueError\'')
def step_impl(context):
    assert_that(context.wynik).is_equal_to(ValueError)
