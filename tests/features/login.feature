Feature: As the administrator of Flaskr
  I want to be able to use my credentials
  To login to the application.

  Scenario: login
    Given I login with "admin" and "default"
    Then I receive the message "You were logged in"
    
