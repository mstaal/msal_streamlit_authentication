#############
# setup #
#############

docker_build: ## build docker image
	docker build -t streamlit .
.PHONY: docker_build


docker_run: ## run docker image
	 docker run -p 8501:8501 streamlit
.PHONY: docker_run
