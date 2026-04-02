# Project 6: API Testing with Playwright
# Site: https://jsonplaceholder.typicode.com

import pytest
from playwright.sync_api import APIRequestContext, Playwright


class TestUsersAPI:

    def test_get_single_user(self, api_request):
        """
        SCENARIO: Get a single user by ID
        GIVEN the API is available
        WHEN I send GET request to /users/1
        THEN I should get status 200
        AND user name should be "Leanne Graham"
        """
        # ACT
        response = api_request.get("/users/1")
        
        # ASSERT - status code
        assert response.status == 200, f"Expected 200 but got {response.status}"
        
        # ASSERT - response body
        body = response.json()
        assert body["id"] == 1
        assert body["name"] == "Leanne Graham"
        assert body["email"] == "Sincere@april.biz"
        
        print(f"✅ Got user: {body['name']}")

    def test_get_all_users(self, api_request):
        """
        SCENARIO: Get all users
        WHEN I send GET request to /users
        THEN I should get status 200
        AND response should contain 10 users
        """
        # ACT
        response = api_request.get("/users")
        
        # ASSERT
        assert response.status == 200
        
        body = response.json()
        assert len(body) == 10, f"Expected 10 users but got {len(body)}"
        
        print(f"✅ Got {len(body)} users!")

    def test_create_user(self, api_request):
        """
        SCENARIO: Create a new user
        WHEN I send POST request with user data
        THEN I should get status 201
        AND response should contain the new user
        """
        # ARRANGE - data to send
        new_user = {
            "name": "Steve Tawali",
            "username": "stevetawali",
            "email": "steve@test.com"
        }
        
        # ACT
        response = api_request.post(
            "/users",
            data=new_user
        )
        
        # ASSERT
        assert response.status == 201, f"Expected 201 but got {response.status}"
        
        body = response.json()
        assert body["name"] == "Steve Tawali"
        assert body["email"] == "steve@test.com"
        
        print(f"✅ Created user with id: {body['id']}")

    def test_update_user(self, api_request):
        """
        SCENARIO: Update an existing user
        WHEN I send PUT request with updated data
        THEN I should get status 200
        AND response should contain updated data
        """
        # ARRANGE
        updated_data = {
            "name": "Steve Updated",
            "email": "updated@test.com"
        }
        
        # ACT
        response = api_request.put(
            "/users/1",
            data=updated_data
        )
        
        # ASSERT
        assert response.status == 200
        
        body = response.json()
        assert body["name"] == "Steve Updated"
        
        print(f"✅ Updated user: {body['name']}")

    def test_delete_user(self, api_request):
        """
        SCENARIO: Delete a user
        WHEN I send DELETE request to /users/1
        THEN I should get status 200
        """
        # ACT
        response = api_request.delete("/users/1")
        
        # ASSERT
        assert response.status == 200
        
        print("✅ User deleted successfully!")