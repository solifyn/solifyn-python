# AddonCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | The product ID of the addon product. | 
**min_quantity** | **float** | Minimum quantity of the addon allowed to be purchased. | [default to 0]
**max_quantity** | **float** | Maximum quantity of the addon allowed to be purchased (optional). | [optional] 
**price_override** | **float** | Price override for the addon product when purchased with this parent (optional). | [optional] 
**is_seat_addon** | **bool** | Flag indicating if this addon represents a seat/license limit increment. | [default to False]

## Example

```python
from solifyn.models.addon_create import AddonCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AddonCreate from a JSON string
addon_create_instance = AddonCreate.from_json(json)
# print the JSON string representation of the object
print(AddonCreate.to_json())

# convert the object into a dict
addon_create_dict = addon_create_instance.to_dict()
# create an instance of AddonCreate from a dict
addon_create_from_dict = AddonCreate.from_dict(addon_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


