include .env
.PHONY : init reset_guides_tours reset_guides init_elasticsearch load_guides_tours up down

init:
	pip install -r requirements.txt

reset_guides_tours:
	curl -XDELETE "${HOST}/guides_tours"

reset_guides:
	curl -XDELETE "${HOST}/guides"

init_elasticsearch:
	# create index for guides, using HOST and PORT from .env
	curl -XPUT "${HOST}/guides_tours" -H 'Content-Type: application/json' -d @mapping_guides_tours.json
	curl -XPUT "${HOST}/guides" -H 'Content-Type: application/json' -d @mapping_guides.json

load_guides_tours: 
	python3 load_guides_tours.py

up:
	docker-compose up -d

down:
	docker-compose down