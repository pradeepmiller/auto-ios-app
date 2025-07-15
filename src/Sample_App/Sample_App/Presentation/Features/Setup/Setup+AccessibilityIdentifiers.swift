
/*
 * Copyright (c) 2025 by Sample App. All Rights Reserved.
 */

import Foundation

extension Setup {
    enum Accessibility {
        enum WelcomeScreen: String, RawRepresentable {
            case WELCOME_SCREEN_TEXT_HEADER = "welcome_screen_text_header"
            case WELCOME_SCREEN_TEXT_DESCRIPTION = "welcome_screen_text_description"
            case WELCOME_SCREEN_BUTTON_CONTINUE = "welcome_screen_button_continue"
        }

        enum LoginScreen: String, RawRepresentable {
            case LOGIN_SCREEN_TEXT_HEADER = "login_screen_text_header"
            case LOGIN_SCREEN_INPUT_EMAIL = "login_screen_input_email"
            case LOGIN_SCREEN_INPUT_PASSWORD = "login_screen_input_password"
            case LOGIN_SCREEN_BUTTON_SUBMIT = "login_screen_button_submit"
        }
    }
}
