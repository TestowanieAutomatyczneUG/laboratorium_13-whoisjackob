from behave import *
from Roman import Roman

def before_scenario(context, scenario):
    context.c = Roman

def after_scenario(context, scenario):
    context.c = None