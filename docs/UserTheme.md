# UserTheme


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Theme configuration ID | 
**config** | **object** | Styling config JSON (fontFamily, borderRadius, colors) | 
**avatar_url** | **str** | Logo/avatar image URL | [optional] 
**banner_url** | **str** | Header banner image URL | [optional] 
**business_id** | **str** | The linked business ID | 

## Example

```python
from solifyn.models.user_theme import UserTheme

# TODO update the JSON string below
json = "{}"
# create an instance of UserTheme from a JSON string
user_theme_instance = UserTheme.from_json(json)
# print the JSON string representation of the object
print(UserTheme.to_json())

# convert the object into a dict
user_theme_dict = user_theme_instance.to_dict()
# create an instance of UserTheme from a dict
user_theme_from_dict = UserTheme.from_dict(user_theme_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


