# Provide an examle of BDD scenarios for the following user story:
# As a user, I want to be able to add a new contact to my address book, so that I can keep my contacts up to date.

Feature: Add a new contact
  As a user
  I want to be able to add a new contact to my address book
  So that I can keep my contacts up to date

  Scenario: Add a new contact
    Given I am on the new contact page
    When I fill in the form with valid information
    And I click submit
    Then I should see a success message
    And I should see my new contact's information on the page

  # add scenario so that the contact is a variable and phone number
  Scenario: Add a new contact with phone number
    Given I am on the new contact page
    When I fill in the form with valid information
    And I click submit
    Then I should see a success message
    And I should see my new contact's information on the page
    And I should see my new contact's phone number on the page

    # Add scenario outline with 10 examples of valid information for the contact
    # Examples should include first name, last name, phone number, and address
    # Examples should be a mix of male and female names
  Scenario Outline: Add a new contact with valid information
    Given I am on the new contact page
    When I fill in the form with "<first_name>" "<last_name>" "<phone_number>" "<address>"
    And I click submit
    Then I should see a success message
    And I should see my new contact's information on the page
    And I should see my new contact's phone number on the page

    Examples:
    | first_name | last_name | phone_number | address |
    | John       | Smith     | 1234567890   | 123 St  |
    | Jane       | Doe       | 0987654321   | 456 St  |
    | Bob        | Jones     | 1234567890   | 789 St  |
    | Mary       | Smith     | 0987654321   | 123 St  |
    | John       | Doe       | 1234567890   | 456 St  |
    | Jane       | Jones     | 0987654321   | 789 St  |
    | Bob        | Smith     | 1234567890   | 123 St  |
    | Mary       | Doe       | 0987654321   | 456 St  |
    | John       | Jones     | 1234567890   | 789 St  |
    | Jane       | Smith     | 0987654321   | 123 St  |

  # Add a scenario outline so I select the contact first_name
  # The selected contacts will be exported to a CSV file
  Scenario Outline: Export contacts to CSV
    Given I am on the contacts page
    When I select "<first_name>" from the contacts list
    And I click export
    Then I should see a success message

    Examples:
    | first_name |
    | John       |
    | Jane       |
    | Bob        |
    | Mary       |
    | John       |
    | Jane       |
    | Bob        |
    | Mary       |
    | John       |
    | Jane       |

# Add a feature so I can delete a contact when I select a contact name
Feature: Delete a contact
  As a user
  I want to be able to delete a contact from my address book
  So that I can keep my contacts up to date

  Scenario: Delete a contact
    Given I am on the contacts page
    When I select "<first_name>" from the contacts list
    And I click delete
    Then I should see a success message
    And I should not see my new contact's information on the page

    Examples:
    | first_name |
    | John       |
    | Jane       |
    | Bob        |
    | Mary       |
    | John       |
    | Jane       |
    | Bob        |
    | Mary       |
    | John       |
    | Jane       |
