from diagrams import Diagram, Cluster, Edge
from diagrams.aws.general import User, Users, GenericDatabase, TraditionalServer, Client, General
from diagrams.aws.compute import Lambda, Batch, ECS, EKS, ElasticBeanstalk, Compute, AutoScaling, Fargate, Lightsail, SAR, ServerlessApplicationRepository
from diagrams.aws.storage import S3, Backup, EBS, EFS, S3Glacier, Storage, StorageGateway
from diagrams.aws.database import Dynamodb, RDS, Redshift, DB, ElastiCache, Neptune, Timestream
from diagrams.aws.network import APIGateway, CloudFront, GlobalAccelerator, Route53, VPC, Endpoint, DirectConnect
from diagrams.aws.security import WAF, SecretsManager, ACM, Cognito
from diagrams.aws.integration import Eventbridge, SNS, SQS, Appsync, StepFunctions
from diagrams.aws.analytics import Kinesis, Athena, Quicksight, ES, ElasticsearchService, Analytics, DataPipeline, Glue, EMR, KinesisDataAnalytics, KinesisDataFirehose, KinesisDataStreams, LakeFormation, Redshift, ManagedStreamingForKafka
from diagrams.aws.ml import Sagemaker, Comprehend, Rekognition, Forecast, Personalize, Polly, Textract, Transcribe, Translate, MachineLearning, Lex, SagemakerNotebook, SagemakerModel, SagemakerTrainingJob

with Diagram("Compute Guidance", show=False):
    with Cluster("Compute", direction="TB"):
        with Cluster("Serverless", direction="LR"):
            General("Lambda")
            General("Glue Job")
        with Cluster("PaaS (Platform as a service)"):
            General("Cloud Foundry")
        with Cluster("Containers", direction="TB"):
            General("ECS on Fargate")
            General("ECS on EC2")
            General("EKS on Fargate")
            General("EKS on EC2")
        with Cluster("IaaS (Infrastructure as a service)"):
            General("EC2")
            
