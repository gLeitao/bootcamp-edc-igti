# HCL - Hashicopr Configuration Language
# Linguagem declarativa

resource "aws_s3_bucket" "datalake" {
  # Parametros de configuracao dos recursos escolhidos
  bucket = "${var.base_bucket_name}-${var.ambiente}-${var.numero_conta}"
  acl    = "private"

  server_side_encryption_configuration {
    rule {
      apply_server_side_encryption_by_default {
        sse_algorithm = "AES256"
      }
    }
  }

  tags = {
    IES   = "IGTI",
    CURSO = "EDC"
  }
}

resource "aws_s3_bucket_object" "codigo_spark" {
  bucket = aws_s3_bucket.datalake.id
  key    = "emr-code/pyspark/job-spark-from-tf.py"
  acl    = "private"
  source = "../interacao-s3/job_spark.py"
  etag   = filemd5("../interacao-s3/job_spark.py")
}

provider "aws" {
  region = "us-east-2"
}