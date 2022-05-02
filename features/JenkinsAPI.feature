# Created by SESA243476 at 4/15/2022
Feature: GITHUB API Validation
  # Enter feature description here

  Scenario: Session Management Check
    Given I have GITHUB credentials
    When I hit GetRepo API of GITHUB
    Then Status code of response should 200