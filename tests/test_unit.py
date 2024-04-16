from model.user import RoleEnum
from view.gestion_menu_view import GestionMenuView
from controller.engine_controller import EngineController
import pytest
from unittest.mock import patch  # MagicMock


@patch('controller.engine_controller.create_engine')
def test_start_engine(mock_create_engine):
    # Instanciation EngineController
    engine_controller = EngineController()

    # Comportement attendu du mock de create_engine
    db_name = 'test_db'
    expected_url = "mysql+pymysql://root:edwood@localhost/" + db_name
    mock_engine = mock_create_engine.return_value

    # Appel de la méthode start_engine avec un nom de base de données
    result = engine_controller.start_engine(db_name)

    # Assert 'create_engine' appelé avec les bons paramètres
    mock_create_engine.assert_called_once_with(expected_url)

    # Résultat attendu de create_engine
    assert result == mock_engine


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

        assert (role !=
                RoleEnum.GESTION.value) | (
                role != RoleEnum.COMMERCIAL.value
                ) | (role != RoleEnum.SUPPORT.value)
