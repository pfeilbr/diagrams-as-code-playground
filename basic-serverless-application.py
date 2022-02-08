from diagrams import Diagram, Cluster, Edge
from diagrams.aws.general import User, Users, GenericDatabase, TradicionalServer
from diagrams.aws.compute import Lambda, Batch, ECS, EKS, ElasticBeanstalk, Compute, AutoScaling, Fargate, Lightsail, SAR, ServerlessApplicationRepository
from diagrams.aws.storage import S3, Backup, EBS, EFS, S3Glacier, Storage, StorageGateway
from diagrams.aws.database import Dynamodb, RDS, Redshift, DB, ElastiCache, Neptune, Timestream
from diagrams.aws.network import APIGateway, CloudFront, GlobalAccelerator, Route53, VPC, Endpoint, DirectConnect
from diagrams.aws.security import WAF, SecretsManager, ACM, Cognito
from diagrams.aws.integration import Eventbridge, SNS, SQS, Appsync, StepFunctions
from diagrams.aws.analytics import Kinesis, Athena, Quicksight, ES, ElasticsearchService, Analytics, DataPipeline, Glue, EMR, KinesisDataAnalytics, KinesisDataFirehose, KinesisDataStreams, LakeFormation, Redshift, ManagedStreamingForKafka
from diagrams.aws.ml import Sagemaker, Comprehend, Rekognition, Forecast, Personalize, Polly, Textract, Transcribe, Translate, MachineLearning, Lex, SagemakerNotebook, SagemakerModel, SagemakerTrainingJob


with Diagram("Basic Serverless Application", show=False):
    
    with Cluster("Corporate Data Center - US"):
        pf = TradicionalServer("PingFederate")
        users = Users("Users")
        
    with Cluster("Account: account-1"):
        dc = DirectConnect("Direct Connect")
        with Cluster("Region: us-east-1"):
            cognito = Cognito("Cognito")
            
            rt53 = Route53("Route 53")
            waf = WAF("WAF")
            acm = ACM("TLS Certificate")
            cf = CloudFront("CloudFront")
            apig = APIGateway("REST API")
            ddb = Dynamodb("Data")
            s3 = S3("static web assets")
            
            with Cluster("VPC"):
                sm = SecretsManager("Secrets Manager")
                with Cluster("AZ"):
                    with Cluster("Private Subnet"):
                        rds = RDS("Oracle RDS")
                        lambdas = Lambda("API Handler(s)")
                        users >> Edge(label="federated auth") >> cognito >> Edge(label="SAML2") >> pf
                        users >> Edge(label="https")>> dc >> rt53 >> waf >> acm >> cf >> s3
                        cf >> apig
                        lambdas >> Edge(label="DB credentials") >> Endpoint("VPC Endpoint") >> sm
                        apig >> Edge(label="json")>> lambdas >> rds            

