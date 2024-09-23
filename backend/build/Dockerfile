FROM osgeo/gdal:alpine-small-3.6.3

WORKDIR /app

# install python and requirements
RUN apk add --no-cache python3 py3-pip py3-virtualenv python3-dev libpq bash geos

# create a virtual env
RUN virtualenv venv
RUN source venv/bin/activate

COPY backend/build/requirements.txt .
RUN venv/bin/python -m pip install -r requirements.txt

COPY backend /app
# venv/bin/python manage.py collectstatic --noinput && \

CMD ["bash", "-c", \
    "venv/bin/python manage.py migrate && \
    venv/bin/python manage.py runserver 0.0.0.0:8000"]

# TODO: use gunicorn
