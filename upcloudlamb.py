import boto3
import StringIO
import zipfile
import mimetypes

def lambda_handler(event, context):

    s3 = boto3.resource('s3')

    cloudbit_bucket = s3.Bucket('cloudbit.tv')
    build_bucket =s3.Bucket('buildcloudbit')

    do_zip=StringIO.StringIO()
    build_bucket.download_fileobj('buildcloudbit.zip', do_zip)

    with zipfile.ZipFile(do_zip) as myzip:
        for nm in myzip.namelist():
            obj = myzip.open(nm)
            cloudbit_bucket.upload_fileobj(obj,nm,
            ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
            cloudbit_bucket.Object(nm).Acl().put(ACL='public-read')
    return 'Hello from Lambda'
