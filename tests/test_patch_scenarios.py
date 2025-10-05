
'''
Validate patch test with valid payload data
Invalid payload returns 200
Payload data should matched with response data
'''
def test_patch_valid_payload_data(http_client, created_object_id):
    payload = {"name": "Apple MacBook Pro 16"}
    #payload_patch = json.dumps({"name": "Apple AirPods"})

    response = http_client.patch(f"objects/{created_object_id}", json=payload)
    print(f"Response {str(response)}")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["name"] == "Apple MacBook Pro 16"
    assert json_data["data"]["year"] == 2025
    assert json_data["data"]["price"] == 1949.99

'''
Validate patch test with nested payload
Invalid payload returns 200
Payload data should matched with response data
'''
def test_patch_update_nested_data(http_client, created_object_id):
    payload = {"data": {"year": 2026}}
    response = http_client.patch(f"objects/{created_object_id}", json=payload)
    assert response.status_code == 200
    assert response.json()["data"]["year"] == 2026

'''
Validate patch test with invalid payload id
Invalid payload returns 404 or 400
Empty payload behavior may vary depending on API design
'''
def test_patch_invalid_object_id(http_client):
    response = http_client.patch("objects/99999", json={"name": "Ghost"})
    assert response.status_code in [400, 404]

'''
Validate patch test with invalid field
Invalid payload returns 404 or 400 depending on API design
'''
def test_patch_invalid_field(http_client, created_object_id):
    payload = {"unknownField": "value"}
    response = http_client.patch(f"objects/{created_object_id}", json=payload)
    assert response.status_code in [400, 404]

'''
Validate patch test with empty payload
Invalid payload returns 404 or 400
Empty payload behavior may vary depending on API design
'''
def test_patch_empty_payload(http_client, created_object_id):
    expected_error = "No valid field(s) to update have been passed as part of a request body."
    response = http_client.patch(f"objects/{created_object_id}", json={})
    print(f" response: {response.text}")
    assert response.status_code in [400, 404]
    assert response.json()["error"] == expected_error

'''
Validate patch test with wrong header
Invalid payload returns 404 or 415 depends on API behaviour
'''
def test_patch_wrong_content_type(http_client, created_object_id):
    payload = {"name": "Wrong Header"}
    response = http_client.patch(
        f"objects/{created_object_id}",
        json=payload,
        headers={"Content-Type": "text/plain"}
    )
    assert response.status_code in [415]

'''
Validate patch test with null payload
Invalid payload returns 404 or 400 may depending on API design
'''
def test_patch_with_null_value(http_client, created_object_id):
    payload = {"name": None}
    response = http_client.patch(f"objects/{created_object_id}", json=payload)
    assert response.status_code in [400, 404]  # Depends on API behavior

