# WebhookPaymentPayloadBillingAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**line1** | **str** |  | [optional] 
**line2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 

## Example

```python
from solifyn.models.webhook_payment_payload_billing_address import WebhookPaymentPayloadBillingAddress

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPaymentPayloadBillingAddress from a JSON string
webhook_payment_payload_billing_address_instance = WebhookPaymentPayloadBillingAddress.from_json(json)
# print the JSON string representation of the object
print(WebhookPaymentPayloadBillingAddress.to_json())

# convert the object into a dict
webhook_payment_payload_billing_address_dict = webhook_payment_payload_billing_address_instance.to_dict()
# create an instance of WebhookPaymentPayloadBillingAddress from a dict
webhook_payment_payload_billing_address_from_dict = WebhookPaymentPayloadBillingAddress.from_dict(webhook_payment_payload_billing_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


