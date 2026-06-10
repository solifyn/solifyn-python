# ProductCreateAddonsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | [optional] 
**min_quantity** | **int** |  | [optional] 
**max_quantity** | **int** |  | [optional] 
**price_override** | **float** |  | [optional] 
**is_seat_addon** | **bool** |  | [optional] 

## Example

```python
from solifyn.models.product_create_addons_inner import ProductCreateAddonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCreateAddonsInner from a JSON string
product_create_addons_inner_instance = ProductCreateAddonsInner.from_json(json)
# print the JSON string representation of the object
print(ProductCreateAddonsInner.to_json())

# convert the object into a dict
product_create_addons_inner_dict = product_create_addons_inner_instance.to_dict()
# create an instance of ProductCreateAddonsInner from a dict
product_create_addons_inner_from_dict = ProductCreateAddonsInner.from_dict(product_create_addons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


