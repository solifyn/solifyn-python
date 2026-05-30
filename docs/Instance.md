# Instance

Represents an active device or software instance that has been activated against a license key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique database identifier of this instance record. | 
**license_id** | **str** | The internal ID of the parent license key this instance belongs to. | 
**instance_id** | **str** | The unique hardware hash or client-generated identifier of the activated device/machine. | 
**instance_name** | **str** | A human-readable display name for this instance, assigned by the client application. | 
**ip_address** | **str** | The IP address recorded at the time of activation. | 
**activated_at** | **str** | Timestamp when this device instance was first activated. | 
**last_seen_at** | **str** | Timestamp of the most recent activation heartbeat or re-activation check from this device. | 

## Example

```python
from solifyn.models.instance import Instance

# TODO update the JSON string below
json = "{}"
# create an instance of Instance from a JSON string
instance_instance = Instance.from_json(json)
# print the JSON string representation of the object
print(Instance.to_json())

# convert the object into a dict
instance_dict = instance_instance.to_dict()
# create an instance of Instance from a dict
instance_from_dict = Instance.from_dict(instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


