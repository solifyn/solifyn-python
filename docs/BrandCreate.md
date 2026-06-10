# BrandCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the brand | 
**website_url** | **str** | The website URL associated with the brand | [optional] 
**support_email** | **str** | Support email address for customer service | [optional] 
**description** | **str** | Short description of the brand | [optional] 
**logo_url** | **str** | Brand logo image URL | [optional] 
**statement_descriptor** | **str** | Credit card statement descriptor (Max 22 chars) | [optional] 

## Example

```python
from solifyn.models.brand_create import BrandCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BrandCreate from a JSON string
brand_create_instance = BrandCreate.from_json(json)
# print the JSON string representation of the object
print(BrandCreate.to_json())

# convert the object into a dict
brand_create_dict = brand_create_instance.to_dict()
# create an instance of BrandCreate from a dict
brand_create_from_dict = BrandCreate.from_dict(brand_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


