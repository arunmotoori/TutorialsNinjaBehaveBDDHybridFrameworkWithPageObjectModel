Feature: Login Functionality

  @login
  Scenario Outline: Login with valid credentials
    Given I navigated to Login page
    When I enter valid email address as "<email>" and valid password as "<password>" into the fields
    And I click on Login button
    Then I should get logged in
    Examples:
      |email                          |password     |
      |amotoorisampleone@gmail.com    |secondone    |
      |amotoorisampletwo@gmail.com    |secondtwo    |
      |amotoorisamplethree@gmail.com  |secondthree  |


  @login
  Scenario: Login with invalid email and valid password
    Given I navigated to Login page
    When I enter invalid email and valid password say "12345" into the fields
    And I click on Login button
    Then I should get a proper warning message

  @login
  Scenario: Login with valid email and invalid password
    Given I navigated to Login page
    When I enter valid email say "amotoriapril2023sample@gmail.com" and invalid password say "1234567890" into the fields
    And I click on Login button
    Then I should get a proper warning message

  @login
  Scenario: Login with invalid credentials
    Given I navigated to Login page
    When I enter invalid email and invalid password say "1234567890" into the fields
    And I click on Login button
    Then I should get a proper warning message

  @login
  Scenario: Login without entering any credentials
    Given I navigated to Login page
    When I dont enter anything into email and password fields
    And I click on Login button
    Then I should get a proper warning message