# ResolvedAddon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | Unique product ID of the addon | 
**name** | **str** | Display name of the addon | 
**image_url** | **object** | URL of the addon image | 
**quantity** | **float** | The purchased quantity of the addon | 

## Example

```python
from solifyn.models.resolved_addon import ResolvedAddon

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedAddon from a JSON string
resolved_addon_instance = ResolvedAddon.from_json(json)
# print the JSON string representation of the object
print(ResolvedAddon.to_json())

# convert the object into a dict
resolved_addon_dict = resolved_addon_instance.to_dict()
# create an instance of ResolvedAddon from a dict
resolved_addon_from_dict = ResolvedAddon.from_dict(resolved_addon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


