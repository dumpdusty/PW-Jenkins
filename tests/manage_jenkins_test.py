import time
from playwright.sync_api import sync_playwright, expect


def test_verify_manage_jenkins_link(page):
    page.goto("/")
    
    with page.expect_response(lambda response: response.status) as response_info:
        page.locator('#root-action-ManageJenkinsAction').click()
    
    
    assert response_info.value.status == 302
        
    expect(page).to_have_url("http://localhost:8080/manage/")