"""
To invoke from CLI:

aws lambda invoke --function-name MarcoPolo9000 --payload '{"name": "Marco" }' out.txt | less out.txt

"""


def lambda_handler(event, context):
    if event["name"] == "Marco":
        return "Polo"
    return "No!"
