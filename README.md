# lambda-headless-chrome
AWS lambda上にてheadless-chromeでseleniumを使用しpythonスクレイピングを行うサンプルコード

このコードは以下のページを参考にした。
>「Lambda上でスクレイピングするならDockerイメージを使おう」
>https://torahack.com/python-scraping-docker-for-lambda/

## Dockerイメージの作成
```
1. docker build -t lambda_fetch_links .
2. docker run -v "${PWD}":/var/task lambda_fetch_links
```
1. lambda_fetch_links : dockerイメージの名前
2. ビルドしたDockerイメージをDockerfileの内容に従って実行する。
lambda_fetch_links : 実行したいpythonファイル（lambda_fetch_links.py）。



## AWS CLIのセットアップ
```bash
pip install awscli
aws configure
（IAMユーザー情報を入力する）
```
参考
>DockerイメージをAWS Lambdaで使うIAM設定方法　https://torahack.com/how-configure-aws-iam/


## s3のbucketを作成する
参考
>手軽で最強のストレージサービスS3の概要と設定方法　https://torahack.com/how-to-use-s3/

## lambda常にDockerイメージをアップロードする
```bash
aws s3 cp deploy_package.zip s3://YOUR_BUCKET_NAME
aws lambda create-function --region ap-northeast-1 --function-name YOUR_FUNCTION_NAME --runtime python3.6 --role YOUR_ROLE_NAME --code S3Bucket=YOUR_BUCKET_NAME,S3Key=deploy_package.zip --handler YOUR_HANDLER --memory-size 512 --timeout 300
```
YOUR_FUNCTION_NAME : 関数名。ここでは「lambda_headless_chrome_python」

YOUR_BUCKET_NAME : あなたが作成したS3バケット名を指定

YOUR_ROLE_NAME : Lambdaの実行権限とS3の読み取り権限を持つIAMロールをarn形式で指定

YOUR_HANDLER : ハンドラーの指定（サービスでコードを実行する際に、lambdaが呼び出すコード内の関数）。ここでは「fetch_links.lambda_handler」

## lambda上で関数を実行する