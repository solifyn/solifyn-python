# Invoice

Represents a generated invoice for an order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique invoice identifier. | 
**order_id** | **str** | Associated order ID. | 
**url** | **str** | Invoice URL for downloading or viewing PDF. | 
**status** | **str** | Status of invoice. | 
**created_at** | **datetime** | Invoice creation date. | 

## Example

```python
from solifyn.models.invoice import Invoice

# TODO update the JSON string below
json = "{}"
# create an instance of Invoice from a JSON string
invoice_instance = Invoice.from_json(json)
# print the JSON string representation of the object
print(Invoice.to_json())

# convert the object into a dict
invoice_dict = invoice_instance.to_dict()
# create an instance of Invoice from a dict
invoice_from_dict = Invoice.from_dict(invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


