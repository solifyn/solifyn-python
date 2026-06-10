# Refund


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The refund ID | 
**whop_id** | **str** | The Whop Refund ID | 
**idempotency_key** | **str** | Client-generated key to prevent duplicate refunds | [optional] 
**amount** | **float** | Refunded amount | 
**currency** | **str** | Currency code | 
**status** | **str** | Status of the refund | 
**provider** | **str** | The payment provider used | [optional] 
**reason** | **str** | Reason for the refund | [optional] 
**reference_value** | **str** | Acquirer Reference Number (ARN) or tracking number | [optional] 
**payment_id** | **str** | The associated Payment ID | 
**provider_created_at** | **datetime** | Timestamp when the refund was processed by the provider | [optional] 
**created_at** | **datetime** | Timestamp when the refund was created in our system | 
**updated_at** | **datetime** | Timestamp when the refund was last updated | 

## Example

```python
from solifyn.models.refund import Refund

# TODO update the JSON string below
json = "{}"
# create an instance of Refund from a JSON string
refund_instance = Refund.from_json(json)
# print the JSON string representation of the object
print(Refund.to_json())

# convert the object into a dict
refund_dict = refund_instance.to_dict()
# create an instance of Refund from a dict
refund_from_dict = Refund.from_dict(refund_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


