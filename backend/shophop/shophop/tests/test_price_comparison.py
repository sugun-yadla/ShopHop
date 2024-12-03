import unittest
from django.test import Client
from rest_framework import status
from django.urls import reverse
import pandas as pd
from ..views import price_comparison
import json

class ProductFetchTests(unittest.TestCase):
    
    def setUp(self):
        self.client = Client()

    def test_fetch_products_basic_api_check(self):

        product_query = 'milk'
        response = self.client.get(reverse('fetch-products', args=[product_query]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertIsInstance(response_data, list)
        
        aldi_products = [item for item in response_data if item['store'] == 'Aldi']
        walmart_products = [item for item in response_data if item['store'] == 'Walmart']

        self.assertGreater(len(aldi_products), 0, "No Aldi products found")
        self.assertGreater(len(walmart_products), 0, "No Walmart products found")
    
    def test_fetch_single_product_with_nonexisting_data(self):
        
        product_query = "birthfydy"
        response = self.client.get(reverse('fetch-products', args=[product_query]))
        response_data = response.json()
        #print(response.status_code)
        assert response.status_code != 200
    
    def test_multiple_products(self):
        product_query = "milk, cheese, birthfydy"
        response = self.client.get(reverse('fetch-products', args=[product_query]))
        response_data = response.json()
        assert response.status_code == 200
    
    def test_only_show_data_having_all_fields(self):
        mock_test_data = pd.DataFrame([{'Product': 'fairlife Lactose Free Fat Free Ultra Filtered Milk', 'Price': None, 'Quantity': None, 'Category': 'milk', 'store': 'Walmart'}, 
                                 {'Product': 'fairlife Lactose Free Ultra Filtered Whole Milk', 'Price': 4.97, 'Quantity': '52 fl oz', 'Category': 'milk', 'store': 'Walmart'}, 
                                 {'Product': 'Silk Dairy Free', 'Price': 3.34, 'Quantity': '64 fl oz Half Gallon', 'Category': 'milk', 'store': 'Walmart'}, 
                                 {'Product': 'fairlife Lactose Free Ultra Filtered Whole Milk', 'Price': 4.97, 'Quantity': '52 fl oz', 'Category': 'milk', 'store': 'Walmart'}, 
                                 {'Product': 'fairlife Lactose Free Fat Free Ultra Filtered Milk', 'Price': 4.97, 'Quantity': '52 fl oz', 'Category': 'milk', 'store': 'Walmart'},
                                 {'Product': None, 'Price': 2.98, 'Quantity': '64 fl oz Half Gallon', 'Category': 'milk', 'store': 'Aldi'}, 
                                 {'Product': 'Great Value Whole Vitamin D Milk', 'Price': 3.52, 'Quantity': '128 Fl Oz', 'Category': 'milk', 'store': 'Aldi'}, 
                                 {'Product': 'Great Value', 'Price': None, 'Quantity': 'Refrigerated', 'Category': 'milk', 'store': 'Aldi'}, 
                                 {'Product': 'Great Value Milk Whole Vitamin D', 'Price': 2.12, 'Quantity': None, 'Category': 'milk', 'store': 'Aldi'}, 
                                 {'Product': 'Great Value Milk', 'Price': 2.12, 'Quantity': '64 fl oz Jug', 'Category': 'milk', 'store': 'Aldi'}])
        
        filtered_data = price_comparison.data_cleaning(mock_test_data)
        response_data = json.loads(filtered_data.content) 
        filtered_data_df = pd.DataFrame(response_data)
        assert filtered_data_df.isnull().sum().sum() == 0, "Filtered data contains None or NaN values"

    # to add
    # check if None getting assigned properly through automation
    # comparison
    
class StandardizeQuantityTests(unittest.TestCase):

    def test_valid_quantities(self):
        mock_test_data = pd.DataFrame([{'Product': 'Mavuno Harvest Organic Dried Fruit', 'Price': 3.64, 'Quantity': '2 Ozbag', 'Category': 'banana', 'store': 'Walmart', 'expected': '2.00 oz'}, 
                                 {'Product': 'Nature All Foods Organic Freeze Dried Raw Banana 2.5 oz - Vegan', 'Price': 7.88, 'Quantity': 'Nature All Foods Organic Freeze Dried Raw Banana 2.5 oz - Vegan', 'Category': 'banana', 'store': 'Walmart', 'expected': '2.50 oz'}, 
                                 {'Product': 'Silk Dairy Free', 'Price': 3.34, 'Quantity': '4 Pack', 'Category': 'milk', 'store': 'Walmart', 'expected':'4.00 ct'}, 
                                 {'Product': 'sugar', 'Price': 4.97, 'Quantity': '1.5 lb', 'Category': 'sugar', 'store': 'Walmart', 'expected':'24.00 oz'}, 
                                 {'Product': 'Salt', 'Price': 4.97, 'Quantity': '1 carton', 'Category': 'salt', 'store': 'Walmart', 'expected':'1.00 ct'},
                                 {'Product': 'Milk', 'Price': 2.98, 'Quantity': '64 fl oz Half Gallon', 'Category': 'milk', 'store': 'Aldi', 'expected': '64.00 oz'}, 
                                 {'Product': 'Great Value Whole Vitamin D Milk', 'Price': 3.52, 'Quantity': '2 gallons', 'Category': 'milk', 'store': 'Aldi', 'expected': '256.00 oz'},
                                 {"Product": "Great Value Milk 1 Lowfat Half Gallon Plastic Jug","Price": 2.12, "Quantity": "Great Value Milk 1 Lowfat Half Gallon Plastic Jug","Category": "milk","store": "Walmart","Standardized_Quantity": None}])
        
        for _, row in mock_test_data.iterrows():
            result = price_comparison.standardize_quantity(row)
            self.assertTrue(pd.isna(result) and pd.isna(row['expected']) or result == row['expected'])
    
    def test_standard_quantity_null_drop(self):
        mock_test_data = pd.DataFrame([{"Product": "Great Value Milk 1 Lowfat Half Gallon Plastic Jug","Price": 2.12,"Quantity": "Great Value Milk 1 Lowfat Half Gallon Plastic Jug","Category": "milk","store": "Walmart"}])
        clean_data = price_comparison.data_cleaning(mock_test_data)
        actual_response = json.loads(clean_data.content.decode('utf-8'))
        expected_response = {"message": "No valid data after cleaning."}
        self.assertEqual(clean_data.status_code, 200)
        self.assertEqual(actual_response, expected_response)
            
if __name__ == "__main__":
    unittest.main()

