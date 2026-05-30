# UserThemeUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | JSON object specifying styling parameters (colors, fonts, borders) | [optional] 
**avatar_url** | **str** | URL of the store avatar/logo | [optional] 
**banner_url** | **str** | URL of the store banner header image | [optional] 

## Example

```python
from solifyn.models.user_theme_update import UserThemeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of UserThemeUpdate from a JSON string
user_theme_update_instance = UserThemeUpdate.from_json(json)
# print the JSON string representation of the object
print(UserThemeUpdate.to_json())

# convert the object into a dict
user_theme_update_dict = user_theme_update_instance.to_dict()
# create an instance of UserThemeUpdate from a dict
user_theme_update_from_dict = UserThemeUpdate.from_dict(user_theme_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


