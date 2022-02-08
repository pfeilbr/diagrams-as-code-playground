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
            sm = SecretsManager("Secrets Manager")
            ddb = Dynamodb("DynamoDB")
            s3 = S3("static web assets")
    
            with Cluster("VPC"):
                
                with Cluster("Availability Zone 1"):
                    with Cluster("Private Subnet 1"):
                        sm_vpce = Endpoint("VPC Endpoint")
                        ddb_vpce = Endpoint("VPC Endpoint")
                        rds_primary = RDS("Oracle RDS")
                        lambdas = Lambda("API Handler(s)")
                        users >> Edge(label="federated auth") >> cognito >> Edge(label="SAML2") >> pf
                        users >> Edge(label="https")>> dc >> rt53 >> waf >> acm >> cf >> s3
                        cf >> apig
                        lambdas >> Edge(label="DB credentials") >> sm_vpce >> sm
                        lambdas >> ddb_vpce
                        apig >> Edge(label="json")>> lambdas >> rds_primary   
                        ddb_vpce >> ddb
                with Cluster("Availability Zone 2"):
                    with Cluster("Private Subnet 2"):
                        rds_standby = RDS("Oracle RDS (Standby)")

                        rds_primary - Edge(label="replication") - rds_standby

