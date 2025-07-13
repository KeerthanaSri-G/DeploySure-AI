import boto3

def check_public_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = response['Buckets']

    public_buckets = []

    for bucket in buckets:
        bucket_name = bucket['Name']
        try:
            acl = s3.get_bucket_acl(Bucket=bucket_name)
            for grant in acl['Grants']:
                if 'AllUsers' in str(grant['Grantee']):
                    public_buckets.append(bucket_name)
        except Exception as e:
            print(f"Could not check {bucket_name}: {e}")

    if public_buckets:
        print("⚠️ Public S3 Buckets found:")
        for bucket in public_buckets:
            print(f" - {bucket}")
    else:
        print("✅ No public S3 buckets found.")

if __name__ == "__main__":
    check_public_s3_buckets()