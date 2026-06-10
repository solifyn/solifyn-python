# BrandUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the brand | [optional] 
**website_url** | **str** | The website URL associated with the brand | [optional] 
**support_email** | **str** | Support email address for customer service | [optional] 
**description** | **str** | Short description of the brand | [optional] 
**logo_url** | **str** | Brand logo image URL | [optional] 
**statement_descriptor** | **str** | Credit card statement descriptor (Max 22 chars) | [optional] 

## Example

```python
from solifyn.models.brand_update import BrandUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BrandUpdate from a JSON string
brand_update_instance = BrandUpdate.from_json(json)
# print the JSON string representation of the object
print(BrandUpdate.to_json())

# convert the object into a dict
brand_update_dict = brand_update_instance.to_dict()
# create an instance of BrandUpdate from a dict
brand_update_from_dict = BrandUpdate.from_dict(brand_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


