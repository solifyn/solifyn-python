# ProductsList200ResponsePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** | Total number of items matching filters. | 
**max_page** | **int** | Maximum page index available based on current page size. | 

## Example

```python
from solifyn.models.products_list200_response_pagination import ProductsList200ResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsList200ResponsePagination from a JSON string
products_list200_response_pagination_instance = ProductsList200ResponsePagination.from_json(json)
# print the JSON string representation of the object
print(ProductsList200ResponsePagination.to_json())

# convert the object into a dict
products_list200_response_pagination_dict = products_list200_response_pagination_instance.to_dict()
# create an instance of ProductsList200ResponsePagination from a dict
products_list200_response_pagination_from_dict = ProductsList200ResponsePagination.from_dict(products_list200_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


