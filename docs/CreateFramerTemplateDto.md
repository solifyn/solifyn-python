# CreateFramerTemplateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the Framer template. | 
**remix_link** | **str** | The public Framer remix link. | 
**description** | **str** | A brief description of the template. | [optional] 

## Example

```python
from solifyn.models.create_framer_template_dto import CreateFramerTemplateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFramerTemplateDto from a JSON string
create_framer_template_dto_instance = CreateFramerTemplateDto.from_json(json)
# print the JSON string representation of the object
print(CreateFramerTemplateDto.to_json())

# convert the object into a dict
create_framer_template_dto_dict = create_framer_template_dto_instance.to_dict()
# create an instance of CreateFramerTemplateDto from a dict
create_framer_template_dto_from_dict = CreateFramerTemplateDto.from_dict(create_framer_template_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


