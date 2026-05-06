# Day 8 Summary - Docker Cache and Tagging

## What I learned
- Docker builds images layer by layer
- Docker can reuse unchanged layers using cache
- Dockerfile ordering affects build speed
- COPY . . too early can reduce cache efficiency
- Image tags help version Docker images
- Docker Hub can store and distribute built images

## Files created
- Dockerfile.bad
- Dockerfile.good
- notes-day-08.md
- commands-day-08.md
- daily-summary-day-08.md

## What I observed
- The bad Dockerfile invalidated cache more easily
- The good Dockerfile reused the dependency layer when only app code changed
- Changing requirements.txt caused dependency rebuild, which is expected

## What confused me
- Difference between image name and tag
- How cache behaves when requirements.txt changes

## What helped
- Building multiple times
- Changing only one file at a time
- Comparing bad and good Dockerfile layouts
