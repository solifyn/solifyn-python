# ProductCreateCustomFieldsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**required** | **bool** |  | [optional] 
**field_type** | **str** |  | [optional] 
**placeholder** | **str** |  | [optional] 

## Example

```python
from solifyn.models.product_create_custom_fields_inner import ProductCreateCustomFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCreateCustomFieldsInner from a JSON string
product_create_custom_fields_inner_instance = ProductCreateCustomFieldsInner.from_json(json)
# print the JSON string representation of the object
print(ProductCreateCustomFieldsInner.to_json())

# convert the object into a dict
product_create_custom_fields_inner_dict = product_create_custom_fields_inner_instance.to_dict()
# create an instance of ProductCreateCustomFieldsInner from a dict
product_create_custom_fields_inner_from_dict = ProductCreateCustomFieldsInner.from_dict(product_create_custom_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


