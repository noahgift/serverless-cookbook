"""
To invoke from CLI:

AWS CLI v1
aws lambda invoke --function-name MarcoPolo9000 --payload '{"name": "Marco" }' out.txt | less out.txt

AWS CLI v2
aws lambda invoke \
	 --cli-binary-format raw-in-base64-out \
	--function-name marcopython \
	--payload '{"name": "Marco"}' \
	response.json

"""


def lambda_handler(event, context):
    if event["name"] == "Marco":
        return "Polo"
    return "No!"
