
# ☁️ Cloud Resume Challenge

This project is my completed version of the [Cloud Resume Challenge](https://cloudresumechallenge.dev/), a hands-on initiative combining frontend development, cloud infrastructure, CI/CD, and serverless tech.

It showcases a static resume site hosted on **AWS S3**, with a dynamic visitor counter powered by **Lambda**, **API Gateway**, and **DynamoDB**.

---

## 🌐 Live Site

**[View my resume](http://bryangarcia-resume-site.s3-website-us-east-1.amazonaws.com)** hosted on AWS S3.

![Resume Screenshot](./Screenshot%202025-04-03%20at%205.14.44%E2%80%AFPM.png)

---

## 🛠 Tech Stack

- **Frontend**: HTML/CSS
- **Cloud**: AWS S3, Lambda, DynamoDB, API Gateway
- **Backend**: Python (Lambda function)
- **Infrastructure**: AWS IAM, CloudWatch Logs
- **CI/CD**: Manual for now (soon to be GitHub Actions)

---

## 🚀 How to Deploy

1. Clone this repo:
   ```bash
   git clone https://github.com/ckideas1/cloud-resume-challenge.git
   cd cloud-resume-challenge
   
2. Set up AWS services:
   
   AWS S3: Host the static website.

   AWS Lambda: Create a function for counting visitors.

   API Gateway: Set up an API to expose Lambda function.

   DynamoDB: Store visitor count.
   
---

📜 Objective

The Cloud Resume Challenge aims to demonstrate a range of cloud computing and web development skills, with a focus on serverless architecture. The main goal is to create a dynamic and highly available resume site that automatically tracks the number of visitors.

---

🛠️ Project Workflow

Frontend Development: I started by building a simple HTML/CSS site to showcase my resume.

AWS Setup:

    Configured S3 to serve as the static hosting for the site.

    Developed a Lambda function to count unique visitors using a DynamoDB table to store the count.

    Set up an API Gateway to expose the Lambda function via a REST API.

CI/CD Pipeline:

    Initially, I manually deployed my site to S3 but am now transitioning to automate the deployment process with GitHub Actions for continuous 
    deployment.

💡 CI/CD with GitHub Actions (To be completed soon)

    GitHub Actions automates the deployment of the site on every change made to the repository. This ensures that the resume site is always up-to- 
    date without needing to manually push files.

---

🔧 Troubleshooting

    Issue: If you're having trouble deploying, ensure all AWS services are properly configured, especially the Lambda function and DynamoDB table.

    AWS Secrets: Make sure your AWS Access Keys are securely configured in GitHub secrets (e.g., AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY).

---

📅 Milestones

    Initial Setup: Completed creating the static resume site and uploaded to AWS S3.

    Visitor Count: Integrated AWS Lambda, API Gateway, and DynamoDB for the dynamic counter.

    CI/CD Pipeline: Transitioning to GitHub Actions for automated deployments.

---

📝 License

    This project is licensed under the MIT License - see the LICENSE file for details.

---

### Breakdown:
1. **Title**: Clearly identifies the project with an emoji to make it visually appealing.
2. **Live Site**: Provides a link to the deployed website, along with a screenshot (if available).
3. **Tech Stack**: Concisely lists the technologies used in the project.
4. **How to Deploy**: Offers clear instructions to set up the project locally or on AWS.
5. **Objective**: Explains the project goal in a few sentences, making it easy for anyone to understand what you're aiming to showcase.
6. **Project Workflow**: Describes the step-by-step process you followed to build the project. This is helpful for potential employers or collaborators who want insight into your development approach.
7. **CI/CD with GitHub Actions**: Mentions the future plan for automation and continuous deployment with GitHub Actions.
8. **Troubleshooting**: Offers potential solutions to common problems you may have encountered during setup.
9. **Milestones**: Helps track the progress of the project and what you've completed so far.
10. **License**: Standard practice to mention the license under which the project is shared (e.g., MIT License).

---








