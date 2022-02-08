FUNCTION =  <function-name>
REGION = us-west2
ENTRYPOINT = <command to call>
TOPIC = <optional to make deploy-pubsub>

deploy-http:
	@echo "Deploying HTTP ${FUNCTION}"
	@gcloud functions deploy ${FUNCTION} --region ${REGION} --entry-point ${ENTRYPOINT} --runtime python38 --trigger-http --allow-unauthenticated

deploy-pubsub:
	@echo "Deploying PubSub ${FUNCTION}"
	@gcloud functions deploy ${FUNCTION} --region ${REGION} --entry-point ${ENTRYPOINT} --runtime python38 --trigger-topic ${TOPIC} --allow-unauthenticated
