# Addon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | The product ID of the addon product. | 
**min_quantity** | **float** | Minimum quantity allowed. | 
**max_quantity** | **object** | Maximum quantity allowed (null if unlimited). | 
**price_override** | **object** | Price override (null if using base product price). | 
**is_seat_addon** | **bool** | Flag indicating if this is a seat/license addon. | 

## Example

```python
from solifyn.models.addon import Addon

# TODO update the JSON string below
json = "{}"
# create an instance of Addon from a JSON string
addon_instance = Addon.from_json(json)
# print the JSON string representation of the object
print(Addon.to_json())

# convert the object into a dict
addon_dict = addon_instance.to_dict()
# create an instance of Addon from a dict
addon_from_dict = Addon.from_dict(addon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


