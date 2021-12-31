# awslambda-with-sam

Hello There,

This demo tutorial contains the information about SAM Deployment. Follow the instructions and complete the demo.
There are some prerequisites for this deployment.
You have installed runtime for your existing projects and yml template based on your requirements.
In this demo I have one Python Lambda function, along with this lambda I have a VPC attached to it, An EFS and IAM role.
I provide all the required files including templates in this demo. Follow the below steps to execute the SAM deployment.

Install AWS CLI in your local system with commands 
 curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip
unzip awscliv2.zip
sudo ./aws/install
Check the installed AWS CLI version with command “aws --version”
Configure your AWS IAM user with command aws configure and provide the required credentials/information.

Install the SAM in your local system (Ubuntu). To install he SAM,
Download the file from given link to directory of your choice https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip
Verify the integrity and authenticity of the downloaded installer files with command “sha256sum aws-sam-cli-linux-x86_64.zip” and it will generate the output “<64-character SHA256 hash value> aws-sam-cli-linux-x86_64.zip”
Unzip the file into  sam-installation/ directory with command “unzip aws-sam-cli-linux-x86_64.zip -d sam-installation”.
Install the AWS SAM CLI with command “sudo ./sam-installation/install”
Verify the installation with command “sam –version”.


Note: For Windows installation follow the link https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-windows.html and for macOS follow the link https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-mac.html

Download the source code from the given link.
Once you download the source code, open the terminal at your source code directory.
Run the command “sam init” and provide the path of the zip file.
After that run command “sam build”
This command will generate the build file for your deployment.
Run the command “sam deploy --guided” to provide the required information including Stack Name, Region Name and other required information.

Once you are complete with these three command and sam deploy --guided command will execute successfully check your AWS console and you’ll have the desired infrastructure.


