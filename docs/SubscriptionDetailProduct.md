# SubscriptionDetailProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The product unique ID | 
**name** | **str** | The product name | 
**price** | **float** | Product base price | 
**currency** | **str** | Base currency | 
**metadata** | **object** | Metadata JSON payload | [optional] 
**pricing_type** | **str** | Pricing type, e.g. one-time or renewal | 

## Example

```python
from solifyn.models.subscription_detail_product import SubscriptionDetailProduct

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionDetailProduct from a JSON string
subscription_detail_product_instance = SubscriptionDetailProduct.from_json(json)
# print the JSON string representation of the object
print(SubscriptionDetailProduct.to_json())

# convert the object into a dict
subscription_detail_product_dict = subscription_detail_product_instance.to_dict()
# create an instance of SubscriptionDetailProduct from a dict
subscription_detail_product_from_dict = SubscriptionDetailProduct.from_dict(subscription_detail_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


