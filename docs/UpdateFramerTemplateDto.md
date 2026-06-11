# UpdateFramerTemplateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Framer template. | [optional] 
**remix_link** | **str** | The public Framer remix link. | [optional] 
**description** | **str** | A brief description of the template. | [optional] 

## Example

```python
from solifyn.models.update_framer_template_dto import UpdateFramerTemplateDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFramerTemplateDto from a JSON string
update_framer_template_dto_instance = UpdateFramerTemplateDto.from_json(json)
# print the JSON string representation of the object
print(UpdateFramerTemplateDto.to_json())

# convert the object into a dict
update_framer_template_dto_dict = update_framer_template_dto_instance.to_dict()
# create an instance of UpdateFramerTemplateDto from a dict
update_framer_template_dto_from_dict = UpdateFramerTemplateDto.from_dict(update_framer_template_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


