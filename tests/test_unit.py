from controller.administration_controller import AdministrationController
from view.start_menu_view import StartMenuView
from controller.user_controller import UserController
from controller.gestion_controller import GestionController
from controller.start_menu_controller import StartMenuController
import pytest
import bcrypt
from unittest.mock import patch



"""def test_check_email_is_ok():
    sut = UserController()
    input_email = 'admin@localhost'
    expected_value = 'Email correct!'
    assert sut.check_email == expected_value


def test_check_password_is_ok():
    sut = UserController(start_controller)
    input_password = 'admin'
    expected_value = 'Password correct!'
    assert sut.check_password == expected_value


def test_db():
    sut = AdministrationController()    # sut: system under test
    db_name = 'db_test'
    expected_value = True
    assert sut.add_database(db_name) == 'True'


def test_check_password():
    test_app = UserController()
    with patch('logging.info') as mock_logging:
        #with patch('bcrypt.hashpw') as mock_hashpw:
            # mock_hashpw.return_value = b'hashed_password_mock'
        result = test_app.sign_in()
            
        # Assertions
        assert result == True
        mock_logging.assert_called_once_with("You are logged!")
"""

def test_create_user():
    start_menu_controller = StartMenuController()
    gestion_controller = GestionController()
    # start_menu_controller.user_controller.create_user()

    with patch('logging.info') as mock_logging:
        with patch('bcrypt.hashpw') as mock_hashpw:
            mock_hashpw.return_value = b'hashed_password_mock'
            result = start_menu_controller.gestion_controller.create_user()
            
            # Assertions
            assert result == b'hashed_password_mock'
            mock_logging.assert_called_once_with("This is a creation test message")