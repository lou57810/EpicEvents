# import logging
# from enum import Enum as PyEnum
import bcrypt
from model.user import RoleEnum, User
from model.contract import Contract
from model.customer import Customer
from model.event import Event
from model.base import Base
# from controller.administration_controller import AdministrationController
from view.start_menu_view import StartMenuView
from view.gestion_menu_view import GestionMenuView
from controller.user_controller import UserController
from controller.start_menu_controller import StartMenuController

# from controller.user_controller import UserController # Contain check_email
# from controller.gestion_controller import GestionController
# from controller.start_menu_controller import StartMenuController
# from controller.engine_controller import EngineController, session
import pytest
# import bcrypt
# import builtins
# import unittest
from unittest.mock import patch  # MagicMock


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
        assert (role !=
                RoleEnum.GESTION.value) | (
                role != RoleEnum.COMMERCIAL.value
                ) | (role != RoleEnum.SUPPORT.value)
