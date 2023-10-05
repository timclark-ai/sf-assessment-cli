# Python/Typescript

## Requirements

1. Write a CLI that exposes two commands
2. One command to list the files in the S3 bucket created in the first step
3. One command lists the versions of the ECS task definition for the service created in step 1
4. Basic unit tests

## These are the steps I took to complete this portion of the assessment:

I took a low-code approach by leveraging existing open source projects and modifying them just enough to meet the requirements of the assessment.

I am happy to walk through the implementation with the SourceFuse team, if interested.

1. Cloned a Typer project template to create a Python CLI.
2. Added 2 CLI commands: s3objects and tdversions.
3. Used the AWS SDK for Python (Boto3) to write logic to fulfill those 2 commands.
4. Added unit tests to cover the 2 commands
5. Setup environment variables:
```
set AWS_PROFILE=nikosce
set AWS_DEFAULT_REGION=us-east-2
```
6. Ran the help to view the available commands:
```
python -m rptodo --help  
```
![python1](https://github.com/timclark-ai/sf-assessment-cli/assets/24612753/135dc96b-549d-47ed-8177-6d827b1bbfc8)

7. Ran the init
```
python -m rptodo init
```
8. Verified s3objects is showing the list of log files in the S3 bucket.
```
python -m rptodo s3objects
```
![python2](https://github.com/timclark-ai/sf-assessment-cli/assets/24612753/604e5355-9cfc-48ee-ba48-093c289f2f3d)

9. Verified tdversions is showing the list of container image versions.
```
python -m rptodo tdversions
```
![python3](https://github.com/timclark-ai/sf-assessment-cli/assets/24612753/6ec32fa6-d4ee-4d10-9ff1-2360b4523506)

10. Ran the unit tests, confirmed all tests pass:
```
python -m pytest tests/
```
![python4](https://github.com/timclark-ai/sf-assessment-cli/assets/24612753/dd24f225-98f4-458a-9278-e8b1e06b184a)
