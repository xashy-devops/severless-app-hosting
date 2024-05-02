####create 2 dynamo db tables: 

Menu Table: Create a DynamoDB table named Menu
ItemId (Primary Key): A unique identifier for each menu item

Orders Table: Create a DynamoDB table named Orders.
Attributes:
OrderId (Primary Key): 

###create 2 lambda functions;

You will need Lambda functions for:

Retrieving the Menu: Fetches menu data from the Menu table.
Placing Orders: Accepts order details from the API Gateway, processes them, and stores them in the Orders table.

### create an IAM role for lambda to make calls to dynamo db 


###create an api gateway with two different resources: 

Step 1: Create a New API
Log in to the AWS Management Console and navigate to the Amazon API Gateway service.
Choose "Create API".
Select REST API (not the private one) and click on "Build".
Choose "New API" and give it a name, e.g., "ShawarmaOrderingAPI".
Provide a description if desired and leave the endpoint type as "Regional".
Click on "Create API".
Step 2: Create Resources
Select your API in the API Gateway dashboard.
In the left-hand menu, click on Resources.
Click on the root resource (‘/’) and then click on "Create Resource".
Enter the resource name, such as "menu" or "order", and the resource path (usually the same).
Ensure "Enable API Gateway CORS" for the resource is checked if you're handling CORS at the API Gateway level.
Click on "Create Resource".
Step 3: Create Methods
For each resource, you will need to create methods (GET for menu, POST for order):

For the Menu:
Select the "menu" resource.
Click on "Create Method" and select GET from the dropdown list, then click the checkmark.
Set up the GET method:
Choose Lambda Function for the integration type.
Check "Use Lambda Proxy integration".
Select the appropriate Lambda Function (e.g., the one you created for retrieving the menu).
Confirm the region where your Lambda function is deployed.
Click "Save" and grant permissions to API Gateway to invoke your Lambda function.
For the Order:
Select the "order" resource.
Click on "Create Method" and select POST from the dropdown list, then click the checkmark.
Set up the POST method:
Follow the same steps as the GET method but select the Lambda function for placing orders.
Step 4: Enable CORS
If not already enabled when creating the resource:

Select each resource ("menu" and "order").
Click on "Actions", then select "Enable CORS".
Accept the default options provided and click on "Enable CORS and replace existing CORS headers".
Review the generated options and click "Yes, replace existing values".
Step 5: Deploy API
Click on "Actions" and select "Deploy API".
You'll need to create a new deployment stage:
Enter a stage name like "dev" or "prod".
Provide a description (optional).
Click "Deploy".
Step 6: Test Your API
After deploying, you'll receive an Invoke URL.
Use this URL to test your API endpoints:
Use tools like Postman or directly from your frontend to make requests to your API.

##create an s3 bucket and upload the html,js and css code. ensure to update the the js code to have the api endpoint
