# Brand


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique brand ID | 
**name** | **str** | The brand name | 
**website_url** | **str** | The website URL associated with the brand | [optional] 
**support_email** | **str** | Support email address for customer service | [optional] 
**description** | **str** | Short description of the brand | [optional] 
**logo_url** | **str** | Brand logo image URL | [optional] 
**is_primary** | **bool** | Whether this is the primary brand for the merchant business | 
**statement_descriptor** | **str** | Credit card statement descriptor | [optional] 
**merchant_id** | **str** | The merchant ID owning the brand | 
**business_id** | **str** | The business ID linked to the brand | [optional] 
**created_at** | **datetime** | Timestamp when the brand was created | 
**updated_at** | **datetime** | Timestamp when the brand was last updated | 

## Example

```python
from solifyn.models.brand import Brand

# TODO update the JSON string below
json = "{}"
# create an instance of Brand from a JSON string
brand_instance = Brand.from_json(json)
# print the JSON string representation of the object
print(Brand.to_json())

# convert the object into a dict
brand_dict = brand_instance.to_dict()
# create an instance of Brand from a dict
brand_from_dict = Brand.from_dict(brand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


