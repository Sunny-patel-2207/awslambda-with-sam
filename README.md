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

Download the source code from the given link."https://github.com/Sunny-patel-2207/awslambda-with-sam"
Once you download the source code, open the terminal at your source code directory.
Run the command “sam init” and provide the path of the zip file.
After that run command “sam build”
This command will generate the build file for your deployment.
Run the command “sam deploy --guided” to provide the required information including Stack Name, Region Name and other required information.

Once you are complete with these three commands and sam deploy --guided command will execute successfully check your AWS console and you’ll have the desired infrastructure.

Post Steps:

Once your deployment will complete, create an AWS EC2 instance. To create an EC2 instance follow the instruction 
Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/
From the console dashboard, choose Launch Instance.
The Choose an Amazon Machine Image (AMI) page displays a list of basic configurations, called Amazon Machine Images (AMIs), that serve as templates for your instance. Select an HVM version of Ubuntu Server 20.04 LTS. Notice that these AMIs are marked "Free tier eligible."
On the Choose an Instance Type page, you can select the hardware configuration of your instance. Select the t2.nano instance type
On the next button make sure to select the Network which will be created by Cloud formation. To find the Network, open the AWS console in another tab and search for CloudFormation. In cloud formation open your stack (Stack name you’d defined when you deployed the function with “sam deploy --guided” command.) Do not close this tab until you install dependencies.. This tab will help you to find your security group.
Click on Add storage and and make values as default, click on Add Tags make the values as default and click on Configure Security Groups and select the Security Group which was created with cloud formation stack.
choose Review and Launch 
On the Review Instance Launch page, choose Launch.
When prompted for a key pair, select Create a new key pair, then name the key pair and download it. then choose Launch Instances.

To connect and mount your EFS to your AWS EC2 Instances follow the below steps.
If your local computer operating system is Linux or macOS X follow the link: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html

If your local computer operating system is Windows follow the link: 
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html

Once you Login to your EC2 insurance  run the following commands.
sudo apt-get update
sudo  apt install nfs-common
sudo apt-get upgrade
sudo mkdir mountpoint
sudo chmod 777 mountpoint
Then in AWS Console search EFS and select the EFS which was created with AWS Cloud Formation stack.
Click on File System.
Click on file system name and click on attach, when it will prompt select Mount via IP select the availability zone and copy the “Using the NFS client:”
One get back to your AWS EC2 instance and paste the “Using the NFS client”, replace efs with mountpoint and hit enter.
Once the process is finished run command “df -h” and check the EFS.
Now run the following commands.
cd mountpoint/
pip install tabula csv pytz requests boto3 –target ~/mountpoint/access/
sudo apt-get upgrade
sudo wget https://bmv-si.s3.amazonaws.com/jre-for-lambda/jre-8u311-linux-x64.tar.gz
tar zxvf "filename"

Now you can test your lambda function.

