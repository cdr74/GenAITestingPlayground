Feature: School Management
  As a school administrator
  I want to manage students, teachers, and courses
  So that I can run the school efficiently

  Scenario: Add a new student
    Given a student with name "John", age "20", address "123 Street", phone "1234567890", student_id "S001", and courses "Math, Science"
    When I add the student to the school
    Then the student should be added to the school's student list

  Scenario: Add a new teacher
    Given a teacher with name "Jane", age "30", address "456 Avenue", phone "0987654321", teacher_id "T001", and courses "Math, English"
    When I add the teacher to the school
    Then the teacher should be added to the school's teacher list

  Scenario: Add a new course
    Given a course with course_id "C001", course_name "Math", teacher_id "T001", and students "John, Jane"
    When I add the course to the school
    Then the course should be added to the school's course list

  Scenario Outline: Add a new person
    Given a <role> with name "<name>", age "<age>", address "<address>", phone "<phone>", id "<id>", and courses "<courses>"
    When I add the <role> to the school
    Then the <role> should be added to the school's <role> list

    Examples:
      | role    | name | age | address   | phone     | id  | courses         |
      | student | John | 20  | 123 St    | 123456789 | S01 | Math, Science   |
      | teacher | Jane | 30  | 456 Ave   | 987654321 | T01 | English, History|

  # Add a scenario outline to create a new course
  Scenario Outline: Add a new course
    Given a course with course_id "<course_id>", course_name "<course_name>", teacher_id "<teacher_id>", and students "<students>"
    When I add the course to the school
    Then the course should be added to the school's course list

    Examples:
      | course_id | course_name | teacher_id | students         |
      | C01       | Math        | T01        | John, Jane       |
      | C02       | English     | T02        | John, Jane, Mary |

  # Add a scenario outline to remove a student from a course
  Scenario Outline: Remove a student from a course
    Given a course with course_id "<course_id>", course_name "<course_name>", teacher_id "<teacher_id>", and students "<students>"
    When I remove the student "<student>" from the course
    Then the student "<student>" should be removed from the course

    Examples:
      | course_id | course_name | teacher_id | students         | student |
      | C01       | Math        | T01        | John, Jane       | John    |
      | C02       | English     | T02        | John, Jane, Mary | Jane    |


  # As administrator I can set the location of a course
  Scenario: Set the location of a course
    Given a course with course_id "C01", course_name "Math", teacher_id "T01", and students "John, Jane"
    When I set the location of the course to "Room 101"
    Then the location of the course should be "Room 101"
  
  # Same but with a scenario outline that will contains 2 variables, the <course_id> and the <location>
  Scenario Outline: Set the location of a course
    Given a course with course_id "<course_id>"
    When I set the location of the course to "<location>"
    Then the location of the course should be "<location>"

    Examples:
      | course_id | location  |
      | C01       | Room 101  |
      | C02       | Room 102  |
