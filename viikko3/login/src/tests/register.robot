*** Settings ***
Resource      resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  testi
    Set Password  1234567890
    Set Password   Confirmation 1234567890
    Click Button  Register
    Main Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username   te
    Set Password    1234567890
    Set Password Confirmation   1234567890
    Click Button   Register
    User Should See Error Message   Invalid username or password

Register With Valid Username And Too Short Password
    Set Username   testi1234
    Set Password   1
    Set Password Confirmation  1
    Click Button   Register
    User Should See Error Message  Invalid username or password

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  testi1234
    Set Password  hihii
    Set Password  Confirmation hihii
    Click Button  Register
    User Should See Error Message  Invalid username or password

Register With Nonmatching Password And Password Confirmation
# ...
    Set Username  testi1234
    Set Password  1234567890
    Set Password Confirmation  123456789000
    Click Button  Register
    User Should See Error Message  Invalid username or password

Register With Username That Is Already In Use
    Create User    banaani1
    Set Username  banaani1
    Set Password  salasana1234
    Set Password Confirmation  salasana1234
    Click Button  Register
    User Should See Error Message  Invalid username or password

*** Keywords ***
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