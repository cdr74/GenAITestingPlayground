# Experience with co-pilot creatign a godog based test suite

This experiment shows a rather naive way of dealing with co-pilot and is probably a good example of a beginner interaction with co-pilot. 

## Creating the feature file

Based on the code of the server the wiki.features have been created with the promt: 
"can you create a bdd (gherkin) style test suite for this application covering the edit, view and re-edit flow"

Result: wiki.features has been created

Assessment: it's covering what was requested, but misses many aspects of a comprehensive test suite (eg negative flows)

## Implementing the tests

Based on the wiki.features definition the test code has been created with the prompt:
"please create the code necessary to implement all tests defined in wiki.features"

The code generated did use deprecated types and had skelleton in it; fairly hard to recover from there. 

Backtracking and running "godog run wiki.features" provides a valid skelleton.

Trying again with co-pilot to continue from here with the prompt
"implement the actual functionality in main_test.go skelleton code to perform tests for the wiki server implemented in main.go"

Result: did absolutly nothing useful to the already existing skelleton code. 

