import boto3, os, re

def get_s3():
    s3client = boto3.client(
        's3',
        aws_access_key_id=os.environ.get('AWS_SUB_ACCESS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_SUB_SECRET_ACCESS_KEY')
        )

    theobjects = s3client.list_objects_v2(Bucket="drake-more-life")
    tmp=[]
    new=[]
    for object in theobjects["Contents"]:
        #anything that has mp3
        tmp.append(object["Key"].replace(".mp3", ''))
    #anything that has zip
    tmp=[ x for x in tmp if "zip" not in x ]
    for i in tmp:
        #clean up anything that may have:
        #   brackets or - or lyrics, only first 3
        #   geazy isn't searchable (change to g-eazy)
        #   tshirt and t-shirt
        new.append(' '.join(re.sub("[\(\[].*?[\)\]]", "", \
            i.replace("-", '')).lower().replace("lyrics", '').split()[:4]) \
            .replace("geazy", 'g-eazy').replace("tshirt", 't-shirt') )
    return new
