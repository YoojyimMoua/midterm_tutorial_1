from constructs import Construct
from cdktf import App, TerraformStack
from imports.aws import (AwsProvider, S3Bucket)

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)
        
        # Configure AWS Provider
        AwsProvider(self, "AWS", region="us-east-1")
        
        # Define an S3 bucket for static website hosting
        bucket = S3Bucket(
            self, 
            "MyWebsiteBucket",
            website={
                "index_document": "index.html",
                "error_document": "error.html"
            },
            acl="public-read"
        )

app = App()
MyStack(app, "cdktf-s3-static-site")

app.synth()
