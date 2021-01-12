Feature: FizzBuzz Scenarios

  Scenario: 1
    Given I am in the zad01 directory
    When the number is 3
    Then the output should be 'Fizz'

  Scenario: 2
    Given I am in the zad01 directory
    When the number is 5
    Then the output should be 'Buzz'

  Scenario: 3
    Given I am in the zad01 directory
    When the number is 15
    Then the output should be 'FizzBuzz'

  Scenario: 4
    Given I am in the zad01 directory
    When the number is 7
    Then the output should be ':('

  Scenario: 5
    Given I am in the zad01 directory
    When the number is String
    Then the output should be 'ValueError'

