from behave import *
from assertpy import *


use_step_matcher("re")

@given(u'one  number')
def step_impl(context):
    context.digits = context.text


@when(u'the number is divided by 15')
def step_impl(context):
    context.wynik = int(context.digits) // 15


@then(u'the output should be 101')
def step_impl(context):
    assert_that(context.wynik).is_equal_to(101)


@given(u'one number')
def step_impl(context):
    context.digits = context.text


@when(u'the number is divided by 2')
def step_impl(context):
    context.wynik = int(context.digits) // 2


@then(u'the output should be 1000')
def step_impl(context):
    assert_that(context.wynik).is_equal_to(1000)


@given(u'two numbers')
def step_impl(context):
    context.digits = context.text.split(",")


@when(u'one number is divided by other number')
def step_impl(context):
    context.wynik = int(context.digits[0]) // int(context.digits[1])


@then(u'the output should be 5')
def step_impl(context):
    assert_that(context.wynik).is_equal_to(5)


@when(u'the number is not dividable by other number')
def step_impl(context):
    context.wynik = int(context.digits[0]) / int(context.digits[1])


@then(u'the output should be instance of float')
def step_impl(context):
    assert_that(isinstance(context.wynik, float)).is_equal_to(True)


@when(u'the one number is longer than other')
def step_impl(context):
    if len(context.digits[0]) > len(context.digits[1]):
        context.wynik = "longer"
    else:    
        context.wynik = "shorter"

@then(u'the output should be "longer"')
def step_impl(context):
    assert_that(context.wynik).is_equal_to("longer")


@when(u'the one number is shorter than other')
def step_impl(context):
    if len(context.digits[0]) < len(context.digits[1]):
        context.wynik = "shorter"
    else:    
        context.wynik = "longer"


@then(u'the output should be "shorter"')
def step_impl(context):
    assert_that(context.wynik).is_equal_to("shorter")


