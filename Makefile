.PHONY: build check serve deploy

# Rewrite generated blocks in the HTML from data/*.json.
build:
	python3 scripts/build.py

# Fail if the committed HTML is out of date with data/*.json.
check:
	python3 scripts/build.py --check

# Local preview at http://localhost:5000
serve: build
	firebase serve --only hosting

# Deploy = build, then firebase deploy.
deploy: build
	firebase deploy --only hosting
