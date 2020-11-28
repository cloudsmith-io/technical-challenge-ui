# for flask: docker run --env-file=.flaskenv image flask run
FROM docker.cloudsmith.io/cloudsmith/challenges-pub/node:12-buster-slim AS node
FROM docker.cloudsmith.io/cloudsmith/challenges-pub/python:3.8

RUN mkdir /code
WORKDIR /code

COPY --from=node /usr/local/bin/ /usr/local/bin/
COPY --from=node /usr/lib/ /usr/lib/
# See https://github.com/moby/moby/issues/37965
RUN true
COPY --from=node /usr/local/lib/node_modules /usr/local/lib/node_modules
COPY requirements.txt setup.py tox.ini ./
RUN pip install -r requirements.txt
RUN pip install -e .

COPY package.json ./
RUN npm install

COPY webpack.config.js ./
COPY challenge challenge
COPY migrations migrations
COPY assets assets
COPY .flaskenv .env
RUN npm run-script build

EXPOSE 2992
EXPOSE 5000
CMD [ "npm", "start" ]
