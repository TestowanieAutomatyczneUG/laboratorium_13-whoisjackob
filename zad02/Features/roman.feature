Feature: Roman Scenarios

  Scenario: 1
    Given I am in the zad02 directory
    When the number is 4
    Then the output should be "IV"

  Scenario: 2
    Given I am in the zad02 directory
    When the number is 9
    Then the output should be "IX"

  Scenario: 3
    Given I am in the zad02 directory
    When the number is 48
    Then the output should be "XLVIII"

  Scenario: 4
    Given I am in the zad02 directory
    When the number is 141
    Then the output should be "CXLI"

  Scenario: 5
    Given I am in the zad02 directory
    When the number is 402
    Then the output should be "CDII"

  Scenario: 6
    Given I am in the zad02 directory
    When the number is 3000
    Then the output should be "MMM"

  Scenario: 7
    Given I am in the zad02 directory
    When the number is 911
    Then the output should be "CMXI"

  Scenario: 8
    Given I am in the zad02 directory
    When the number is 59
    Then the output should be "LIX"

