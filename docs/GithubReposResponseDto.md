# GithubReposResponseDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | The GitHub repository ID | 
**full_name** | **str** | The repository full name (owner/repo) | 
**name** | **str** | The repository name | 

## Example

```python
from solifyn.models.github_repos_response_dto import GithubReposResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of GithubReposResponseDto from a JSON string
github_repos_response_dto_instance = GithubReposResponseDto.from_json(json)
# print the JSON string representation of the object
print(GithubReposResponseDto.to_json())

# convert the object into a dict
github_repos_response_dto_dict = github_repos_response_dto_instance.to_dict()
# create an instance of GithubReposResponseDto from a dict
github_repos_response_dto_from_dict = GithubReposResponseDto.from_dict(github_repos_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


