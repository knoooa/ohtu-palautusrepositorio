*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}        localhost:5001
${DELAY}         0.5 seconds
${HOME_URL}      http://${SERVER}
${LOGIN_URL}     http://${SERVER}/login
${REGISTER_URL}  http://${SERVER}/register
${BROWSER}       chrome
${HEADLESS}      false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
        Call Method  ${options}  add_argument  --incognito
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
        Call Method  ${options}  add_argument  --private-window
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0.05 seconds
        Call Method  ${options}  add_argument  --headless
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}


Register Page Should Be Open
    Title Should Be    Register

Go To Starting Page
    Go To    ${HOME_URL}

Login Page Should Be Open
    Title Should Be  Login

Main Page Should Be Open
    Title Should Be  Ohtu Application main page

Go To Login Page
    Go To  ${LOGIN_URL}

Set Username
    [Arguments]  ${username}
    Input Text    id=username    ${username}

Set Password
    [Arguments]  ${password}
    Input Password    id=password    ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password    id=password_confirmation    ${password}

User Should See Error Message
    [Arguments]  ${message}
    Page Should Contain    ${message}

Go To Register Page
    Go To    http://localhost:5001/register
    Wait Until Element Is Visible    id=username    5s

Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page