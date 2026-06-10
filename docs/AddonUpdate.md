# AddonUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_quantity** | **float** | Minimum quantity of the addon allowed to be purchased. | [optional] 
**max_quantity** | **float** | Maximum quantity of the addon allowed to be purchased (optional). | [optional] 
**price_override** | **float** | Price override for the addon product when purchased with this parent (optional). | [optional] 
**is_seat_addon** | **bool** | Flag indicating if this addon represents a seat/license limit increment. | [optional] 

## Example

```python
from solifyn.models.addon_update import AddonUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AddonUpdate from a JSON string
addon_update_instance = AddonUpdate.from_json(json)
# print the JSON string representation of the object
print(AddonUpdate.to_json())

# convert the object into a dict
addon_update_dict = addon_update_instance.to_dict()
# create an instance of AddonUpdate from a dict
addon_update_from_dict = AddonUpdate.from_dict(addon_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


