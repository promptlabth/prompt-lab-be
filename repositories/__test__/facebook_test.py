import pytest
from unittest.mock import Mock, patch
from sqlmodel import Session
from model.users.users_model import Users


from repositories.facebook import FacebookRepository

class MockUserModel(Users):
    pass

class TestFacebookRepository:
    @pytest.fixture
    def session_mock(self):
        with patch.object(Session, '__init__', return_value=None) as _mock:
            yield Mock(spec=Session)

    @pytest.fixture
    def facebook_repository(self, session_mock):
        return FacebookRepository(session=session_mock)

    def test_get_facebook_token_by_user_id_returns_token(self, facebook_repository, session_mock):
        test_user_id = "123"
        expected_token = "fake_token"
        user_mock = Mock(spec=MockUserModel)
        user_mock.platform = 'facebook'
        user_mock.access_token = expected_token


        session_mock.exec.return_value.first.return_value = user_mock
        result = facebook_repository.get_facebook_token_by_user_id(test_user_id)

        assert result == expected_token

    def test_get_facebook_token_by_non_facebook_platform(self, facebook_repository, session_mock):
        test_user_id = "123"
        user_mock = Mock(spec=Users)
        user_mock.platform = 'other_platform'

        session_mock.exec.return_value.first.return_value = user_mock
        result = facebook_repository.get_facebook_token_by_user_id(test_user_id)

        assert result is None

    def test_get_facebook_token_by_user_id_no_user_found(self, facebook_repository, session_mock):
        session_mock.exec.return_value.first.return_value = None

        result = facebook_repository.get_facebook_token_by_user_id("non_existent_user_id")

        assert result is None
