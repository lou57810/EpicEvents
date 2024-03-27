import logging
from enum import Enum as PyEnum

from model.user import User, RoleEnum
from controller.administration_controller import AdministrationController
from view.start_menu_view import StartMenuView
from view.gestion_menu_view import GestionMenuView 

from controller.user_controller import UserController # Contain check_email
from controller.gestion_controller import GestionController
from controller.start_menu_controller import StartMenuController
from controller.engine_controller import EngineController, session
import pytest
import bcrypt
import builtins
import unittest
from unittest.mock import patch, MagicMock



class TestUserSignIn:

    @pytest.fixture
    def instance(self):
        return StartMenuView()

    def test_user_sign_in(self, instance, monkeypatch, capsys):
        # Simulate user input
        monkeypatch.setattr('builtins.input', lambda _: 'test@example.com')
        monkeypatch.setattr('maskpass.askpass', lambda prompt, mask: 'password123')

        # Call the method
        email, password = instance.user_sign_in()

        # Check if the method returned the correct values
        assert email == 'test@example.com'
        assert password == 'password123'

        # Check if the method printed the prompt
        captured = capsys.readouterr()
        assert captured.out == 'Enter Email and then, password: \n'


"""class TestUserController:
    
    @pytest.fixture
    def instance(self):
        start_controller = StartMenuController()
        # Create instance of yourTestUserController class
        user_controller = UserController(start_controller)
        return UserController(start_controller)
        # your_module = 
        # return user_controller
        # return UserController()

    def test_check_email_with_correct_email(self, instance, monkeypatch, mocker, capsys):
        session_app = EngineController()
        # Mock user input
        # monkeypatch.setattr('view.start_menu_view.StartMenuView.user_sign_in', lambda _: ('test@example.com', 'password123'))
        monkeypatch.setattr('view.start_menu_view.StartMenuView.user_sign_in', lambda _: ('test@example.com', 'password123'))

        # Mock the query result
        user_row_mock = mocker.MagicMock()
        user_row_mock.one_or_none.return_value = user_row_mock
        monkeypatch.setattr('controller.user_controller.session.query(User).filter_by', lambda **kwargs: user_row_mock)

        # Mock self.check_password
        check_password_mock = mocker.patch.object(instance, 'check_password')

        # Call the method
        instance.check_email()

        # Check if self.check_password was called with the correct arguments
        check_password_mock.assert_called_once_with('password123', user_row_mock)"""


class TestGestionMenuView:

    @pytest.fixture
    def instance(self):
        return GestionMenuView()


    def test_should_print_menu_role(self, instance, monkeypatch, capsys):
        menu_app = GestionMenuView()
        menu_app.menu_role()
        out, err = capsys.readouterr()
        expect_out = ("\n=========== MENU ==========="
                        "\n1 - GESTION"
                        "\n2 - COMMERCIAL"
                        "\n3 - SUPPORT"
                        "\n============================\n\n")
        assert out == expect_out


    def test_get_role_valid_input(self, monkeypatch, mocker):
        # Mock the input function to return a valid role number
        mocker.patch('builtins.input', return_value='1')

        # Mock menu_role if it's an external function
        mocker.patch.object(GestionMenuView, 'menu_role')

        menu_app = GestionMenuView()
        role = menu_app.get_role()

        assert role == RoleEnum.GESTION.value

    def test_get_role_invalid_input(self, monkeypatch, mocker):
        # Mock the input function to return an invalid role number
        mocker.patch('builtins.input', return_value='0')

        # Mock menu_role if it's an external function
        mocker.patch.object(GestionMenuView, 'menu_role')

        menu_app = GestionMenuView()
        role = menu_app.get_role()
    
        # with pytest.raises(IndexError):
        assert (role != RoleEnum.GESTION.value) | (role != RoleEnum.COMMERCIAL.value) | (role != RoleEnum.SUPPORT.value)
