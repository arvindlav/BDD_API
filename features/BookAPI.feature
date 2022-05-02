# Created by SESA243476 at 4/14/2022
Feature: Verify if Books are added and deleted using Library API
  # Enter feature description here
  @library
  Scenario: Verify AddBook API functionality
    Given Book Details to be added to Library
    When Execute the AddBook PostAPI method
    Then Book is successfully added
    And Status code of response should 200

  @library
  Scenario Outline: Verify AddBook API functionality
    Given Book Details with <isbn> and <aisle>
    When Execute the AddBook PostAPI method
    Then Book is successfully added
    Examples:
      |isbn  |aisle |
      |wscx  |2013 |
      |tgvn  |2014  |