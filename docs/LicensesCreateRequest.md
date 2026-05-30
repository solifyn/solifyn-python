# LicensesCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | The unique product identifier (internal product ID or ID) for which the license key will be issued. | 
**customer_id** | **str** | The unique customer identifier (internal customer ID or ID) who will own this license key. | 
**activation_limit** | **int** | The maximum number of concurrent device or server activations allowed for this license key. | [optional] 
**expiry_hours** | **int** | Relative validity period of the license in hours starting from the time of creation. | [optional] 
**key** | **str** | Optional custom license key string. If not provided, a random uppercase cryptographic serial key (e.g., ABCD-EFGH) will be generated automatically. | [optional] 

## Example

```python
from solifyn.models.licenses_create_request import LicensesCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LicensesCreateRequest from a JSON string
licenses_create_request_instance = LicensesCreateRequest.from_json(json)
# print the JSON string representation of the object
print(LicensesCreateRequest.to_json())

# convert the object into a dict
licenses_create_request_dict = licenses_create_request_instance.to_dict()
# create an instance of LicensesCreateRequest from a dict
licenses_create_request_from_dict = LicensesCreateRequest.from_dict(licenses_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


