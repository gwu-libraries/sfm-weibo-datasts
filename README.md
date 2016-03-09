# sfm-weibo-datasts
A demo UI for analysis weibo status supporting sfm-weibo-harvester

# Install
```bash
git clone https://github.com/gwu-libraries/sfm-weibo-datasts
cd sfm-weibo-datasts
pip install -r requirements/requirements.txt
```

# Integration tests in docker containers

##Setting the warc file path in settings.py

```python
#Setting the warc file directory
DATA_DIR = os.path.join(ROOT_DIR,'datasts', 'data')
```

##Start up the containers

```bash
docker-compose -f docker/dev.docker-compose.yml up -d
```

##Load weibo to database

```bash
docker exec docker_sfmweibodatasts_1 python weiboanalysis/manage.py load_weibos
```

##Open your browser

```bash
http://localhost:8080
```

##Cleaning what your have done

```bash
docker-compose -f docker/dev.docker-compose.yml kill
docker-compose -f docker/dev.docker-compose.yml rm -v --force
docker rmi $(docker images -q)
```
