FROM ubuntu:16.04

# Install system dependencies
# Removing the package lists after installation is a good practice
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential curl g++ gcc gettext gfortran git git-core \
    graphviz graphviz-dev language-pack-en libffi-dev libfreetype6-dev libgeos-dev \
    libjpeg8-dev liblapack-dev libmysqlclient-dev libpng12-dev libxml2-dev \
    libxmlsec1-dev libxslt1-dev nodejs nodejs-legacy npm ntp pkg-config python-apt python-dev \
    python-pip software-properties-common swig && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app/edx-platform

# Install Python requirements
# ... adding only targeted requirements files first to benefit from caching
ADD ./src/edx-platform/requirements/edx /app/edx-platform/requirements/edx
RUN pip install --src ../src -r requirements/edx/pre.txt && \
    pip install --src ../src -r requirements/edx/github.txt && \
    pip install --src ../src -r requirements/edx/base.txt && \
    pip install --src ../src -r requirements/edx/paver.txt && \
    pip install --src ../src -r requirements/edx/post.txt

# Install Javascript requirements
# ... adding only the package.json file first to benefit from caching
ADD ./src/edx-platform/package.json /app/edx-platform/package.json
RUN npm install

# Now add the complete project sources
ADD ./src/edx-platform /app/edx-platform

# Install the project Python packages
RUN pip install --src ../src -r requirements/edx/local.txt

# Add configuration files
RUN mkdir -p /config && \
    ln -sf /config/lms.env.json /app/lms.env.json && \
    ln -sf /config/lms.auth.json /app/lms.auth.json && \
    ln -sf /config/docker_run_lms.py /app/edx-platform/lms/envs/docker_run.py && \
    ln -sf /config/cms.env.json /app/cms.env.json && \
    ln -sf /config/cms.auth.json /app/cms.auth.json && \
    ln -sf /config/docker_run_cms.py /app/edx-platform/cms/envs/docker_run.py

# Use Gunicorn in production as web server
CMD DJANGO_SETTINGS_MODULE=${SERVICE_VARIANT}.envs.docker_run \
    gunicorn --name=${SERVICE_VARIANT} --bind=0.0.0.0:8000 --max-requests=1000 ${SERVICE_VARIANT}.wsgi:application
