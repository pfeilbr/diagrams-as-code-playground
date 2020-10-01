.PHONY: dev
dev:
	fswatch -o basic-serverless-application.py | xargs -n1 -I{} python basic-serverless-application.py