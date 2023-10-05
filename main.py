import boto3
import typer


def main(name: str, lastname: str):
    print(f"Hello {name} {lastname}")


if __name__ == "__main__":
    typer.run(main)


# s3 = boto3.resource('s3')
# print("S3 bucket object keys:")
# for my_bucket_object in s3.Bucket('nikos-test-ecs-web-app-alb-access-logs').objects.all():
#     print(my_bucket_object.key)

# print("---")

# ecs = boto3.client('ecs')
# print("ECS task definitions:")
# for r in ecs.list_task_definitions(familyPrefix='nikos-test-ecs-web-app')['taskDefinitionArns']:
#     print(r)