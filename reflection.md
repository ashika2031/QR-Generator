# Reflection: Dockerized QR Code Generator

This project taught me the complete cycle of building, containerizing, and deploying an application with Docker and GitHub Actions.  
I learned how to write a secure Dockerfile using a non-root user, create lightweight images with the `python:slim` base, and automate the build pipeline with CI/CD.  

Initially, I faced issues with authentication (DockerHub tokens and GitHub secrets) and architecture mismatch on Apple Silicon, which I solved by enabling multi-platform builds (`linux/amd64, linux/arm64`).  
Through this process, I gained a strong understanding of Docker security, Buildx configuration, and workflow automation — skills directly applicable to modern DevOps pipelines.
