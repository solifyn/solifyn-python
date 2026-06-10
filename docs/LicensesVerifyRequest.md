# LicensesVerifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The license key to validate. | 
**product_id** | **str** | The product ID associated with the license. | 

## Example

```python
from solifyn.models.licenses_verify_request import LicensesVerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LicensesVerifyRequest from a JSON string
licenses_verify_request_instance = LicensesVerifyRequest.from_json(json)
# print the JSON string representation of the object
print(LicensesVerifyRequest.to_json())

# convert the object into a dict
licenses_verify_request_dict = licenses_verify_request_instance.to_dict()
# create an instance of LicensesVerifyRequest from a dict
licenses_verify_request_from_dict = LicensesVerifyRequest.from_dict(licenses_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


