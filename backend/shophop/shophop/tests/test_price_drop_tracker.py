import unittest
from unittest.mock import patch, MagicMock
from django.test import Client
from rest_framework import status
from django.urls import reverse
import pandas as pd
from ..views import price_drop_tracker
from ..models import User, productData, SavedItem
import json
from shophop.views.updated_price_drop_tracker import update_saved_items_db, get_users_saved_data


class PriceDropTrackerTests(unittest.TestCase):
    def setUp(self):
        """Set up initial test data."""
        User.objects.all().delete()
        self.user1 = User.objects.create(
            username="testuser1@example.com",  
            email="testuser1@example.com",
            first_name="Test",
            last_name="User1",
            registration_method="google"
        )
        self.user2 = User.objects.create(
            username="testuser2@example.com",  
            email="testuser2@example.com",
            first_name="Test",
            last_name="User2",
            registration_method="google"
        )

        # Create saved items for users
        SavedItem.objects.create(user=self.user1, name="Potato", price=2.0)
        SavedItem.objects.create(user=self.user1, name="Tomato", price=3.0)
        SavedItem.objects.create(user=self.user2, name="Onion", price=1.5)

        # Create product data for cheapest prices
        productData.objects.create(category="Potato", price=1.5)
        productData.objects.create(category="Tomato", price=2.5)
        productData.objects.create(category="Onion", price=1.0)

        self.client = Client()
    

    def test_update_saved_items_db(self):
        """Test the update_saved_items_db function."""
        # Prepare a mock mailing list
        mailing_list = {
            "testuser1@example.com": [
                {"name": "Potato", "old_price": 2.0, "new_price": 1.5, "store": "Store A", "product": "Fresh Potatoes"},
                {"name": "Tomato", "old_price": 3.0, "new_price": 2.5, "store": "Store B", "product": "Fresh Tomatoes"}
            ]
        }

        # Call the update_saved_items_db function
        
        update_saved_items_db(mailing_list)

        # Verify that the saved items are updated in the database
        saved_potato = SavedItem.objects.get(user=self.user1, name="Potato")
        saved_tomato = SavedItem.objects.get(user=self.user1, name="Tomato")

        self.assertEqual(saved_potato.price, 1.5)
        self.assertEqual(saved_tomato.price, 2.5)


    def test_get_users_saved_data(self):
        """Test get_users_saved_data function."""
        # Call the function
        result = get_users_saved_data()

        # Expected result
        expected_result = [
            {"user": "testuser1@example.com", "name": "Potato", "price": 2.0},
            {"user": "testuser1@example.com", "name": "Tomato", "price": 3.0},
            {"user": "testuser2@example.com", "name": "Onion", "price": 1.5},
        ]

        # Assert the result matches the expected output
        self.assertEqual(result, expected_result)


    def tearDown(self):
        """Clean up after tests."""
        User.objects.all().delete()
        SavedItem.objects.all().delete()
        productData.objects.all().delete()