# License

Represents a cryptographically secure software license key issued to a customer upon purchase or manual issuance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique prefix-based identifier of the license key. | 
**key** | **str** | The cryptographically generated license key string delivered to the customer. | 
**status** | **str** | Lifecycle status of the license. ACTIVE &#x3D; active. DISABLED &#x3D; suspended. REVOKED &#x3D; hard-revoked. | 
**business_id** | **str** | The unique identifier associated with the business this license belongs to. | 
**product_id** | **str** | The unique ID of the product this license key is associated with. | 
**payment_id** | **str** | The unique payment identifier that triggered the issuance of this license key. | 
**customer_id** | **str** | The unique customer identifier (ID) who received this license key. | 
**activation_limit** | **float** | Maximum number of simultaneous active device instances allowed for this license. Null means unlimited. | 
**activation_message** | **str** | Optional message displayed to the customer upon successful activation. | 
**instances_count** | **float** | Running count of how many times this license key has been activated. | 
**expiry_hours** | **float** | Relative expiry duration in hours from the time of issuance. | 
**expires_at** | **str** | Absolute expiration timestamp. The license becomes invalid after this point. | 
**filters** | **object** | Optional custom metadata filters associated with the license. | 
**archived** | **bool** | Indicates if the license key is archived. | 
**created_at** | **str** | Timestamp indicating exactly when the license key was issued. | 
**updated_at** | **str** | Timestamp indicating when the license key was last modified. | 

## Example

```python
from solifyn.models.license import License

# TODO update the JSON string below
json = "{}"
# create an instance of License from a JSON string
license_instance = License.from_json(json)
# print the JSON string representation of the object
print(License.to_json())

# convert the object into a dict
license_dict = license_instance.to_dict()
# create an instance of License from a dict
license_from_dict = License.from_dict(license_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


