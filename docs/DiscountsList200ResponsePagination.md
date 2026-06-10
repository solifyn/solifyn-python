# DiscountsList200ResponsePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of items matching filters. | 
**total_count** | **int** | Total number of items matching filters (alias). | 
**max_page** | **int** | Maximum page index available based on current page size. | 

## Example

```python
from solifyn.models.discounts_list200_response_pagination import DiscountsList200ResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountsList200ResponsePagination from a JSON string
discounts_list200_response_pagination_instance = DiscountsList200ResponsePagination.from_json(json)
# print the JSON string representation of the object
print(DiscountsList200ResponsePagination.to_json())

# convert the object into a dict
discounts_list200_response_pagination_dict = discounts_list200_response_pagination_instance.to_dict()
# create an instance of DiscountsList200ResponsePagination from a dict
discounts_list200_response_pagination_from_dict = DiscountsList200ResponsePagination.from_dict(discounts_list200_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


