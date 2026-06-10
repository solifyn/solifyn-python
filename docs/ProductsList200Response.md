# ProductsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Product]**](Product.md) |  | 
**pagination** | [**ProductsList200ResponsePagination**](ProductsList200ResponsePagination.md) |  | 

## Example

```python
from solifyn.models.products_list200_response import ProductsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsList200Response from a JSON string
products_list200_response_instance = ProductsList200Response.from_json(json)
# print the JSON string representation of the object
print(ProductsList200Response.to_json())

# convert the object into a dict
products_list200_response_dict = products_list200_response_instance.to_dict()
# create an instance of ProductsList200Response from a dict
products_list200_response_from_dict = ProductsList200Response.from_dict(products_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


