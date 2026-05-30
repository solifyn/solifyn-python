# DiscountsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Discount]**](Discount.md) |  | 
**total** | **int** | Total number of items matching filters. | 
**total_count** | **int** | Total number of items matching filters (alias). | 
**pagination** | [**DiscountsList200ResponsePagination**](DiscountsList200ResponsePagination.md) |  | 

## Example

```python
from solifyn.models.discounts_list200_response import DiscountsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountsList200Response from a JSON string
discounts_list200_response_instance = DiscountsList200Response.from_json(json)
# print the JSON string representation of the object
print(DiscountsList200Response.to_json())

# convert the object into a dict
discounts_list200_response_dict = discounts_list200_response_instance.to_dict()
# create an instance of DiscountsList200Response from a dict
discounts_list200_response_from_dict = DiscountsList200Response.from_dict(discounts_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


