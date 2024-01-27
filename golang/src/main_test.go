package main

import "github.com/cucumber/godog"

func aPageTitledExists(arg1 string) error {
	return godog.ErrPending
}

func aRunningServer() error {
	return godog.ErrPending
}

func iMakeAGETRequestTo(arg1 string) error {
	return godog.ErrPending
}

func iMakeAPOSTRequestToWithBody(arg1, arg2 string) error {
	return godog.ErrPending
}

func theResponseBodyShouldContain(arg1 string) error {
	return godog.ErrPending
}

func theResponseBodyShouldContainAnEditForm() error {
	return godog.ErrPending
}

func theResponseBodyShouldContainTheOriginalContentOf(arg1 string) error {
	return godog.ErrPending
}

func theResponseShouldRedirectTo(arg1 string) error {
	return godog.ErrPending
}

func theResponseStatusShouldBe(arg1 int) error {
	return godog.ErrPending
}

func InitializeScenario(ctx *godog.ScenarioContext) {
	ctx.Step(`^a page titled "([^"]*)" exists$`, aPageTitledExists)
	ctx.Step(`^a running server$`, aRunningServer)
	ctx.Step(`^I make a GET request to "([^"]*)"$`, iMakeAGETRequestTo)
	ctx.Step(`^I make a POST request to "([^"]*)" with body "([^"]*)"$`, iMakeAPOSTRequestToWithBody)
	ctx.Step(`^the response body should contain "([^"]*)"$`, theResponseBodyShouldContain)
	ctx.Step(`^the response body should contain an edit form$`, theResponseBodyShouldContainAnEditForm)
	ctx.Step(`^the response body should contain the original content of "([^"]*)"$`, theResponseBodyShouldContainTheOriginalContentOf)
	ctx.Step(`^the response should redirect to "([^"]*)"$`, theResponseShouldRedirectTo)
	ctx.Step(`^the response status should be (\d+)$`, theResponseStatusShouldBe)
}
