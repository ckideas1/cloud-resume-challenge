# ☁️ Cloud Resume Challenge

A security-hardened, serverless resume website built using AWS services and CI/CD best practices. This project was inspired by the original Cloud Resume Challenge, but with a strong emphasis on security, automation, and real-world cloud architecture.

---

## 🌐 Features

- 🚀 Serverless website hosted on AWS S3 with HTTPS via CloudFront  
- 🔒 IAM policies and S3 bucket permissions designed with least privilege  
- 🔁 Visitor counter using Lambda + DynamoDB  
- 🛠️ CI/CD deployment pipeline using GitHub Actions  
- 🧪 DNS managed through Route 53 for custom domain  
- 📄 Fully documented project with security-first mindset  

---

## 🧰 Tech Stack

- AWS S3 (Static site hosting)  
- AWS CloudFront (HTTPS + CDN)  
- AWS Lambda (Backend logic)  
- AWS DynamoDB (Visitor count)  
- AWS Route 53 (DNS)  
- IAM (Security permissions)  
- GitHub Actions (CI/CD Pipeline)  
- HTML/CSS + JavaScript  

---

## ⚙️ Setup Overview

> Note: You must have AWS credentials configured on your machine to deploy this project.

```bash
# Clone the repo
git clone https://github.com/ckideas1/cloud-resume-challenge.git
cd cloud-resume-challenge

# Update your bucket name and region in deployment scripts

# Deploy to S3 (manual method)
aws s3 sync ./site s3://your-bucket-name --delete

# Invalidate CloudFront cache if needed
aws cloudfront create-invalidation --distribution-id YOUR_DIST_ID --paths "/*"

---

🔐 Security Enhancements
IAM roles follow the principle of least privilege

S3 buckets are private with tightly scoped access

Public access blocked unless required via CloudFront

HTTPS enforced via CloudFront distribution

No hardcoded secrets (IAM creds use GitHub Secrets)

---

🔮 Future Improvements
Add WAF (Web Application Firewall) to front CloudFront

Integrate CloudTrail and GuardDuty monitoring

Add basic authentication for resume editor

Automate full teardown and redeploy via Terraform

---

🔗 GitHub Repository
https://github.com/ckideas1/cloud-resume-challenge

---

`Updated README.md with security-first writeup`
