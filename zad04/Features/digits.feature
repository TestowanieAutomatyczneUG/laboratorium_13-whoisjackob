Feature: Number dividing

  @digits
  Scenario: 1
    Given one  number
    """
    1515
    """
    When the number is divided by 15
    Then the output should be 101

  @digits
  Scenario: 2
    Given one number
    """
    2000
    """
    When the number is divided by 2
    Then the output should be 1000

  @digits
  Scenario: 3
    Given two numbers
    """
    150,30
    """
    When one number is divided by other number
    Then the output should be 5

  @digits
  Scenario: 4
    Given two numbers
    """
    150,40
    """
    When the number is not dividable by other number
    Then the output should be instance of float

  @digits
  Scenario: 5
    Given two numbers
    """
    30000,1
    """
    When the one number is longer than other
    Then the output should be "longer"

  @digits
  Scenario: 6
    Given two numbers
    """
    1,3000
    """
    When the one number is shorter than other
    Then the output should be "shorter"

  @digits
  Scenario: 7
    Given two numbers
    """
    30000,3000
    """
    When one number is divided by other number
    Then the output should be 1

  @digits
  Scenario: 8
    Given two numbers
    """
    30000,3
    """
    When one number is divided by 3
    Then the output should be 1000

