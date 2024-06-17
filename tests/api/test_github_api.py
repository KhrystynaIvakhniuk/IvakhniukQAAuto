import pytest
import requests
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api_client):
    user = github_api_client.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_non_exists(github_api_client):
    r = github_api_client.get_user("kristinaivakhniuk")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api_client):
    r = github_api_client.search_repo("become-qa-auto")
    assert r["total_count"] == 58
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api_client):
    r = github_api_client.search_repo("ivakhniuk_repo_non_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api_client):
    r = github_api_client.search_repo("s")
    assert r["total_count"] != 0


@pytest.mark.api
def test_emoji_file_format(github_api_client):
    r = github_api_client.get_emojis()
    assert "1f44d.png" in r["+1"]


@pytest.mark.api
def test_emoji_file_location(github_api_client):
    r = github_api_client.get_emojis()
    assert ".png?v8" in r["100"]


@pytest.mark.api
def test_emoji_link_is_accessible(github_api_client):
    r = github_api_client.get_emojis()
    assert "images/icons/emoji/unicode" in r["1st_place_medal"]


@pytest.mark.api
def test_emoji_status_code(github_api_client):
    r = github_api_client.get_emojis()
    assert requests.get(r["2nd_place_medal"]).status_code == 200


@pytest.mark.api
def test_owner_not_exists(github_api_client):
    owner = 'invalid_owner'
    repo = 'invalid_repo'
    r = github_api_client.search_commit(owner, repo)
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_commit_by_author(github_api_client):
    owner = 'KhrystynaIvakhniuk'
    repo = 'IvakhniukQAAuto'
    r = github_api_client.search_commit(owner, repo)
    author_name = r[0]['commit']['author']['name']
    assert author_name == 'Khrystyna Ivakhniuk'
