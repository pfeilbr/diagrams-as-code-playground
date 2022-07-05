.PHONY: dev
dev:
#	fswatch -o basic-serverless-application.py | xargs -n1 -I{} python basic-serverless-application.py
	fswatch -o compute-guidance-stack.py | xargs -n1 -I{} python compute-guidance-stack.py
	