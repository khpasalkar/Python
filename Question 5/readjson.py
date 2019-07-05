import json

#loading json file in data 
with open('info.json') as file:
	data = json.load(file)

#prints the output of the arn of bucket
print(data['Records'][0]['s3']['bucket']['arn'])


