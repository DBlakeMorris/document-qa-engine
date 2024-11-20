# syntax=docker/dockerfile:1
FROM nvidia/cuda:11.7.1-runtime-ubuntu22.04

# Update system and install Python and pip
RUN apt-get update && apt-get install -y \
    software-properties-common \
    g++-11 \
    make \
    python3 \
    python-is-python3 \
    pip

# Install Python packages individually with verbosity for troubleshooting
RUN pip install -v langchain==0.0.267
RUN pip install -v chromadb==0.4.6
RUN pip install -v pdfminer.six==20221105
RUN pip install -v sentence-transformers==2.2.2
RUN pip install -v faiss-cpu
RUN pip install -v huggingface_hub
RUN pip install -v transformers
# The following package installations are conditional based on the platform.
# Since Docker images are usually Linux-based, you might not need the macOS-specific conditions.
# Adjust or remove these lines according to your application's requirements and target deployment environment.
RUN pip install -v protobuf==3.20.2
RUN pip install -v 'auto-gptq==0.6.0'
RUN pip install -v docx2txt
RUN pip install -v unstructured
RUN pip install -v 'unstructured[pdf]'
RUN pip install -v urllib3==1.26.6
RUN pip install -v accelerate
RUN pip install -v click
RUN pip install -v flask
RUN pip install -v requests
RUN pip install -v openpyxl

# Copy the rest of your application's source code into the Docker image
COPY . .

ENV device_type=cuda

CMD ["python", "run_localGPT.py", "--device_type", "cuda"]














# syntax=docker/dockerfile:1
# Build as `docker build . -t localgpt`, requires BuildKit.
# Run as `docker run -it --mount src="$HOME/.cache",target=/root/.cache,type=bind --gpus=all localgpt`, requires Nvidia container toolkit.

#FROM nvidia/cuda:11.7.1-runtime-ubuntu22.04
#RUN apt-get update && apt-get install -y software-properties-common
#RUN apt-get install -y g++-11 make python3 python-is-python3 pip

# Use BuildKit cache mount to drastically reduce redownloading from pip on repeated builds
#RUN --mount=type=cache,target=/root/.cache \
#    pip install --timeout 100 -r requirements.txt && \
#    pip install azureml-sdk
# only copy what's needed at every step to optimize layer cache
#COPY ./requirements.txt .
# use BuildKit cache mount to drastically reduce redownloading from pip on repeated builds
#RUN --mount=type=cache,target=/root/.cache CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install --timeout 100 -r requirements.txt llama-cpp-python==0.1.83
#COPY SOURCE_DOCUMENTS ./SOURCE_DOCUMENTS
#COPY ingest.py constants.py ./
# Docker BuildKit does not support GPU during *docker build* time right now, only during *docker run*.
# See <https://github.com/moby/buildkit/issues/1436>.
# If this changes in the future you can `docker build --build-arg device_type=cuda  . -t localgpt` (+GPU argument to be determined).
#ARG device_type=cpu
#RUN --mount=type=cache,target=/root/.cache python ingest.py --device_type $device_type
#COPY . .
#ENV device_type=cuda
#CMD python run_localGPT.py --device_type $device_type
