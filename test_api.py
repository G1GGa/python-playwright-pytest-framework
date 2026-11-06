from playwright.sync_api import APIRequestContext

def test_create_user(playwright):
    api_context: APIRequestContext = playwright.request.new_context(
        base_url="https://reqres.in"
    )

    payload = {"name": "Giga", "job": "SDET"}
    response = api_context.post("/api/users", data=payload)

    assert response.status == 201
    data = response.json()
    assert data["name"] == "Giga"
    assert "io" in data

    print(f"\n[API Test Passed] Created User ID: {data['id']}")