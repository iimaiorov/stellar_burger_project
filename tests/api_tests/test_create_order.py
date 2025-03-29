import allure


class TestCreateOrder:
    @allure.title("Create order")
    def test_create_order(self, api_manager, create_and_register_user):
        ingredients = api_manager.ingredients_api.get_ingredients(expected_status=200).json()
        ingredients_id = [ingredient['_id'] for ingredient in ingredients['data']]
        order = {
            "ingredients": ingredients_id
        }
        response = api_manager.order_api.create_order(order)
        response_data = response.json()
        response_ingredients_id = [ingredient['_id'] for ingredient in response_data['order']['ingredients']]
        assert response_data is not None
        assert response_data['success']
        assert ingredients_id == response_ingredients_id
        assert response_data['order']['owner']['name'] == create_and_register_user.name

    @allure.title("Create order non auth client")
    def test_create_order_non_auth_client(self, api_manager):
        ingredients = api_manager.ingredients_api.get_ingredients(expected_status=200).json()
        ingredients_id = [ingredient['_id'] for ingredient in ingredients['data']]
        order = {
            "ingredients": ingredients_id
        }
        response = api_manager.order_api.create_order(order)
        response_data = response.json()
        assert response_data is not None
        assert response_data['success']
        assert response_data['order']['number'] is not None

    @allure.title("Create order with empty ingredients")
    def test_create_order_with_empty_ingredients(self, api_manager):
        order = {
            "ingredients": []
        }
        response = api_manager.order_api.create_order(order, expected_status=400)
        response_data = response.json()
        assert response_data is not None
        assert not response_data['success']
        assert response_data['message'] == "Ingredient ids must be provided"
