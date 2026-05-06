# Day 8 Notes - Docker Cache, Tags, and Registry Push

## What is Docker cache?
Docker cache is the reuse of previously built image layers when the corresponding Dockerfile instruction and input files have not changed.

## Why does Docker cache matter?
It makes rebuilds faster and avoids unnecessary dependency installation.

## What creates a layer in Docker?
Most Dockerfile instructions such as FROM, COPY, RUN, and WORKDIR create layers.

## Why does Dockerfile order matter?
If stable files are copied earlier and changing files later, Docker can reuse more cached layers.

## Bad Dockerfile pattern
Using `COPY . .` before dependency installation can invalidate cache too often.

## Better Dockerfile pattern
Copy dependency files like `requirements.txt` first, install dependencies, and only then copy the application code.

## What I observed
When I changed only app code, the good Dockerfile reused earlier layers better.
When I changed requirements.txt, the dependency layer rebuilt, which is correct.

## What is an image tag?
A tag is a version label attached to a Docker image.

## Why is latest a weak tag?
Because it does not clearly identify the exact version of the application.

## Better tagging strategy
Use meaningful tags such as v1, day8, build number, or commit-style tags.
