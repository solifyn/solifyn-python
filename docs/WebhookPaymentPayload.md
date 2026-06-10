# WebhookPaymentPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Internal payment ID. | [optional] 
**status** | **str** |  | [optional] 
**substatus** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**customer_email** | **str** |  | [optional] 
**customer_name** | **str** |  | [optional] 
**customer_username** | **str** |  | [optional] 
**product_title** | **str** |  | [optional] 
**product_route** | **str** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**membership_id** | **str** |  | [optional] 
**membership_status** | **str** |  | [optional] 
**billing_reason** | **str** |  | [optional] 
**amount** | **str** | Dollar value, 2 d.p. | [optional] 
**subtotal** | **str** |  | [optional] 
**usd_total** | **str** |  | [optional] 
**fee_amount** | **str** |  | [optional] 
**amount_after_fees** | **str** |  | [optional] 
**tax_amount** | **str** |  | [optional] 
**tax_behavior** | **str** |  | [optional] 
**tax_refunded_amount** | **str** |  | [optional] 
**refunded_amount** | **str** |  | [optional] 
**settlement_amount** | **str** |  | [optional] 
**settlement_currency** | **str** |  | [optional] 
**settlement_exchange_rate** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**refundable** | **bool** |  | [optional] 
**retryable** | **bool** |  | [optional] 
**auto_refunded** | **bool** |  | [optional] 
**payment_method** | **str** |  | [optional] 
**card_brand** | **str** |  | [optional] 
**card_last4** | **str** |  | [optional] 
**card_exp_month** | **int** |  | [optional] 
**card_exp_year** | **int** |  | [optional] 
**billing_address** | [**WebhookPaymentPayloadBillingAddress**](WebhookPaymentPayloadBillingAddress.md) |  | [optional] 
**license_key** | **str** |  | [optional] 
**files_snapshot** | **List[object]** |  | [optional] 
**checkout_id** | **str** |  | [optional] 
**discount_code** | **str** |  | [optional] 
**failure_message** | **str** |  | [optional] 
**paid_at** | **datetime** |  | [optional] 
**refunded_at** | **datetime** |  | [optional] 
**dispute_alerted_at** | **datetime** |  | [optional] 
**last_payment_attempt** | **datetime** |  | [optional] 
**next_payment_attempt** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**payment_event_type** | **str** |  | [optional] 
**last_event_type** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 

## Example

```python
from solifyn.models.webhook_payment_payload import WebhookPaymentPayload

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookPaymentPayload from a JSON string
webhook_payment_payload_instance = WebhookPaymentPayload.from_json(json)
# print the JSON string representation of the object
print(WebhookPaymentPayload.to_json())

# convert the object into a dict
webhook_payment_payload_dict = webhook_payment_payload_instance.to_dict()
# create an instance of WebhookPaymentPayload from a dict
webhook_payment_payload_from_dict = WebhookPaymentPayload.from_dict(webhook_payment_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


