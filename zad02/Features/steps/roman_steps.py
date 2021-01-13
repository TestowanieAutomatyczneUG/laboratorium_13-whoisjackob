from behave import *
from Roman import Roman
from assertpy import *


@given(u'I am in the zad02 directory')
def step_impl(context):
    context.roman = Roman()


@when(u'the number is 4')
def step_impl(context):
    context.wynik = context.roman.roman(4)


@then(u'the output should be "IV"')
def step_impl(context):
    assert_that(context.wynik).is_equal_to("IV")


@when(u'the number is 9')
def step_impl(context):
    context.wynik = context.roman.roman(9)


@then(u'the output should be "IX"')
def step_impl(context):
    assert_that(context.wynik).is_equal_to("IX")


@when(u'the number is 48')
def step_impl(context):
    context.wynik = context.roman.roman(48)


@then(u'the output should be "XLVIII"')
def step_impl(context):
    assert_that(context.wynik).is_equal_to("XLVIII")


@when(u'the number is 141')
def step_impl(context):
    context.wynik = context.roman.roman(141)


@then(u'the output should be "CXLI"')
def step_impl(context):
    assert_that(context.wynik).is_equal_to("CXLI")


@when(u'the number is 402')
def step_impl(context):
    context.wynik = context.roman.roman(402)


@then(u'the output should be "CDII"')
def step_impl(context):
    assert_that(context.wynik).is_equal_to("CDII")


@when(u'the number is 3000')
def step_impl(context):
    context.wynik = context.roman.roman(3000)


@then(u'the output should be "MMM"')
def step_impl(context):
    assert_that(context.wynik).is_equal_to("MMM")


@when(u'the number is 911')
def step_impl(context):
    context.wynik = context.roman.roman(911)


@then(u'the output should be "CMXI"')
def step_impl(context):
    assert_that(context.wynik).is_equal_to("CMXI")


@when(u'the number is 59')
def step_impl(context):
    context.wynik = context.roman.roman(59)


@then(u'the output should be "LIX"')
def step_impl(context):
    assert_that(context.wynik).is_equal_to("LIX")
