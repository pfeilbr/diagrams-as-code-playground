from diagrams import Diagram
from diagrams.aws.compute import Lambda, Batch, ECS, EKS, ElasticBeanstalk, Compute, AutoScaling, Fargate, Lightsail, SAR, ServerlessApplicationRepository
from diagrams.aws.storage import S3, Backup, EBS, EFS, S3Glacier, Storage, StorageGateway
from diagrams.aws.database import Dynamodb, RDS, Redshift, DB, ElastiCache, Neptune, Timestream
from diagrams.aws.network import APIGateway, CloudFront, GlobalAccelerator, Route53, VPC
from diagrams.aws.integration import Eventbridge, SNS, SQS, Appsync, StepFunctions
from diagrams.aws.analytics import Kinesis, Athena, Quicksight, ES, ElasticsearchService, Analytics, DataPipeline, Glue, EMR, KinesisDataAnalytics, KinesisDataFirehose, KinesisDataStreams, LakeFormation, Redshift, ManagedStreamingForKafka
from diagrams.aws.ml import Sagemaker, Comprehend, Rekognition, Forecast, Personalize, Polly, Textract, Transcribe, Translate, MachineLearning, Lex, SagemakerNotebook, SagemakerModel, SagemakerTrainingJob


with Diagram("Event-based Application", show=False):
    eb = Eventbridge("EventBridge (Event Router)")
    apig = APIGateway("REST API")
    apig >> Lambda("API Handler(s)") >> Dynamodb("Data")
