# ProductSubDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**digital_link** | **str** |  | 

## Example

```python
from solifyn.models.product_sub_dto import ProductSubDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProductSubDto from a JSON string
product_sub_dto_instance = ProductSubDto.from_json(json)
# print the JSON string representation of the object
print(ProductSubDto.to_json())

# convert the object into a dict
product_sub_dto_dict = product_sub_dto_instance.to_dict()
# create an instance of ProductSubDto from a dict
product_sub_dto_from_dict = ProductSubDto.from_dict(product_sub_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


