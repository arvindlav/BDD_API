# Created by SESA243476 at 4/22/2022
Feature: Formula One
  # Enter feature description here

  Scenario Outline: Formula One Circuit ID
    Given I have Formula One Circuits
    When I hit Formula One Circuits to get Body
    Then I assert that Circuit ID <circuit id> and <value>
    Examples:
      |circuit id|value|
      |20        |estoril|

    # Enter steps here