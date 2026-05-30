# Withdrawal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The local withdrawal ID | 
**whop_id** | **str** | The Whop withdrawal ID | 
**amount** | **float** | The amount withdrawn in cents | 
**currency** | **str** | Three-letter ISO currency code | 
**status** | **str** | The status of the withdrawal request | 
**fee_amount** | **float** | Fee amount charged for the withdrawal in cents | [optional] 
**fee_type** | **str** | The fee structure type (inclusive or exclusive) | [optional] 
**markup_fee** | **float** | Markup fee applied in cents | [optional] 
**speed** | **str** | Speed of withdrawal (standard, instant) | [optional] 
**trace_code** | **str** | Bank trace or reference code for tracking the payout | [optional] 
**payer_name** | **str** | The name of the entity or account paying out | [optional] 
**error_message** | **str** | Error message if the withdrawal failed | [optional] 
**business_id** | **str** | The business ID associated with this withdrawal | 
**created_at** | **datetime** | Timestamp when the withdrawal was requested | 
**updated_at** | **datetime** | Timestamp when the withdrawal status was updated | 

## Example

```python
from solifyn.models.withdrawal import Withdrawal

# TODO update the JSON string below
json = "{}"
# create an instance of Withdrawal from a JSON string
withdrawal_instance = Withdrawal.from_json(json)
# print the JSON string representation of the object
print(Withdrawal.to_json())

# convert the object into a dict
withdrawal_dict = withdrawal_instance.to_dict()
# create an instance of Withdrawal from a dict
withdrawal_from_dict = Withdrawal.from_dict(withdrawal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


